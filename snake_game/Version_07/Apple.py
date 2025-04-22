import pygame
from pygame.sprite import Sprite
from Configurations import Configurations


class Apple(Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((Configurations.get_apple_size()))
        self.image.fill((Configurations.get_apple_color()))

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla donde se dibuja.
        :return:
        """
        screen.blit(self.image, self.rect)

