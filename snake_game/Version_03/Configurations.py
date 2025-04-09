

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """

    _screen_size = (1280, 720)   #Resolución de la pantalla (ancho x alto)
    _game_title = "Snake game en pygame" # Título del juego.
    _background = (20, 30, 50) #Fondo de la pantalla en formato rgb


    @classmethod
    def get_screen_size(cls)->tuple[int, int]:
        """
        Getter para _screen_size
        :return:
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls)->str:
        """
        Getter para _game_title
        :return:
        """
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int, int,int]:
        """
        Getter para background
        :return:
        """
        return cls._background

