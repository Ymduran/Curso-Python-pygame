"""
Nombre: Durán Breceda Lourdes Jamileth
Fecha: 280425
Versión 12:
-

"""
# Se importan los módulos.
import pygame
#from pygments.styles.dracula import background

from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh, snake_movement, check_collision, game_over_screen
from Snake import SnakeBlock
from pygame.sprite import Group
from Apple import Apple
from Media import Background, Audio, Scoreboard


def run_game() -> None:
    """ Función principal del videojuego. """
    # Se inicializa el módulo de pygame y se realizan las configuraciones iniciales.
    pygame.init()
    screen = pygame.display.set_mode(Configurations.get_screen_size())  # Resolución de la pantalla (ancho, alto).
    pygame.display.set_caption(Configurations.get_game_title())         # Se configura el título de la ventana.
    clock = pygame.time.Clock()                     #  Se usa para controlar la velocidad de fotogramas (FPS).

    # Se crea el bloque inicial de la serpiente (cabeza) y se inicializa en un lugar aleatorio de la pantalla.
    snake_head = SnakeBlock(is_head = True)
    snake_head.snake_head_init()

    # Se crea un grupo que va a almacenar el cuerpo de la serpiente, por lo que se agrega la cabeza de la serpiente.
    snake_body = Group()
    snake_body.add(snake_head)


    # Se crea el bloque inicial de la manzana.
    apple = Apple()
    apple.random_position(snake_body)

    # Se crea un grupo con las manzanas.
    apples = Group()
    apples.add(apple)

    background = Background()

    # Se crea el objeto con el sonido del juego y se reproduce la música y el sonido inicial del juego.
    audio = Audio() # Audio.play_music(0.25)
    audio.play_music(volume=Configurations.get_music_volume())
    audio.play_star_sound()

    # Se crea el objeto
    scoreboard = Scoreboard()



    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:

        # Función que administra los eventos del juego.
        game_over = game_events()


        # Si el usuario ha cerrado la ventana, entonces se termina el ciclo inmediatamente para cerrar la ventana.
        if game_over:
            break

        # Función que administra el movimiento de la serpiente.
        snake_movement(snake_body)


        # Función que revisa las colisiones en el juego.
        game_over = check_collision(screen, snake_body, apples, audio, scoreboard)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, snake_body, apples, background, scoreboard)


        # Si el usuario ha perdido la partida, entonces se llama a la función que muestra la pantalla
        # del fin del juego.
        if game_over:
            game_over_screen(audio, screen)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()



if __name__ == "__main__":
    run_game()