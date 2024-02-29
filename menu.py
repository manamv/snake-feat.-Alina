import pygame
import pygame_menu as pm
import game
import pygame.mixer

# Импортирование и инициализация Pygame
pygame.init()
WIDTH, HEIGHT = 640, 480
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
    pygame.display.set_caption('Меню')
    pygame.mixer.init()
    pygame.mixer.music.load('music/menuau.mp3')
    pygame.mixer.music.play(-1)

    # скины
    colors = [("Черный",),
              ("Розовый",),
              ("Фиолетовый",)]

    # музыка
    music = [("1",),
             ("2",),
             ("3",)]

    meanings = list()

    # Функция отображения выбранных настроек
    def print_settings():
        print("\n\n")
        settings_data = settings.get_input_data()
        for key in settings_data.keys():
            print(f"{key}\t:\t{settings_data[key]}")
            meanings.append(settings_data[key][-1])
        print(meanings)

    # Создание меню настроек
    settings = pm.Menu(title="Настройки",
                       width=WIDTH,
                       height=HEIGHT,
                       theme=pm.themes.THEME_DARK)

    stats = pm.Menu(title="Статистика",
                    width=WIDTH,
                    height=HEIGHT,
                    theme=pm.themes.THEME_DARK)
    stats.add.label(game.get_stats())

    # Настройка значений по умолчанию
    settings._theme.widget_font_size = 25
    settings._theme.widget_font_color = BLACK
    settings._theme.widget_alignment = pm.locals.ALIGN_LEFT

    settings.add.selector(title="Цвет",
                          items=colors,
                          selector_id="color",
                          style="fancy",
                          default=0)

    settings.add.selector(title="Музыка",
                          items=music,
                          default=0,
                          style="fancy",
                          selector_id="music")

    settings.add.button(title="Сохранить",
                        action=print_settings,
                        font_color=WHITE)
    settings.add.button(title="Сброс",
                        action=settings.reset_value,
                        font_color=WHITE)

    main_menu = pm.Menu(title="Меню",
                        width=WIDTH,
                        height=HEIGHT,
                        theme=pm.themes.THEME_DARK)

    main_menu._theme.widget_alignment = pm.locals.ALIGN_CENTER

    # Кнопка, запускающая игру
    main_menu.add.button(title="Играть",
                         action=game.game_loop,
                         font_color=BLACK)

    # Кнопка, открывающая меню настроек при клике
    main_menu.add.button(title="Настройки",
                         action=settings,
                         font_color=BLACK)

    # Кнопка, открывающая меню статистики при клике
    main_menu.add.button(title="Статистика",
                         action=stats,
                         font_color=BLACK)

    # Пустая метка, используемая для создания разделителя между двумя кнопками
    main_menu.add.label(title="")

    # Кнопка выхода, завершающая программу
    main_menu.add.button(title="Выход",
                         action=pm.events.EXIT,
                         font_color=WHITE)

    # Запуск главного меню на экране
    main_menu.mainloop(screen)


if __name__ == "__main__":
    main()
