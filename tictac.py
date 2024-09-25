import pygame
import logica_juego
import ganador  # Importamos el archivo ganador.py
import random  # Importamos random para el sorteo


# Inicializamos Pygame
pygame.init()

# Definimos los colores
amarillo = (242, 213, 84)
rojo = (243, 109, 127)
azul = (26, 190, 179)
gris = (53, 57, 66)
blanco = (255, 255, 255)

# Establecemos las dimensiones de la ventana
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Tres en Raya")

def sorteo_inicial():
    return 'X' if random.choice([True, False]) else 'O'  # Elige aleatoriamente entre 'X' y 'O'
# Cargamos la fuente
fuente = pygame.font.Font(None, 50)

def main(modo):
    global modo_juego
    modo_juego = modo

    # Estado inicial del tablero
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

    inicia = sorteo_inicial()  # Llama a la función para determinar quién inicia
    turno_jugador = inicia == 'X'  # True si empieza el jugador 1, False si empieza la IA    # Bucle principal para mantener la ventana abierta
    ejecutando = True
    turno_jugador = inicia == 'X'  # True si empieza el jugador 1, False si empieza la IA

    ancho_rect = 80
    alto_rect = 80
    distancia = 15
    total_ancho = (ancho_rect * 3) + (distancia * 2)
    inicio_x = (ANCHO_PANTALLA - total_ancho) // 2
    inicio_y = (ALTO_PANTALLA - (alto_rect * 3) - (distancia * 2)) // 2
    # Si la IA comienza, hacemos su jugada inicial solo una vez
    if inicia == 'O' and modo_juego != '2vs2':
        movimiento_ia = logica_juego.IA_NORMAL(matriz_letras)
        if movimiento_ia:
            matriz_letras = logica_juego.RESULT(matriz_letras, movimiento_ia, 'O')
            turno_jugador = True  # Cambiar turno al jugador 1 después de la jugada de IA

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            
            ancho_rect = 80
            alto_rect = 80
            distancia = 15

            # Calculamos la posición de los rectángulos
            total_ancho = (ancho_rect * 3) + (distancia * 2)
            inicio_x = (ANCHO_PANTALLA - total_ancho) // 2
            inicio_y = (ALTO_PANTALLA - (alto_rect * 3) - (distancia * 2)) // 2
            
            if modo_juego == '2vs2' or (modo_juego != '2vs2' and turno_jugador):
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    # Obtener posición del clic
                    mouse_x, mouse_y = evento.pos

                    # Verificar si el clic fue en algún cuadrado del tablero
                    for fila in range(3):
                        for col in range(3):
                            rect_x = inicio_x + col * (ancho_rect + distancia)
                            rect_y = inicio_y + fila * (alto_rect + distancia)

                            if rect_x < mouse_x < rect_x + ancho_rect and rect_y < mouse_y < rect_y + alto_rect:
                                # Verificar si la casilla está vacía y si el juego no ha terminado
                                if matriz_letras[fila][col] == 'vacio' and not logica_juego.TERMINAL(matriz_letras):
                                    # Si el modo es 2vs2, siempre colocamos 'X' o 'O' según el turno
                                    jugador = 'X' if turno_jugador else 'O'  # Alternar entre 'X' y 'O'
                                    matriz_letras = logica_juego.RESULT(matriz_letras, (fila, col), jugador)
                                    turno_jugador = not turno_jugador  # Cambiar de turno
                                    
                                    # Verificar si el juego ha terminado
                                    if logica_juego.TERMINAL(matriz_letras):
                                        print(f"Juego terminado, utilidad: {logica_juego.UTILITY(matriz_letras)}")

            # IA juega en su turno
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
                    turno_jugador = not turno_jugador  # Cambiar de turno

                    # Verificar si el juego ha terminado
                    if logica_juego.TERMINAL(matriz_letras):
                        print(f"Juego terminado, utilidad: {logica_juego.UTILITY(matriz_letras)}")
            # Dentro del bucle de eventos, donde verificas si el juego ha terminado
            if logica_juego.TERMINAL(matriz_letras):
                ganador_jugador = 'X' if not turno_jugador else 'O'  # Determinamos quién ganó
                ganador.mostrar_ganador(ganador_jugador)  # Llamamos a mostrar_ganador con el jugador
                    # Rellenamos la ventana de amarillo
        pantalla.fill(amarillo)
        # Determinamos quién es el jugador actual
        jugador_actual = 'X' if turno_jugador else 'O'
        texto_turno = fuente.render(f'Turno de: {jugador_actual}', True, blanco)
        texto_turno_rect = texto_turno.get_rect(center=(ANCHO_PANTALLA // 2, 50))  # Centrado en la parte superior
        pantalla.blit(texto_turno, texto_turno_rect)
        # Dibujamos el tablero de 3x3 con letras y colores
        for fila in range(3):
            for col in range(3):
                rect_x = inicio_x + col * (ancho_rect + distancia)
                rect_y = inicio_y + fila * (alto_rect + distancia)
                color_rect = matriz_colores[fila][col]
                pygame.draw.rect(pantalla, color_rect, (rect_x, rect_y, ancho_rect, alto_rect), border_radius=20)

                # Renderizamos la letra
                letra = matriz_letras[fila][col] if matriz_letras[fila][col] != 'vacio' else ''
                texto = fuente.render(letra, True, blanco)
                texto_rect = texto.get_rect(center=(rect_x + ancho_rect // 2, rect_y + alto_rect // 2))
                pantalla.blit(texto, texto_rect)

        # Actualizamos la pantalla
        pygame.display.flip()

    pygame.quit()
