"""
Nombre: Durán Breceda Lourdes Jamileth
Fecha: 240425
Versión 0.8:
- Se agregaron las colisiones del juego.

"""
# Se importan los módulos.
import pygame
from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh, snake_movement, check_collision, game_over_screen
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
    apple.random_position(snake_body)

    # Se crea un grupo con las manzanas.
    apples = Group()
    apples.add(apple)


    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:
        # Función que administra los eventos del juego.
        game_over = game_events()

        # Condición para cerrar la ventana
        if game_over: break

        # Función que administra el movimiento de la serpiente.
        snake_movement(snake_body)


        # Se revisan las colisiones en el juego.
        game_over = check_collision(screen, snake_body, apples)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, snake_body, apples)
        
        # Cuando el jugador pierde se llama a la pantalla de fin de juego.
        if game_over: game_over_screen()


    # Cierra todos los recursos del módulo pygame.
    pygame.quit()


if __name__ == "__main__":
    run_game()