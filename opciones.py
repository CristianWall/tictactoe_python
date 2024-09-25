import pygame
import tictac
from config import Nombres

pygame.init()

# definir colores
rojo = (243, 109, 127)
azul = (26, 190, 179)
verde = (106, 190, 48)
amarillo = (242, 213, 84)
blanco = (255, 255, 255)

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Opciones")

fuente = pygame.font.Font(None, 50)

def main():
    global modo_juego

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if 10 <= mouse_x <= 110 and 10 <= mouse_y <= 60:
                    ejecutando = False

                botones = [
                    ((ANCHO_PANTALLA - 300) // 2, 150, "2vs2"),
                    ((ANCHO_PANTALLA - 300) // 2, 250, "facil"),
                    ((ANCHO_PANTALLA - 300) // 2, 350, "normal"),
                    ((ANCHO_PANTALLA - 300) // 2, 450, "dificil")
                ]

                for boton_x, boton_y, texto in botones:
                    if boton_x <= mouse_x <= boton_x + 300 and boton_y <= mouse_y <= boton_y + 80:
                        modo_juego = texto.lower()
                        if modo_juego != "2vs2":
                            Nombres.jugador_o = "IA"
                        tictac.main(modo_juego)
                        ejecutando = False

        pantalla.fill(blanco)

        pygame.draw.rect(pantalla, rojo, (10, 10, 100, 50), border_radius=10)
        texto_volver = fuente.render("Volver", True, blanco)
        pantalla.blit(texto_volver, (20, 15))

        botones = [
            ("2vs2", azul),
            ("IA - Fácil", verde),
            ("IA - Normal", amarillo),
            ("IA - Difícil", rojo)
        ]

        for i, (texto, color) in enumerate(botones):
            boton_x = (ANCHO_PANTALLA - 300) // 2
            boton_y = 150 + i * 100
            pygame.draw.rect(pantalla, color, (boton_x, boton_y, 300, 80), border_radius=10)
            texto_boton = fuente.render(texto, True, blanco)
            pantalla.blit(texto_boton, (boton_x + 100, boton_y + 25))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
