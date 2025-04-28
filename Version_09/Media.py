import pygame
from Configurations import Configurations



class Background:
    """ Clase que contiene el fondo de pantalla. """
    def __init__(self):
        self.image = pygame.image.load(Configurations.get_backgrounds_image_path())

        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()




    def blit(self, screen: pygame.surface.Surface):
        """ Se utiliza para dibujar el fondo de pantalla. """
        screen.blit(self.image, self.rect)

class Apple:
    """ Clase que contiene la manzana. """
    def __init__(self):
        self.image = pygame.image.load(Configurations.get_apple_image_path())
        self.rect = self.image.get_rect()