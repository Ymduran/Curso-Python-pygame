

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """

    _screen_size = (1280, 720)   #Resolución de la pantalla (ancho x alto)
    _game_title = "Snake game en pygame" # Título del juego.
    _background = (20, 30, 50) #Fondo de la pantalla en formato rgb
    _fps = 8


    #Configuraciones de la serpiente:
    _snake_block_size = 80          # Tamaño del bloque de la serpiente.
    _snake_head_color = (255, 255, 255) #Color de la cabeza de la serpiente.
    _snake_body_color = (0, 255, 0)

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title.
        """
        return cls._game_title

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_background(cls) -> tuple[int, int, int]:
        """
        Getter para _background.
        """
        return cls._background

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_snake_block_size(cls) -> int:
        """
        Getter para _snake_block_size.
        """
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_head_color.
        """
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_body_color.
        """
        return cls._snake_body_color
