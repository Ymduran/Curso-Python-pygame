import pygame

from pygame.sprite import Sprite
from Configurations import Configurations
from random import randint


class Apple(Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.Surface((Configurations.get_apple_size(), Configurations.get_apple_size()))
        self.image.fill(color = Configurations.get_apple_color())

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla donde se dibuja.
        :return:
        """
        screen.blit(self.image, self.rect)


    def random_position(self) -> None:
        """ Se utiliza para inicializar una ubicación aleatoria de la manzana."""

        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        apple_size = Configurations.get_apple_size()
        self.rect.x = apple_size* randint(0, (screen_width // apple_size - 1))
        self.rect.y = apple_size * randint(0, (screen_height // apple_size - 1))



