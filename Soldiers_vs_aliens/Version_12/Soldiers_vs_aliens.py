"""
Nombre: Durán Breceda Lourdes Jamileth y Bautista Juárez Juan
Fecha: 23 junio 2025
Versión 12:



"""
from time import sleep
import pygame
from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh, check_collisions
from Media import Background
from Soldier import Soldier
from Soldier2 import Soldier2  # Nuevo import
from Shot import Shot
from Alien import Alien
from GameOverAnimation import GameOverAnimation
from Score import Score
from AudioManager import AudioManager
from random import randint


def run_game() -> None:
    pygame.init()
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())

    # Inicializar sistemas
    clock = pygame.time.Clock()
    background = Background()
    soldier = Soldier(screen)
    soldier2 = Soldier2(screen)  # Nuevo jugador
    shots = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    score = Score()
    audio = AudioManager()
    audio.play_music()

    # Generar aliens iniciales
    for _ in range(Configurations.get_min_aliens() + randint(0, 5)):
        aliens.add(Alien(screen))

    # Bucle principal
    game_over = False
    while not game_over:
        game_over = game_events(soldier, soldier2, shots, audio)

        if not game_over:
            game_over = check_collisions(screen, soldier, soldier2, shots, aliens, score, audio)
            screen_refresh(screen, clock, background, soldier, soldier2, shots, aliens, score)

        if game_over:
            GameOverAnimation(screen).play()
            sleep(1)

    audio.stop_music()
    pygame.quit()


if __name__ == "__main__":
    run_game()