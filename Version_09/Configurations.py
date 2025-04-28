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
    _snake_block_size = 30                          # Tamaño del bloque. Es muy recomendable que sea
                                                    # divisor común del largo y ancho de _screen_size.
    _snake_head_color = (255, 255, 255)             # Color de la cabeza de la serpiente.
    _snake_body_color = (160, 32, 240)                 # Color del cuerpo de la serpiente.

    # Configuraciones de la manzana.
    _apple_color = (255, 0, 0)                      #Color de la manzana en formato RGB.
    _apple_size = _snake_block_size                 # Tamaño de la manzana.

    # Rutas de Archivos multimedia.
    _backgrounds_image_path = "../snake_game/media/background_image.png"
    _apple_image_path = "../snake_game/media/apple1.png"
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
    def get_backgrounds_image_path(cls) -> str:
        """ Getter para _"""
        return cls._backgrounds_image_path

    @classmethod
    def get_apple_image_path(cls) -> str:
        """ Getter para _"""
        return cls._apple_image_path
