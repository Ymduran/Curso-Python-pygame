from email.headerregistry import Group

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


    if event.type == pygame.KEYDOWN:    # Tipo de evento sea precionar una tecla
        if event.key == pygame.K_RIGHT:
            SnakeBlock.set_is_moving_rigth(True)
            SnakeBlock.set_is_moving_left(False)
            SnakeBlock.set_is_moving_up(False)
            SnakeBlock.set_is_moving_down(False)

        if event.key == pygame.K_LEFT:
            SnakeBlock.set_is_moving_rigth(False)
            SnakeBlock.set_is_moving_left(True)
            SnakeBlock.set_is_moving_up(False)
            SnakeBlock.set_is_moving_down(False)

        if event.key == pygame.K_UP:
            SnakeBlock.set_is_moving_rigth(False)
            SnakeBlock.set_is_moving_left(False)
            SnakeBlock.set_is_moving_up(True)
            SnakeBlock.set_is_moving_down(False)

        if event.key == pygame.K_DOWN:
            SnakeBlock.set_is_moving_rigth(False)
            SnakeBlock.set_is_moving_left(False)
            SnakeBlock.set_is_moving_up(False)
            SnakeBlock.set_is_moving_down(True)

    # Se regresa la bandera
    return game_over


def snake_movment(snake_body : pygame.sprite.Group) -> None:
    """
    Función que gestiona el movimiento del cuerpo de la serpiente.
    :param: snake_body: Grupo con el cuerpi de la serpiente
    """
    head = snake_body.sprites()[0]
    if SnakeBlock.get_is_moving_rigth():
        head.rect.x += Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_down():
        head.rect.y -= Configurations.get_snake_block_size()





def screen_refresh(screen: pygame.surface.Surface, snake_body: pygame.sprite.Group, clock: pygame.time.Clock) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    # Fondo de la pantalla en formato RGB.
    screen.fill(Configurations.get_background())

    # Se dibuja el cuerpo de la serpiente.
    for snake_block in snake_body.sprites():
        snake_block.blit(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de fps del juego.
    clock.tick(Configurations.get_fps())