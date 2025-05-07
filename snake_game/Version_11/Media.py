import pygame
from Configurations import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla.
    Sus atributos son: image (apariencia) y rect (posición y tamaño).
    Sus métodos son: blit() (dibujar).
    """
    def __init__(self):
        # Se carga la imagen del fondo de pantalla.
        self.image = pygame.image.load(Configurations.get_backgrounds_image_path())

        # Se escala la imagen al tamaño de la pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el fondo de pantalla en la pantalla.
        :param screen: Pantalla en donde se dibuja el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)



class Audio:
    """
    Clase que contiene el audio del videojuego, incluyendo la música y los efectos de sonido.
    Sus atributos son: la música y los sonidos.
    Sus métodos son: para reproducir y controlar la música, así como los que reproducen los sonidos.
    """
    def __init__(self):
        # Se carga la música del videojuego.
        pygame.mixer.music.load(Configurations.get_music_path())

        # Se carga el sonido de inicio.
        self._start_sound = pygame.mixer.Sound(Configurations.get_start_sound_path())

        # Se carga el sonido cuando la serpiente come una manzana.
        self._eats_apple_sound = pygame.mixer.Sound(Configurations.get_eats_apple_sound_path())

        # Se carga el sonido cuando el jugador ha perdido.
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())


    @classmethod
    def play_music(cls, volume) -> None:
        """ Se utiliza para reproducir la música en bucle. """
        pygame.mixer.music.play(loops=-1)   # Un -1 indica que la música se reproduce en bucle.
        pygame.mixer.music.set_volume(volume)


    @classmethod
    def music_fadeout(cls, time) -> None:
        """
        Se utiliza para realizar un desvanecimiento de la música del juego hasta parar.
        :param time: Tiempo de desvanecimiento de la música (en ms).
        """
        pygame.mixer.music.fadeout(time)


    def play_star_sound(self) -> None:
        """ Se utiliza para reproducir el sonido de inicio del juego. """
        self._start_sound.play()


    def play_eats_apple_sound(self) -> None:
        """ Se utiliza para reproducir el sonido cuando la serpiente come la manzana. """
        self._eats_apple_sound.play()


    def play_game_over_sound(self) -> None:
        """ Se utiliza para reproducir el sonido cuando el jugador ha perdido. """
        self._game_over_sound.play()
