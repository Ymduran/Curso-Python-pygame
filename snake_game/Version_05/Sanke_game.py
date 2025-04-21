"""
Nombre: Durán Breceda Lourdes Jamileth
Fecha: 210425
Versión 0.5:
    - Se crea la pantalla de inicio.
    - Se configura el título de la pantalla.
    - Configuraciones del juego.
    - Se agregó el módulo Game_funcionalities.py
"""
from email.headerregistry import Group

#Se importan los módulos
import pygame
from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh, snake_movment
from Snake import SnakeBlock
from pygame.sprite import Group




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

    snake_body = Group()
    snake_body.add(snake_head)



    #Ciclo principal del videojuego.
    game_over = False

    while not game_over:
        # Se verifican los eventos del teclado (mouse y teclado) del juego.
        game_over = game_events()

        # Se administra el movimiento de la serpiente.
        snake_movment(snake_body)

        # Se dibujan los elementos de la pantalla.
        screen_refresh(screen,snake_body, clock)


    # Cerrar los recursos de pygame
    pygame.quit()


if __name__ == '__main__':
    run_game()