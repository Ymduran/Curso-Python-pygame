import pygame


from pygame.sprite import Sprite
from Configurations import Configurations
from random import randint


class Apple(Sprite):

    # Atributo de clase para la puntuación.
    _no_apples = 0
    def __init__(self) -> None:
        super().__init__()

        Apple._no_apples += 1

        self.apple_frames = []
        apple_block_size = Configurations.get_apple_size()

        for i in range(len(Configurations.get_apple_images_path())):
            frame = pygame.image.load(Configurations.get_apple_images_path()[i])
            frame = pygame.transform.scale(frame, (apple_block_size,apple_block_size))
            self.apple_frames.append(frame)

        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0


        self.image = self.apple_frames[self._frame_index]
        self._frame_index = 1

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla donde se dibuja.
        :return:
        """
        screen.blit(self.image, self.rect)


    def random_position(self, snake_body: pygame.sprite.Group) -> None:
        """ Se utiliza para inicializar una ubicación aleatoria de la manzana y verificar que no se sobreponga sobre el cuerpo de la serpiente."""
        repeat = True
        while repeat:
            # Se genera la posición aleatoria.
            screen_width = Configurations.get_screen_size()[0]
            screen_height = Configurations.get_screen_size()[1]
            apple_size = Configurations.get_apple_size()

            self.rect.x = apple_size* randint(0, (screen_width // apple_size - 1))
            self.rect.y = apple_size * randint(0, (screen_height // apple_size - 1))
            # Se verifica que no se encuentre sobre el cuerpo de la serpiente.
            for snake_block in snake_body.sprites():
                if self.rect == snake_block.rect:
                    repeat = True
                    break
                else: repeat = False


    def animate_apple(self) -> None :
        """ Se utiliza un mét0do para actualizar manzana dando la impresión de movimiento"""
        current_time = pygame.time.get_ticks()
        time_to_refresh = Configurations.get_time_to_refresh_apple_frames()
        needs_refresh = (current_time - self._last_update_time) >= time_to_refresh
        if needs_refresh:
            self.image = self.apple_frames[self._frame_index]

            self._last_update_time = current_time
            self._frame_index += 1

            if self._frame_index >= len(self.apple_frames): self._frame_index = 0


    @classmethod
    def get_no_apples(cls) -> int:
        """ Getter para _no_apples. """
        return cls._no_apples



