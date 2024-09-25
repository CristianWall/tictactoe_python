import pygame
import sys
from config import Nombres

def mostrar_ganador(jugador):
    pygame.init()

    # dimensiones de la ventana
    ANCHO_PANTALLA = 800
    ALTO_PANTALLA = 600
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Ganador")

    # cargar fuente
    fuente = pygame.font.Font(None, 50)

    mensaje = "GANADOR"
    texto_jugador = Nombres.jugador_x if jugador == "X" else Nombres.jugador_o
    texto_ganador = f"{jugador}: {texto_jugador} es el ganador!"

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            # verificar si se hace clic en el boton "volver"
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mouse_x, mouse_y = evento.pos
                if ANCHO_PANTALLA // 2 - 50 <= mouse_x <= ANCHO_PANTALLA // 2 + 50 and ALTO_PANTALLA - 60 <= mouse_y <= ALTO_PANTALLA - 10:
                    import inicio  
                    inicio.main()
                    pygame.quit()
                    return

        # rellenar pantalla de amarillo
        pantalla.fill((242, 213, 84))

        # renderizar mensajes
        texto_mensaje = fuente.render(mensaje, True, (255, 255, 255))
        texto_rect = texto_mensaje.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 - 20))
        pantalla.blit(texto_mensaje, texto_rect)

        texto_ganador_render = fuente.render(texto_ganador, True, (255, 255, 255))
        texto_rect_jugador = texto_ganador_render.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 + 20))
        pantalla.blit(texto_ganador_render, texto_rect_jugador)

        # dibujar boton "volver"
        rojo = (243, 109, 127)
        blanco = (255, 255, 255)
        pygame.draw.rect(pantalla, rojo, (ANCHO_PANTALLA // 2 - 50, ALTO_PANTALLA - 60, 100, 50), border_radius=10)
        texto_volver = fuente.render("Volver", True, blanco)
        pantalla.blit(texto_volver, (ANCHO_PANTALLA // 2 - 40, ALTO_PANTALLA - 50))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    ganador = "X"
    mostrar_ganador(ganador)
