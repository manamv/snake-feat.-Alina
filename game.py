# import pygame
# import random
# import pygame.mixer
# import sqlite3
# import datetime
#
# pygame.init()
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (70, 130, 180)
# dis_width = 800
# dis_height = 600
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Змейка')
# clock = pygame.time.Clock()
# snake_block = 10
# snake_speed = 15
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)
#
# pygame.mixer.init()
# death_sound = pygame.mixer.Sound('music/overau.mp3')
# good_sound = pygame.mixer.Sound('music/plusau.mp3')
#
#
# # выводит счёт
# def your_score(score):
#     value = score_font.render("Ваш счёт: " + str(score), True, yellow)
#     dis.blit(value, [0, 0])
#
#
# # движение змейки
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
#
#
# # основной функционал игры
# def game_loop():
#     pygame.mixer.music.load(f'music/gameau3.mp3')
#     pygame.mixer.music.play(-1)
#     game_over = False
#     game_close = False
#     x1 = dis_width / 2
#     y1 = dis_height / 2
#     x1_change = 0
#     y1_change = 0
#     snake_list = list()
#     length_of_snake = 1
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#     while not game_over:
#         while game_close:
#             dis.fill(blue)
#             message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
#             your_score(length_of_snake - 1)
#             pygame.display.update()
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         game_loop()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             death_sound.play()
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_head = list()
#         snake_head.append(x1)
#         snake_head.append(y1)
#         snake_list.append(snake_head)
#         if len(snake_list) > length_of_snake:
#             del snake_list[0]
#         for x in snake_list[:-1]:
#             if x == snake_head:
#                 death_sound.play()
#                 game_close = True
#         our_snake(snake_block, snake_list)
#         your_score(length_of_snake - 1)
#         pygame.display.update()
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             length_of_snake += 1
#             good_sound.play()
#         clock.tick(snake_speed)
#     pygame.quit()
#     conn = sqlite3.connect('scores.db')
#     conn.execute("INSERT INTO scores (date, score) VALUES (?, ?)",
#                  (datetime.date.today().strftime("%d.%m"), length_of_snake - 1))
#     conn.commit()
#     conn.close()
#     quit()
#
#
# # назначить музыку
# def mus_giv():
#     pass
#
#
# # сбор статистики
# def get_stats():
#     conn = sqlite3.connect('scores.db')
#     cursor = conn.execute("SELECT date, score FROM scores")
#     stat = ''
#     for row in cursor:
#         stat += f"{row[0]}: {row[1]}\n"
#     conn.close()
#     return stat
#
# # Размеры окна
# WIDTH, HEIGHT = 400, 300
#
# # Создание экрана
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Красивое окно завершения")
#
# # Цвета
# BACKGROUND_COLOR = (255, 255, 255)
# TEXT_COLOR = (0, 0, 0)
#
# # Шрифт
# font = pygame.font.Font(None, 40)
#
# # Фоновое изображение
# background_image = pygame.image.load("background.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
#
# # Основной цикл программы
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Отрисовка фонового изображения
#     screen.blit(background_image, (0, 0))
#
#     # Отрисовка текста на экране
#     text_surface = font.render("Игра завершена", True, TEXT_COLOR)
#     text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
#     screen.blit(text_surface, text_rect)
#
#     # Обновление экрана
#     pygame.display.flip()
#
# # Задержка перед закрытием окна
# pygame.time.delay(2000)
#
# # Завершение Pygame
# pygame.quit()
#
# # Завершение программы
# sys.exit()

import sqlite3
import pygame
import random
import sys
from pygame.color import THECOLORS
import datetime

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
HIGHSCORE = cursor.fetchone()[0]
cursor.close()
conn.close()


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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
                if event.key == pygame.K_w:
                    if direction[2] != DOWN:
                        to_direction = UP
                elif event.key == pygame.K_a:
                    if direction[2] != RIGHT:
                        to_direction = LEFT
                elif event.key == pygame.K_d:
                    if direction[2] != LEFT:
                        to_direction = RIGHT
                elif event.key == pygame.K_s:
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


def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAY, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAY, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))


def draw_apple(apple):
    draw_cell(apple, APPLE_OUTER_COLOR, APPLE_COLOR)


def draw_snake(snake):
    for coord in snake:
        draw_cell(coord, SNAKE_OUTER_COLOR, SNAKE_COLOR)


def draw_cell(cell, outer_color, inner_color):
    cellpos_x, cellpos_y = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
    cell = pygame.Rect(cellpos_x, cellpos_y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(DISPLAY, inner_color, cell, 0)
    pygame.draw.rect(DISPLAY, outer_color, cell, 4)


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
