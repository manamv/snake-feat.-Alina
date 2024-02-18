import pygame
import pygame_menu as pm
from main import game_loop, get_stats
import pygame.mixer

# Импортирование и инициализация Pygame
pygame.init()
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Стандартные цвета RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Главная функция программы
def main():
    pygame.mixer.init()
    pygame.mixer.music.load('music/menuau.mp3')
    pygame.mixer.music.play(-1)

    # Список, который отображается при выборе сложности
    colors = [("Черный", "Черный"),
              ("Розовый", "Розовый"),
              ("Фиолетовый", "Фиолетовый")]

    # Список, который отображается при выборе перспективы игрока
    music = [("1", "1"),
             ("2", "2"),
             ("3", "3")]

    # Функция отображения выбранных настроек
    def print_settings():
        print("\n\n")
        settings_data = settings.get_input_data()
        for key in settings_data.keys():
            print(f"{key}\t:\t{settings_data[key]}")

    # Создание меню настроек
    settings = pm.Menu(title="Настройки",
                       width=WIDTH,
                       height=HEIGHT,
                       theme=pm.themes.THEME_GREEN)

    stats = pm.Menu(title="Статистика",
                    width=WIDTH,
                    height=HEIGHT,
                    theme=pm.themes.THEME_GREEN)
    stats.add.label(get_stats())

    # Настройка значений по умолчанию
    settings._theme.widget_font_size = 25
    settings._theme.widget_font_color = BLACK
    settings._theme.widget_alignment = pm.locals.ALIGN_LEFT

    # Текстовый ввод для имени пользователя
    # 2 выпадающих списка для выбора уровня графики и разрешения
    # Переключатели для включения/выключения музыки и звука
    # Селектор для выбора уровня сложности
    settings.add.selector(title="Цвет",
                          items=colors,
                          selector_id="difficulty",
                          style="fancy",
                          default=0)

    # Ползунок для выбора значения с помощью ползунка
    # Стильный селектор (добавленный к стандартному селектору) для выбора между
    # видом от первого или третьего лица
    settings.add.selector(title="Музыка",
                          items=music,
                          default=0,
                          style="fancy",
                          selector_id="perspective")

    # 3 разные кнопки с разными стилями и назначением
    settings.add.button(title="Сохранить",
                        action=print_settings,
                        font_color=WHITE,
                        background_color=GREEN)
    settings.add.button(title="Сброс",
                        action=settings.reset_value,
                        font_color=WHITE,
                        background_color=RED)

    # Создание главного меню
    main_menu = pm.Menu(title="Меню",
                        width=WIDTH,
                        height=HEIGHT,
                        theme=pm.themes.THEME_GREEN)

    # Настройка значений по умолчанию
    main_menu._theme.widget_alignment = pm.locals.ALIGN_CENTER

    # Кнопка, запускающая игру
    main_menu.add.button(title="Играть",
                         action=game_loop,
                         font_color=BLACK,
                         background_color=GREEN)

    # Кнопка, открывающая меню настроек при клике
    main_menu.add.button(title="Настройки",
                         action=settings,
                         font_color=BLACK,
                         background_color=GREEN)

    # Кнопка, открывающая меню статистики при клике
    main_menu.add.button(title="Статистика",
                         action=stats,
                         font_color=BLACK,
                         background_color=GREEN)

    # Пустая метка, используемая для создания разделителя между двумя кнопками
    main_menu.add.label(title="")

    # Кнопка выхода, завершающая программу
    main_menu.add.button(title="Выход",
                         action=pm.events.EXIT,
                         font_color=WHITE,
                         background_color=RED)

    # Запуск главного меню на экране
    main_menu.mainloop(screen)


if __name__ == "__main__":
    main()
