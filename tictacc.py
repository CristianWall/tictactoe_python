import pygame
import logica_juego
import ganador 
import random 


pygame.init()

amarillo = (242, 213, 84)
rojo = (243, 109, 127)
azul = (26, 190, 179)
gris = (53, 57, 66)
blanco = (255, 255, 255)

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Tres en Raya")

def sorteo_inicial():
    return 'X' if random.choice([True, False]) else 'O'  # elige aleatoriamente 
fuente = pygame.font.Font(None, 50)

def main(modo):
    global modo_juego
    modo_juego = modo

    matriz_letras = [
        ['vacio', 'vacio', 'vacio'],
        ['vacio', 'vacio', 'vacio'],
        ['vacio', 'vacio', 'vacio']
    ]

    matriz_colores = [
        [gris, gris, gris],
        [gris, gris, gris],
        [gris, gris, gris]
    ]

    inicia = sorteo_inicial()  
    turno_jugador = inicia == 'X'  
    ejecutando = True
    turno_jugador = inicia == 'X'  

    ancho_rect = 80
    alto_rect = 80
    distancia = 15
    total_ancho = (ancho_rect * 3) + (distancia * 2)
    inicio_x = (ANCHO_PANTALLA - total_ancho) // 2
    inicio_y = (ALTO_PANTALLA - (alto_rect * 3) - (distancia * 2)) // 2
    if inicia == 'O' and modo_juego != '2vs2':
        movimiento_ia = logica_juego.IA_NORMAL(matriz_letras)
        if movimiento_ia:
            matriz_letras = logica_juego.RESULT(matriz_letras, movimiento_ia, 'O')
            turno_jugador = True 

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            
            ancho_rect = 80
            alto_rect = 80
            distancia = 15

            total_ancho = (ancho_rect * 3) + (distancia * 2)
            inicio_x = (ANCHO_PANTALLA - total_ancho) // 2
            inicio_y = (ALTO_PANTALLA - (alto_rect * 3) - (distancia * 2)) // 2
            
            if modo_juego == '2vs2' or (modo_juego != '2vs2' and turno_jugador):
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mouse_x, mouse_y = evento.pos

                    for fila in range(3):
                        for col in range(3):
                            rect_x = inicio_x + col * (ancho_rect + distancia)
                            rect_y = inicio_y + fila * (alto_rect + distancia)

                            if rect_x < mouse_x < rect_x + ancho_rect and rect_y < mouse_y < rect_y + alto_rect:
                                if matriz_letras[fila][col] == 'vacio' and not logica_juego.TERMINAL(matriz_letras):
                                    # según el turno
                                    jugador = 'X' if turno_jugador else 'O' 
                                    matriz_letras = logica_juego.RESULT(matriz_letras, (fila, col), jugador)
                                    turno_jugador = not turno_jugador  # Cambiar de turno
                                    
                                    #  si el juego ha terminado
                                    if logica_juego.TERMINAL(matriz_letras):
                                        print(f"Juego terminado, utilidad: {logica_juego.UTILITY(matriz_letras)}")

            # IA 
            if not turno_jugador and modo_juego != '2vs2':
                if not logica_juego.TERMINAL(matriz_letras):
                    if modo_juego == 'facil':
                        movimiento_ia = logica_juego.IA_FACIL(matriz_letras)
                    elif modo_juego == 'normal':
                        movimiento_ia = logica_juego.IA_NORMAL(matriz_letras)
                    elif modo_juego == 'dificil':
                        movimiento_ia = logica_juego.IA_DIFICIL(matriz_letras)

                    if movimiento_ia:
                        matriz_letras = logica_juego.RESULT(matriz_letras, movimiento_ia, 'O')
                    turno_jugador = not turno_jugador  #  turno

                    if logica_juego.TERMINAL(matriz_letras):
                        print(f"Juego terminado, utilidad: {logica_juego.UTILITY(matriz_letras)}")
            #  juego ha terminado
            if logica_juego.TERMINAL(matriz_letras):
                ganador_jugador = 'X' if not turno_jugador else 'O'
                ganador.mostrar_ganador(ganador_jugador)  
        pantalla.fill(amarillo)
        jugador_actual = 'X' if turno_jugador else 'O'
        texto_turno = fuente.render(f'Turno de: {jugador_actual}', True, blanco)
        texto_turno_rect = texto_turno.get_rect(center=(ANCHO_PANTALLA // 2, 50))  
        pantalla.blit(texto_turno, texto_turno_rect)
        for fila in range(3):
            for col in range(3):
                rect_x = inicio_x + col * (ancho_rect + distancia)
                rect_y = inicio_y + fila * (alto_rect + distancia)
                color_rect = matriz_colores[fila][col]
                pygame.draw.rect(pantalla, color_rect, (rect_x, rect_y, ancho_rect, alto_rect), border_radius=20)

                letra = matriz_letras[fila][col] if matriz_letras[fila][col] != 'vacio' else ''
                texto = fuente.render(letra, True, blanco)
                texto_rect = texto.get_rect(center=(rect_x + ancho_rect // 2, rect_y + alto_rect // 2))
                pantalla.blit(texto, texto_rect)

        pygame.display.flip()

    pygame.quit()
