import pygame
from pygame.sprite import Sprite
#Atributos de Herencia
class SnakeBlock(Sprite):
    def __init__(self):
        """
        Constructor de la clase.
        """

        super().__init__()

        color = (255, 0, 0)

        self.image = pygame.Surface((40,40))
        self.image.fill(color)  #Rellenar de un color

        self.rect = self.image.get_rect()   # Obteniendo su rectángulo


    def blit(self, screen: pygame.surface.Surface) ->None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        :param self:
        :param scree: Pantalla en donde se dibuja.
        :return:
        """

        screen.blit(self.image, self.rect)

