import pygame
import pygame_menu as pm
from main import gameLoop
import pygame.mixer

pygame.mixer.init()
menu_sound = pygame.mixer.music.load('music/menuau.mp3')
pygame.init()

WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Standard RGB colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Main function of the program


def main():
    pygame.mixer.music.play(-1)
    # List that is displayed while selecting the difficulty
    colors = [("Черный", "Черный"),
              ("Розовый", "Розовый"),
              ("Фиолетовый", "Фиолетовый")]

    # List that is displayed while selecting the player's perspective
    music = [("1", "1"),
             ("2", "2"),
             ("3", "3")]

    # This function displays the currently selected options

    def printSettings():
        print("\n\n")
        # getting the data using "get_input_data" method of the Menu class
        settingsData = settings.get_input_data()

        for key in settingsData.keys():
            print(f"{key}\t:\t{settingsData[key]}")

            # Creating the settings menu

    settings = pm.Menu(title="Настройки",
                       width=WIDTH,
                       height=HEIGHT,
                       theme=pm.themes.THEME_GREEN)

    stats = pm.Menu(title="Статистика",
                    width=WIDTH,
                    height=HEIGHT,
                    theme=pm.themes.THEME_GREEN)

    # Adjusting the default values
    settings._theme.widget_font_size = 25
    settings._theme.widget_font_color = BLACK
    settings._theme.widget_alignment = pm.locals.ALIGN_LEFT

    # Text input that takes in the username

    # 2 different Drop-downs to select the graphics level and the resolution level

    # Toggle switches to turn on/off the music and sound

    # Selector to choose between the types of difficulties available
    settings.add.selector(title="Цвет\t", items=colors,
                          selector_id="difficulty", style="fancy", default=0)

    # Range slider that lets to choose a value using a slider

    # Fancy selector (style added to the default selector) to choose between
    # first person and third person perspectives
    settings.add.selector(title="Музыка", items=music,
                          default=0, style="fancy", selector_id="perspective")

    # 3 different buttons each with a different style and purpose
    settings.add.button(title="Сохранить", action=printSettings,
                        font_color=WHITE, background_color=GREEN)
    settings.add.button(title="Сброс", action=settings.reset_value,
                        font_color=WHITE, background_color=RED)

    # Creating the main menu
    mainMenu = pm.Menu(title="Меню",
                       width=WIDTH,
                       height=HEIGHT,
                       theme=pm.themes.THEME_GREEN)

    # Adjusting the default values
    mainMenu._theme.widget_alignment = pm.locals.ALIGN_CENTER

    mainMenu.add.button(title="Играть", action=gameLoop,
                        font_color=BLACK, background_color=GREEN)

    # Button that takes to the settings menu when clicked
    mainMenu.add.button(title="Настройки", action=settings,
                        font_color=BLACK, background_color=GREEN)

    mainMenu.add.button(title="Статистика", action=stats,
                        font_color=BLACK, background_color=GREEN)
    # An empty label that is used to add a seperation between the two buttons
    mainMenu.add.label(title="")

    # Exit button that is used to terminate the program
    mainMenu.add.button(title="Выход", action=pm.events.EXIT,
                        font_color=WHITE, background_color=RED)

    # Lets us loop the main menu on the screen
    mainMenu.mainloop(screen)


if __name__ == "__main__":
    main()
