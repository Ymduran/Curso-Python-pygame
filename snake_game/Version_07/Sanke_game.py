"""
Nombre: Durán Breceda Lourdes Jamileth
Fecha: 210425
Versión 0.5:
    - Se crea la pantalla de inicio.
    - Se configura el título de la pantalla.
    - Configuraciones del juego.
    - Se agregó el módulo Game_funcionalities.py
    - Se agrega bloques al cuerpo de la serpiente.
"""

#from email.headerregistry import Group

#Se importan los módulos
import pygame
from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh, snake_movement
from Snake import SnakeBlock
from pygame.sprite import Group
from Apple import Apple




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


    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:
        """CAMBIO. Ahora recibe el cuerpo de la serpiente para añadir el nuevo bloque al presionar 'espacio'."""
        # Función que administra los eventos del juego.
        game_over = game_events(snake_body)

        # Función que administra el movimiento de la serpiente.
        snake_movement(snake_body)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, snake_body, apple)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()


if __name__ == "__main__":
    run_game()