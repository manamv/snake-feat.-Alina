import pygame
import sys
import sqlite3
import menu


# меню конца игры
def game_over():
    pygame.init()
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Конец игры")
    font = pygame.font.Font(None, 64)
    text_surface = font.render("Конец игры", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 2))

    # Создание кнопок
    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Вернуться в меню", True, (255, 255, 255))
    button_width = button_text.get_width() + 20
    button_height = button_text.get_height() + 10
    button_rect = pygame.Rect((screen_width - button_width) // 2,
                              (screen_height - button_height) // 2 + 100,
                              button_width, button_height)

    # Подключение к базе данных
    conn = sqlite3.connect("scores.db")
    cursor = conn.cursor()

    # Выполнение запроса для получения статистики игры
    cursor.execute("SELECT date, score FROM scores")
    rows = cursor.fetchall()

    # Формирование текста статистики игры
    stats_text = ""
    stats_text += f"Ваш счёт: {rows[-1][-1]}\n"

    # Закрытие соединения с базой данных
    cursor.close()
    conn.close()

    stats_font = pygame.font.Font(None, 24)
    stats_surface = stats_font.render(stats_text, True, (255, 255, 255))
    stats_rect = stats_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 40))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    running = False
                    menu.main()  # Вызов функции главного меню

        screen.fill((0, 0, 0))
        screen.blit(text_surface, text_rect)
        screen.blit(stats_surface, stats_rect)

        # Отрисовка кнопок
        pygame.draw.rect(screen, (100, 100, 100), button_rect)
        screen.blit(button_text, button_rect.move(10, 5))

        pygame.display.flip()

    pygame.quit()
    sys.exit()
