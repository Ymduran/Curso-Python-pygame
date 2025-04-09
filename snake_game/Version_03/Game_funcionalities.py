import pygame
from snake_game.Version_03.Configurations import Configurations
from Snake import SnakeBlock

def game_events() -> bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin de juego.
    """
    #Se declara la bandera de fin de juego.
    game_over = False

    # Se verifican los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        print(event)
        # Clic en cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True

    return game_over


def screen_refresh(screen: pygame.surface.Surface, snake_head: SnakeBlock) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    # Fondo de la pantalla en formato RGB.
    screen.fill(Configurations.get_background())

    # Se dibuja la cabeza de la serpiente.
    snake_head.blit(screen)



    # Se actualiza la pantalla.
    pygame.display.flip()