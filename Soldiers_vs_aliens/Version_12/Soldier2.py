import pygame
from pygame.sprite import Sprite
from Configurations import Configurations


class Soldier2(Sprite):
    """
    Segundo personaje jugable con controles alternativos.
    Hereda funcionalidad básica de Sprite para colisiones.
    Atributos:
        _is_moving_up (bool): Bandera movimiento arriba
        _is_moving_down (bool): Bandera movimiento abajo
        _is_shooting (bool): Bandera estado disparando
        _frames (list): Lista de frames de animación
        image (Surface): Imagen actual del sprite
        rect (Rect): Posición y dimensiones
        _rect_y (float): Posición vertical precisa
        _speed (float): Velocidad de movimiento
        _last_update_time (int): Tiempo último frame
        _frame_index (int): Índice frame actual
    """

    def __init__(self, screen: pygame.Surface):
        """Inicializa el segundo soldado en la derecha de la pantalla"""
        super().__init__()

        # Banderas de estado
        self._is_moving_up = False
        self._is_moving_down = False
        self._is_shooting = False

        # Carga de hoja de sprites
        self._frames = []
        sheet_path = Configurations.get_soldier_sheet_path()
        soldier_sheet = pygame.image.load(sheet_path)

        # Configuración de frames
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_frames_per_column = Configurations.get_frames_per_column()
        sheet_width = soldier_sheet.get_width()
        sheet_height = soldier_sheet.get_height()
        frame_width = sheet_width // sheet_frames_per_row
        frame_height = sheet_height // sheet_frames_per_column

        # Recorte y escalado de frames
        soldier2_size = Configurations.get_soldier2_size()
        for i in range(sheet_frames_per_column):
            for j in range(sheet_frames_per_row):
                x = j * frame_width
                y = i * frame_height
                subsurface_rect = (x, y, frame_width, frame_height)
                frame = soldier_sheet.subsurface(subsurface_rect)
                frame = pygame.transform.scale(frame, soldier2_size)
                self._frames.append(frame)

        # Configuración inicial
        self.image = self._frames[0]
        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right  # Posición derecha
        self.rect.centery = screen_rect.centery

        # Atributos de movimiento
        self._rect_y = float(self.rect.y)
        self._speed = Configurations.get_soldier_speed()
        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0

    def update_position(self, screen: pygame.Surface) -> None:
        """Actualiza posición vertical según las banderas de movimiento"""
        screen_rect = screen.get_rect()

        if self._is_moving_up:
            self._rect_y -= self._speed
        elif self._is_moving_down:
            self._rect_y += self._speed

        # Limitar movimiento a los bordes
        if self._rect_y < screen_rect.top:
            self._rect_y = float(screen_rect.top)
        elif self._rect_y > screen_rect.bottom - self.rect.height:
            self._rect_y = float(screen_rect.bottom - self.rect.height)

        self.rect.y = int(self._rect_y)

    def update_animation(self) -> None:
        """Actualiza el frame de animación según el estado"""
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()

        if (current_time - self._last_update_time) >= frame_delay:
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Lógica de animación para disparo/reposo
            frames_per_row = Configurations.get_frames_per_row()
            if not self._is_shooting and self._frame_index >= frames_per_row:
                self._frame_index = 0
            elif self._is_shooting and self._frame_index >= 2 * frames_per_row:
                self._frame_index = frames_per_row
            elif self._is_shooting and self._frame_index == frames_per_row + 1:
                self._is_shooting = False

    def shoots(self) -> None:
        """Activa el estado de disparo y ajusta la animación"""
        self._is_shooting = True
        self._frame_index = Configurations.get_frames_per_row()
        self._last_update_time = pygame.time.get_ticks()

    def blit(self, screen: pygame.Surface) -> None:
        """Dibuja el sprite en la pantalla"""
        screen.blit(self.image, self.rect)

    # Propiedades (getters/setters)
    @property
    def is_moving_up(self) -> bool:
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self, value: bool) -> None:
        self._is_moving_up = value

    @property
    def is_moving_down(self) -> bool:
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self, value: bool) -> None:
        self._is_moving_down = value

    @property
    def is_shooting(self) -> bool:
        return self._is_shooting

    @is_shooting.setter
    def is_shooting(self, value: bool) -> None:
        self._is_shooting = value