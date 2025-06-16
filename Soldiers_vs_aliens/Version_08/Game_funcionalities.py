import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Shot import Shot
from Alien import Alien


def game_events(soldier: Soldier, shots: pygame.sprite.Group) -> bool:
    """
    Función que administra los eventos del juego.
    :param soldier: Objeto con el soldado (personaje principal).
    :param shots:

    :return: La bandera de fin del juego.

    """
    # Se declara la bandera de fin del juego que se retorna.
    game_over = False

    # Se verifican los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # El evento es un clic para cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True


        # Se verifica el evento de presionar una tecla.
        if event.type == pygame.KEYDOWN:
            # Se verifica las flechas para el movimiento.
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

            # Si se presionó el espacio, entonces se crea un nuevo disparo y se agrega al grupo. Además, indica que
            # el soldado está disparando.
            if event.key == pygame.K_SPACE:
                new_shot = Shot(soldier)
                shots.add(new_shot)
                soldier.shoots()





        # Se verifica el evento de soltar una tecla.
        if event.type == pygame.KEYUP:
            # Se verifica las flechas para dejar de moverse.
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False



    # Se regresa la bandera.
    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   soldier: Soldier, shots: pygame.sprite.Group,
                   aliens: pygame.sprite.Group) -> None:
    """
    Función que administra los elementos de la pantalla.
    :param screen: Objeto con la pantalla.
    :param clock: Objeto con el reloj del videojuego.
    :param background: Objeto con el fondo de pantalla.
    :param soldier: Objeto con el soldado (personaje principal).
    :param shots: Bala
    :param aliens:
    """
    # Se dibuja el fondo de la pantalla.
    background.blit(screen)

    for shot in shots.sprites():
        shot.update_position(screen)
        shot.update_animation()
        shot.blit(screen)

    shots.draw(screen)

    for alien in aliens.sprites():
        alien.update_position(screen)
        alien.update_animation()
        alien.blit(screen)


    # Se actualiza la posición del soldado, se anima su sprite y se dibuja en la pantalla.
    soldier.update_position(screen)
    soldier.update_animation()
    soldier.blit(screen)




    # Se actualiza la pantalla, dando la impresión de movimiento.
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())





