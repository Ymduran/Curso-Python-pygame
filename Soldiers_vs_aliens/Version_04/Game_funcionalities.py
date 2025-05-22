import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldier

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                soldier._is_movig_up = False
            if event.key == pygame.K_DOWN:
                soldier._is_moving_down = False
        #if event.type == pygame.QUIT:
            #game_over = True

    return game_over








def screen_refresh(screen: pygame.surface.Surface, background:Background, soldier: Soldier, clock: pygame.time.Clock) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    # Se dibuja el fondo de la pantalla
    background.blit(screen)

    soldier.blit(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    clock.tick(Configurations.get_fps())