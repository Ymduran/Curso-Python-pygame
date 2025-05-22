

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """

    _screen_size = (1280, 720)   #Resolución de la pantalla (ancho x alto)
    _game_title = "Soldier VS Aliens" # Título del juego.
    _background = (20, 30, 50) #Fondo de la pantalla en formato rgb

    _background_image_path = "../media/background.png"

    _soldier_image_path = "../media/soldier.png"
    _soldier_block_size = 80
    _fps = 8


    @classmethod
    def get_screen_size(cls)->tuple[int, int]:
        """
        Getter para _screen_size
        :return:
        """
        return cls._screen_size

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._fps

    @classmethod
    def get_soldier_block_size(cls) -> int:
        """
        Getter para _soldier_block_size
        :return:
        """
        return cls._soldier_block_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title
        :return:
        """
        return cls._game_title

    @classmethod
    def get_soldier_image_path(cls)->str:
        """
        Getter para _soldier_image_path
        :return:
        """
        return cls._soldier_image_path

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path
        :return:
        """
        return cls._background_image_path

    @classmethod
    def get_background(cls) -> tuple[int, int,int]:
        """
        Getter para background
        :return:
        """
        return cls._background

