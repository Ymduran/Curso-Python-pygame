"""
Nombre: Durán Breceda Lourdes Jamileth
Fecha: 02 junio 2025
Versión 0.5:


"""
#from email.headerregistry import Group

# Se importan los módulos necesarios.
import pygame
from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh
from Media import Background
from Soldier import Soldier
from Shot import Shot
from pygame.sprite import Group


def run_game() -> None:
    """ Función principal del videojuego. """
    # Se inicializa el módulo de pygame y se realizan las configuraciones iniciales.
    pygame.init()
    screen_size = Configurations.get_screen_size()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()  # Se usa para controlar la velocidad de fotogramas (FPS).

    # Se configura el título de la ventana.
    game_title = Configurations.get_game_title()
    pygame.display.set_caption(game_title)

    # Se crea el objeto del fondo de pantalla.
    background = Background()

    # Se crea el objeto del soldado (personaje principal).
    soldier = Soldier(screen)
    #shot = Shot(soldier)

    shots = Group()
    #shots.add(shot)

    aliens = Group()

    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:

        # Función que administra los eventos del juego.
        game_over = game_events(soldier, shots, aliens, screen)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, background, soldier, shots, aliens)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()


if __name__ == "__main__":
    run_game()