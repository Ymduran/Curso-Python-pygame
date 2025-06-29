class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Soldados vs aliens"              # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    _fps = 30                                       # Número máximo de FPS del videojuego.

    # Configuraciones del soldado.
    _soldier_size = (140, 80)                       # Escala del soldado (ancho, alto).

    _frames_per_row = 4                             # Número de frames que contiene cada fila de la hoja de frames.
    _soldier_frame_delay = 100                      # Tiempo de cada frame del personaje (en ms).
    _soldier_speed = 12.5                           # Velocidad (en píxeles) del personaje.


    _frames_per_column = 2

    # Rutas de las imágenes utilizadas.
    _background_image_path = "../media/background.png"
    _soldier_sheet_path = "../media/soldier-idle_shooting_sheet.png"

    _shot_sheet_path = "../media/shot-sheet.png"
    _shot_size = (32,32)
    _shot_speed = 12.5





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
    def get_shot_size(cls) -> tuple[int, int]:
        """
        Getter para _shot_size
        """
        return cls._shot_size

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_soldier_size(cls) -> tuple[int, int]:
        """
        Getter para _soldier_size.
        """
        return cls._soldier_size




    @classmethod
    def get_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._frames_per_row

    @classmethod
    def get_frames_per_column(cls) -> int:
        """
        Getter para _soldier_frames_per_column.
        """
        return cls._frames_per_column


    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay


    @classmethod
    def get_soldier_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._soldier_speed

    @classmethod
    def get_shot_speed(cls) -> float:
        """
        Getter para _shot_speed.
        """
        return cls._shot_speed

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path


    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path

    @classmethod
    def get_shot_sheet_path(cls) -> str:
        """
        Getter para _shot_sheet_path.
        """
        return cls._shot_sheet_path