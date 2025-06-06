"""
Nombre:
Fecha:
Versión 0.4:
    - Se crea la pantalla de inicio.
    - Se configura el título de la pantalla.
    - Configuraciones del juego.
    - Se agregó el módulo Game_funcionalities.py
"""

#Se importan los módulos
import pygame
from snake_game.Version_04.Configurations import Configurations
from snake_game.Version_04.Game_funcionalities import game_events, screen_refresh
from Snake import SnakeBlock





def run_game()->None:
    """
    Función principal del videojuego.
    :return:
    """
    # Se incia el módulo pygame.
    pygame.init()

    # Se configura reloj del juego.
    clock = pygame.time.Clock()

    # Se inicaliza la pantalla.
    #screen_size = (1280, 720)   #Resolución de la pantalla (ancho x alto)
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    # Se configura el título del juego.
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())


    # Se crea el bloque inicial de la serpiente
    snake_head = SnakeBlock(is_head = True)
    snake_head.snake_head_init()


    #Ciclo principal del videojuego.
    game_over = False

    while not game_over:
        # Se verifican los eventos del teclado (mouse y teclado) del juego.
        game_over = game_events()

        # Se dibujan los elementos de la pantalla.
        screen_refresh(screen,snake_head, clock)


    # Cerrar los recursos de pygame
    pygame.quit()


if __name__ == '__main__':
    run_game()