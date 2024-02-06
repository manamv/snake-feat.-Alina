import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Меню змейки")

background_image = pygame.image.load(r"D:\memes\4onmsPmivoQ.jpg").convert()


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)  # Нарисовать прямоугольник кнопки
        font = pygame.font.Font(None, 36)
        text_render = font.render(self.text, True, (255, 255, 255))
        surface.blit(text_render, (self.rect.x + 10, self.rect.y + 10))  # Нарисовать текст кнопки

    def clicked(self, event):
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True


play_button = Button(150, 200, 200, 50, "Играть")
quit_button = Button(450, 200, 200, 50, "Выйти")
settings_button = Button(300, 300, 200, 50, "Настройки")
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if play_button.clicked(event):
            print("Кнопка Играть нажата")

        if quit_button.clicked(event):
            running = False

    screen.blit(background_image, (0, 0))  # Нарисовать фоновое изображение

    play_button.draw(screen)  # Нарисовать кнопку Играть
    quit_button.draw(screen)  # Нарисовать кнопку Выйти
    settings_button.draw(screen) # Нарисовать кнопку Настройки

    pygame.display.flip()
pygame.quit()
