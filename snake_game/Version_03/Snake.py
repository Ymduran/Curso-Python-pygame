import pygame
#from pexpect.screen import screen
from pygame.sprite import Sprite
from Configurations import Configurations
from random import randint


#Atributos de Herencia
class SnakeBlock(Sprite):
    def __init__(self, is_head: bool):
        """
        Constructor de la clase.
        """

        super().__init__()

        if is_head:
            color = Configurations.get_snake_head_color()
        else:
            color = Configurations.get_snake_body_color()

        snake_block_size = Configurations.get_snake_block_size()
        self.image = pygame.Surface((snake_block_size, snake_block_size))
        self.image.fill(color)  #Rellenar de un color

        self.rect = self.image.get_rect()   # Obteniendo su rectángulo


    def blit(self, screen: pygame.surface.Surface) ->None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        :param self:
        :param screen: Pantalla en donde se dibuja.
        :return:
        """
        screen.blit(self.image, self.rect)

    def snake_head_init(self)->None:
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        snake_block_size = Configurations.get_snake_block_size()

        self.rect.x = snake_block_size * randint(0, (screen_width // snake_block_size -1))
        self.rect.y = snake_block_size * randint(0, (screen_height // snake_block_size -1))


