from random import choice
class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Snake game en pygame"            # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    _fps = 8                                        # Número máximo de FPS del videojuego.
    _game_over_screen_time = 1                      # Núm de segundos de pantalla.


    # Configuraciones de la serpiente.
    _snake_block_size = 50                         # Tamaño del bloque. Es muy recomendable que sea
                                                    # divisor común del largo y ancho de _screen_size.
    _snake_head_color = (255, 255, 255)             # Color de la cabeza de la serpiente.
    _snake_body_color = (160, 32, 240)                 # Color del cuerpo de la serpiente.

    # Configuraciones de la manzana.
    _apple_color = (255, 0, 0)                      #Color de la manzana en formato RGB.
    _apple_size = _snake_block_size                 # Tamaño de la manzana.
    _time_to_refresh_apple_frames = 200

    # Rutas de Archivos multimedia.
    _backgrounds_image_path = "../media/background_image.png"
    _apple_images_path = ["../media/media_snake_game/apple1.png",
                            "../media/media_snake_game/apple2.png",
                            "../media/media_snake_game/apple3.png",
                            "../media/media_snake_game/apple4.png"]

    _snake_body_path = ["../media/body3.png" , "../media/img_2.png"]

    _snake_heads_path = ["../media/media_snake_game/head1.png",
                         "../media/media_snake_game/head2.png",
                         "../media/media_snake_game/head3.png"]




    @classmethod
    def get_game_title(cls) -> str:
        """ Getter para _game_title. """
        return cls._game_title

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """ Getter para _screen_size. """
        return cls._screen_size


    @classmethod
    def get_fps(cls) -> int:
        """ Getter para _fps. """
        return cls._fps

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """ Getter para _game_over_screen_time. """
        return cls._game_over_screen_time

    @classmethod
    def get_snake_block_size(cls) -> int:
        """ Getter para _snake_block_size. """
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int, int]:
        """ Getter para _snake_head_color. """
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        """ Getter para _snake_body_color. """
        return cls._snake_body_color

    @classmethod
    def get_apple_color(cls) -> tuple[int, int, int]:
        """ Getter para _apple_color. """
        return cls._apple_color


    @classmethod
    def get_apple_size(cls) -> int:
        """ Getter para _apple_size. """
        return cls._apple_size

    @classmethod
    def get_time_to_refresh_apple_frames (cls) -> int:
        """ Getter para _time_to_refresh_apple_frames . """
        return cls._time_to_refresh_apple_frames

    @classmethod
    def get_backgrounds_image_path(cls) -> str:
        """ Getter para _"""
        return cls._backgrounds_image_path

    @classmethod
    def get_apple_images_path(cls) -> list:
        """ Getter para _"""
        return cls._apple_images_path

    @classmethod
    def get_snake_body_image_path(cls) -> list:
        """ Getter para get_snake_body_image_path"""
        return cls._snake_body_path

    @classmethod
    def get_snake_heads_path(cls) -> list:
        """ Getter para get_snake_head_path"""
        return cls._snake_heads_path
