"""
Nombre:
Fehca:
Versión 0.3:
    - Se crea la pantalla de inicio.
    - Se configura el título de la pantalla.
    - Configuraciones del juego.
    - Se agregó el módulo Game_funcionalities.py
"""

#Se importan los módulos
import pygame


from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh
from Media import Background
from Soldier import Soldier





def run_game()->None:
    """
    Función principal del videojuego.
    :return:
    """
    # Se incia el módulo pygame.
    pygame.init()

    clock = pygame.time.Clock()

    # Se inicaliza la pantalla.
    #screen_size = (1280, 720)   #Resolución de la pantalla (ancho x alto)
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    background=Background()

    # Se configura el título del juego.
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())
    soldier = Soldier()
    soldier.soldier_init(screen)


    #Ciclo principal del videojuego.
    game_over = False

    while not game_over:
        # Se verifican los eventos del teclado (mouse y teclado) del juego.
        game_over = game_events()

        # Se dibujan los elementos de la pantalla
        screen_refresh(screen, background, soldier, clock)


    # Cerrar los recursos de pygame
    pygame.quit()


if __name__ == '__main__':
    run_game()