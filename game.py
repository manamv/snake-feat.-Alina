import sqlite3
import pygame
import random
import sys
from pygame.color import THECOLORS
import datetime
import ending

pygame.mixer.init()
death_sound = pygame.mixer.Sound('music/overau.mp3')
good_sound = pygame.mixer.Sound('music/plusau.mp3')

# Размеры окна в пикселях
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

CELL_SIZE = 20

# Размеры сетки в ячейках
WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)

# Цвета
BG_COLOR = (0, 0, 0)
GRID_COLOR = (40, 40, 40)
APPLE_COLOR = (255, 0, 0)
APPLE_OUTER_COLOR = (155, 0, 0)
SNAKE_COLOR = (0, 255, 0)
SNAKE_OUTER_COLOR = (0, 155, 0)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0

FPS = 5
POINTS = 0

conn = sqlite3.connect('scores.db')
cursor = conn.cursor()
cursor.execute('SELECT MAX(score) FROM scores')
HIGHSCORE = int(cursor.fetchone()[0])
cursor.close()
conn.close()


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# игра
def main():
    global FPS_CLOCK
    global DISPLAY

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Змейка')

    while True:
        pygame.mixer.music.load(f'music/gameau3.mp3')
        pygame.mixer.music.play(-1)
        run_game()


def run_game():
    applepos = [20, 10]
    multiplier = 0
    direction = [1, 0, RIGHT]
    to_direction = RIGHT
    snake = [[5, 10, 4, 10], [4, 10, 3, 10], [3, 10, 2, 10]]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP):
                    if direction[2] != DOWN:
                        to_direction = UP
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    if direction[2] != RIGHT:
                        to_direction = LEFT
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    if direction[2] != LEFT:
                        to_direction = RIGHT
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    if direction[2] != UP:
                        to_direction = DOWN

        change_direction(direction, to_direction)
        move_snake(snake, direction)
        global FPS
        global HIGHSCORE
        global POINTS
        global good_sound
        if snake_hit_self(snake) or snake_hit_edge(snake):
            FPS = 5
            POINTS = 0
            ending.game_over()
            break
        if snake_hit_apple(snake, applepos):
            good_sound.play()
            snake_grow(snake)
            applepos = new_apple(snake)
            POINTS += 1
            if HIGHSCORE < POINTS:
                HIGHSCORE = POINTS
            multiplier += 1
            if multiplier == 5:
                FPS += 1
                multiplier = 0
                print(f"Difficulty: {FPS}")
        draw_frame(snake, applepos)
        FPS_CLOCK.tick(FPS)


# нарисовать поле
def draw_frame(snake, apple):
    global FPS
    global POINTS
    global HIGHSCORE
    DISPLAY.fill(BG_COLOR)
    draw_grid()
    draw_snake(snake)
    draw_apple(apple)
    font = pygame.font.SysFont('couriernew', 30)
    text = font.render(str(f'Сложность: {FPS - 5}'), True, THECOLORS['white'])
    DISPLAY.blit(text, (0, 0))
    font = pygame.font.SysFont('couriernew', 15)
    text = font.render(str(f'Очки: {POINTS}'), True, THECOLORS['white'])
    DISPLAY.blit(text, (0, 40))
    text = font.render(str(f'Рекорд: {HIGHSCORE}'), True, THECOLORS['white'])
    DISPLAY.blit(text, (0, 60))
    pygame.display.set_caption(f'Wormy | Сложность: {FPS - 5} | Очки: {POINTS} | Рекорд: {HIGHSCORE}')
    pygame.display.update()


# отрисовка сетки
def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAY, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAY, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))


# добавить яблоко
def draw_apple(apple):
    draw_cell(apple, APPLE_OUTER_COLOR, APPLE_COLOR)


# отрисовка змейки
def draw_snake(snake):
    for coord in snake:
        draw_cell(coord, SNAKE_OUTER_COLOR, SNAKE_COLOR)


def draw_cell(cell, outer_color, inner_color):
    cellpos_x, cellpos_y = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
    cell = pygame.Rect(cellpos_x, cellpos_y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(DISPLAY, inner_color, cell, 0)
    pygame.draw.rect(DISPLAY, outer_color, cell, 4)


# движение змейки
def move_snake(snake, direction):
    for cell in snake:
        if cell == snake[0]:
            cell[2] = cell[0]
            cell[3] = cell[1]
            cell[0] += direction[0]
            cell[1] += direction[1]
        else:
            cell[2] = cell[0]
            cell[3] = cell[1]
            cell[0] = snake[snake.index(cell) - 1][2]
            cell[1] = snake[snake.index(cell) - 1][3]


# змейка вышла за грани
def snake_hit_edge(snake):
    global death_sound
    flag = False
    head = [snake[0][0], snake[0][1]]
    if head[0] < 0 or head[0] > WINDOW_WIDTH // CELL_SIZE or head[1] < 0 or head[1] > WINDOW_HEIGHT // CELL_SIZE:
        flag = True
    if flag:
        set_stats()
        death_sound.play()
    return flag


# самоубийство
def snake_hit_self(snake):
    global death_sound
    flag = False
    head = [snake[0][0], snake[0][1]]
    for i in range(1, len(snake)):
        if snake[i][0] == head[0] and snake[i][1] == head[1]:
            flag = True
    if flag:
        set_stats()
        death_sound.play()
    return flag


# съесть яблоко
def snake_hit_apple(snake, apple):
    for cell in snake:
        if cell[0] == apple[0] and cell[1] == apple[1]:
            return True


def snake_grow(snake):
    snake.append([snake[-1][2], snake[-1][3], snake[-1][2], snake[-1][3]])


# генерация яблока
def new_apple(snake):
    while True:
        x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1)
        y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1)
        for cell in snake:
            if cell[0] != x and cell[1] != y:
                return [x, y]


# смена направления
def change_direction(direction, to_direction):
    if to_direction == UP:
        if direction[2] != DOWN:
            direction[0] = 0
            direction[1] = -1
            direction[2] = to_direction
    elif to_direction == LEFT:
        if direction[2] != RIGHT:
            direction[0] = -1
            direction[1] = 0
            direction[2] = to_direction
    elif to_direction == RIGHT:
        if direction[2] != LEFT:
            direction[0] = 1
            direction[1] = 0
            direction[2] = to_direction
    elif to_direction == DOWN:
        if direction[2] != UP:
            direction[0] = 0
            direction[1] = 1
            direction[2] = to_direction


# установка статистики
def set_stats():
    global POINTS
    conn = sqlite3.connect('scores.db')
    conn.execute("INSERT INTO scores (date, score) VALUES (?, ?)",
                 (datetime.date.today().strftime("%d.%m"), POINTS))
    conn.commit()
    conn.close()


# сбор статистики
def get_stats():
    conn = sqlite3.connect('scores.db')
    cursor = conn.execute("SELECT date, score FROM scores")
    stat = ''
    for row in cursor:
        stat += f"{row[0]}: {row[1]}\n"
    conn.close()
    return stat


# запуск игры
def game_loop():
    pygame.mixer.music.stop()
    main()


# закрытие игры
def terminate():
    pygame.quit()
    sys.exit()
