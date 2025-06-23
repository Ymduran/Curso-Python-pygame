import pygame
from pygame.sprite import Group
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Soldier2 import Soldier2
from Shot import Shot
from Alien import Alien
from Score import Score
from AudioManager import AudioManager
from random import randint


def game_events(soldier: Soldier,
                soldier2: Soldier2,
                shots: Group,
                audio: AudioManager) -> bool:
    """
    Maneja los eventos de entrada para ambos jugadores.

    Args:
        soldier: Instancia del primer jugador
        soldier2: Instancia del segundo jugador
        shots: Grupo de disparos activos
        audio: Gestor de efectos de sonido

    Returns:
        bool: True si el juego debe terminar
    """
    game_over = False
    controls = Configurations.get_second_player_controls()  # Controles del jugador 2

    for event in pygame.event.get():
        # Evento de salida
        if event.type == pygame.QUIT:
            game_over = True

        # Eventos de tecla presionada
        if event.type == pygame.KEYDOWN:
            # Jugador 1 - Controles originales
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True
            if event.key == pygame.K_SPACE and len(shots) < 4:  # Límite aumentado
                shots.add(Shot(soldier))
                audio.play_sound('shot')
                soldier.shoots()

            # Jugador 2 - Nuevos controles
            if event.key == controls["move_up"]:
                soldier2.is_moving_up = True
            if event.key == controls["move_down"]:
                soldier2.is_moving_down = True
            if event.key == controls["shoot"] and len(shots) < 4:
                shots.add(Shot(soldier2))
                audio.play_sound('shot')
                soldier2.shoots()

        # Eventos de tecla liberada
        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

            # Jugador 2
            if event.key == controls["move_up"]:
                soldier2.is_moving_up = False
            if event.key == controls["move_down"]:
                soldier2.is_moving_down = False

    return game_over


def check_collisions(screen: pygame.Surface,
                     soldier: Soldier,
                     soldier2: Soldier2,
                     shots: Group,
                     aliens: Group,
                     score: Score,
                     audio: AudioManager) -> bool:
    """
    Detecta colisiones entre elementos del juego.

    Args:
        screen: Superficie de la pantalla
        soldier: Primer jugador
        soldier2: Segundo jugador
        shots: Grupo de disparos
        aliens: Grupo de aliens
        score: Marcador de puntos
        audio: Gestor de sonidos

    Returns:
        bool: True si el juego debe terminar
    """
    game_over = False
    screen_rect = screen.get_rect()

    # Colisiones disparo-alien (elimina ambos)
    collisions = pygame.sprite.groupcollide(shots, aliens, True, True)

    if collisions:
        audio.play_sound('alien_hit')
        for aliens_hit in collisions.values():
            score.increase()  # +1 punto por cada alien impactado

    # Limpieza de elementos fuera de pantalla
    for alien in aliens.copy():
        if alien.rect.left > screen_rect.right:
            aliens.remove(alien)

    for shot in shots.copy():
        if shot.rect.right < screen_rect.left or shot.rect.left > screen_rect.right:
            shots.remove(shot)

    # Colisiones jugadores-alien (game over)
    if (pygame.sprite.spritecollide(soldier, aliens, False) or
            pygame.sprite.spritecollide(soldier2, aliens, False)):
        audio.play_sound('game_over')
        game_over = True

    # Generación de nuevos aliens si quedan pocos
    if len(aliens) <= Configurations.get_min_aliens():
        for _ in range(randint(0, 5)):
            aliens.add(Alien(screen))

    return game_over


def screen_refresh(screen: pygame.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   soldier: Soldier,
                   soldier2: Soldier2,
                   shots: Group,
                   aliens: Group,
                   score: Score) -> None:
    """
    Actualiza todos los elementos gráficos en pantalla.

    Args:
        screen: Superficie donde se dibuja
        clock: Controlador de FPS
        background: Fondo del juego
        soldier: Primer jugador
        soldier2: Segundo jugador
        shots: Disparos activos
        aliens: Aliens activos
        score: Marcador de puntos
    """
    # Dibujar fondo
    background.blit(screen)

    # Actualizar y dibujar disparos
    for shot in shots:
        shot.update_position(screen)
        shot.update_animation()
        shot.blit(screen)

    # Actualizar y dibujar aliens
    for alien in aliens:
        alien.update_position(screen)
        alien.update_animation()
        alien.blit(screen)

    # Actualizar y dibujar jugadores
    soldier.update_position(screen)
    soldier.update_animation()
    soldier.blit(screen)

    soldier2.update_position(screen)
    soldier2.update_animation()
    soldier2.blit(screen)

    # Dibujar marcador
    score.draw(screen)

    # Actualizar pantalla completa
    pygame.display.flip()
    clock.tick(Configurations.get_fps())



