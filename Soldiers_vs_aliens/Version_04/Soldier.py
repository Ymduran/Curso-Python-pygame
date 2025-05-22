import pygame

from pygame.sprite import Sprite
from Configurations import Configurations


class Soldier(Sprite):
    def __init__(self, screen):

       super().__init__()
       soldier_image_path = Configurations.get_soldier_image_path()
       self.image= pygame.image.load(soldier_image_path)

       soldier_block_size = Configurations.get_soldier_block_size()
       self.image = pygame.transform.scale(self.image,[soldier_block_size, soldier_block_size])
       self.rect = self.image.get_rect()

       self._is_movig_up = False
       self._is_moving_down = False


    def update_position(self):
        if (self._is_moving_up): self.rect.y -= 10
        if (self._is_moving_down): self.rect.y += 10


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """

        screen.blit(self.image, self.rect)

    def soldier_init(self, screen) -> None:
        screen_rect = screen.get_rect()
        self.rect.center = screen_rect.center
        self.rect.right = screen_rect.right



    @property
    def is_moving_up(self):
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self, movingup: bool):
        self._is_moving_up = movingup




    @property
    def is_moving_down(self):
        return self._is_moving_down

    @is_moving_up.setter
    def is_moving_up(self, movingdown: bool):
        self._is_moving_down = movingdown
