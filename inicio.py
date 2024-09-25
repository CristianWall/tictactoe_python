import pygame
import opciones  
import config

pygame.init()

pygame.mixer.music.load("musica2.mp3")
pygame.mixer.music.play(-1) 

amarillo = (242, 213, 84)
rojo = (243, 109, 127)
azul = (26, 190, 179)
gris = (53, 57, 66)
blanco = (255, 255, 255)

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 700
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Tres en Raya")

fuente = pygame.font.Font(None, 50)

global input_active_x, input_active_o
nombre_x = ""
nombre_o = ""
input_active_x = False
input_active_o = False

matriz_letras = [
    ['T', 'I', 'C'],
    ['T', 'A', 'C'],
    ['T', 'O', 'E']
]

matriz_colores = [
    [azul, rojo, gris],
    [rojo, gris, azul],
    [azul, rojo, gris]
]

def guardar_nombres():
    config.Nombres.jugador_x = nombre_x
    config.Nombres.jugador_o = nombre_o

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if boton_x <= mouse_x <= boton_x + 200 and boton_y <= mouse_y <= boton_y + 50:
                guardar_nombres()
                opciones.main()

            if guardar_x <= mouse_x <= guardar_x + 200 and guardar_y <= mouse_y <= guardar_y + 50:
                guardar_nombres()
                print(f"Jugador X: {nombre_x}, Jugador O: {nombre_o}")

            if input_x_rect.collidepoint(mouse_x, mouse_y):
                input_active_x = not input_active_x
                input_active_o = False

            if input_o_rect.collidepoint(mouse_x, mouse_y):
                input_active_o = not input_active_o
                input_active_x = False

        if evento.type == pygame.KEYDOWN:
            if input_active_x:
                if evento.key == pygame.K_BACKSPACE:
                    nombre_x = nombre_x[:-1]
                elif len(nombre_x) < 10:
                    nombre_x += evento.unicode
            elif input_active_o:
                if evento.key == pygame.K_BACKSPACE:
                    nombre_o = nombre_o[:-1]
                elif len(nombre_o) < 10:
                    nombre_o += evento.unicode

    pantalla.fill(amarillo)

    ancho_rect = 80
    alto_rect = 80
    distancia = 15
    total_ancho = (ancho_rect * 3) + (distancia * 2)
    inicio_x = (ANCHO_PANTALLA - total_ancho) // 2
    inicio_y = (ALTO_PANTALLA - (alto_rect * 3) - (distancia * 2)) // 5

    for fila in range(3):
        for col in range(3):
            rect_x = inicio_x + col * (ancho_rect + distancia)
            rect_y = inicio_y + fila * (alto_rect + distancia)
            color_rect = matriz_colores[fila][col]
            pygame.draw.rect(pantalla, color_rect, (rect_x, rect_y, ancho_rect, alto_rect), border_radius=20)

            letra = matriz_letras[fila][col]
            texto = fuente.render(letra, True, blanco)
            texto_rect = texto.get_rect(center=(rect_x + ancho_rect // 2, rect_y + alto_rect // 2))
            pantalla.blit(texto, texto_rect)

    boton_x = (ANCHO_PANTALLA - 200) // 2
    boton_y = inicio_y + (alto_rect * 3) + (distancia * 2) + 20
    pygame.draw.rect(pantalla, gris, (boton_x, boton_y, 200, 50), border_radius=20)
    texto_boton = fuente.render("Empezar", True, blanco)
    texto_boton_rect = texto_boton.get_rect(center=(boton_x + 100, boton_y + 25))
    pantalla.blit(texto_boton, texto_boton_rect)

    guardar_x = (ANCHO_PANTALLA - 200) // 2
    guardar_y = boton_y + 70
    pygame.draw.rect(pantalla, gris, (guardar_x, guardar_y, 200, 50), border_radius=20)
    texto_guardar = fuente.render("Guardar", True, blanco)
    texto_guardar_rect = texto_guardar.get_rect(center=(guardar_x + 100, guardar_y + 25))
    pantalla.blit(texto_guardar, texto_guardar_rect)

    input_x_rect = pygame.Rect(guardar_x, guardar_y + 70, 200, 50)
    pygame.draw.rect(pantalla, gris, input_x_rect, border_radius=10)
    texto_input_x = fuente.render(nombre_x, True, blanco)
    pantalla.blit(texto_input_x, (guardar_x + 10, guardar_y + 80))

    input_o_rect = pygame.Rect(guardar_x, guardar_y + 130, 200, 50)
    pygame.draw.rect(pantalla, gris, input_o_rect, border_radius=10)
    texto_input_o = fuente.render(nombre_o, True, blanco)
    pantalla.blit(texto_input_o, (guardar_x + 10, guardar_y + 140))

    etiqueta_x = fuente.render("Jugador X:", True, blanco)
    pantalla.blit(etiqueta_x, (guardar_x - 200, guardar_y + 80))
    etiqueta_o = fuente.render("Jugador O:", True, blanco)
    pantalla.blit(etiqueta_o, (guardar_x - 200, guardar_y + 140))

    pygame.display.flip()

pygame.quit()
