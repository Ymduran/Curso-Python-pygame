"""
Nombre:
Fehca:
Versión 0.1:
    - Se crea la pantalla de inicio.
    - Se configura el título de la pantalla.
"""

#Se importan los módulos
import pygame




def run_game()->None:
    """
    Función principal del videojuego.
    :return:
    """
    # Se incia el módulo pygame.
    pygame.init()

    # Se inicaliza la pantalla.
    #screen_size = (1280, 720)   #Resolución de la pantalla (ancho x alto)
    screen = pygame.display.set_mode(Configuration.get_screen_size)

    # Se configura el título del juego.
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configuration.get_game_title)

    #Ciclo principal del videojuego.
    game_over = False

    while not game_over:
        # Se verifican los eventos (teclado y ratón) del juego.
        for event in pygame.event.get():
            print(event)
            # Clic en cerrar el juego.
            if event.type == pygame.QUIT:
                game_over = True

        # Se dibujan los elementos gráficos.
        #background = (20, 30, 50)   # Fondo de la pantalla en formato rgb.
        screen.fill(Configuration.get_background())

        # Se actualiza la pantalla.
        pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
    run_game()