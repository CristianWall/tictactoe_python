import random

def IA_FACIL(s):
    movimientos_legales = ACTIONS(s)
    return random.choice(movimientos_legales) if movimientos_legales else None

def IA_NORMAL(s):
    movimientos_legales = ACTIONS(s)

    for mov in movimientos_legales:
        nuevo_estado = RESULT(s, mov, 'O')
        if TERMINAL(nuevo_estado):
            return mov  

    for mov in movimientos_legales:
        nuevo_estado = RESULT(s, mov, 'X')
        if TERMINAL(nuevo_estado):
            return mov  

    return random.choice(movimientos_legales) if movimientos_legales else None


def IA_DIFICIL(s):
    def minimax(s, es_maximizador):
        if TERMINAL(s):
            return UTILITY(s)

        if es_maximizador:
            mejor_valor = -float('inf')
            for mov in ACTIONS(s):
                valor = minimax(RESULT(s, mov, 'X'), False)
                mejor_valor = max(mejor_valor, valor)
            return mejor_valor
        else:
            mejor_valor = float('inf')
            for mov in ACTIONS(s):
                valor = minimax(RESULT(s, mov, 'O'), True)
                mejor_valor = min(mejor_valor, valor)
            return mejor_valor

    for mov in ACTIONS(s):
        if TERMINAL(RESULT(s, mov, 'X')):
            return mov 

    mejor_movimiento = None
    mejor_valor = -float('inf')

    for mov in ACTIONS(s):
        nuevo_estado = RESULT(s, mov, 'O')
        valor = minimax(nuevo_estado, True)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = mov

    return mejor_movimiento



def PLAYER(s):
    count_X = sum(row.count('X') for row in s)
    count_O = sum(row.count('O') for row in s)
    
    if count_X <= count_O:
        return 'X'
    else:
        return 'O'


def ACTIONS(s):
    movimientos_legales = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 'vacio':
                movimientos_legales.append((i, j))
    return movimientos_legales


def RESULT(s, a, jugador):
    nuevo_estado = [row.copy() for row in s]
    
    i, j = a
    if nuevo_estado[i][j] == 'vacio':
        nuevo_estado[i][j] = jugador
    
    return nuevo_estado


def TERMINAL(s):
    def verificar_victoria(s, jugador):
        for i in range(3):
            if all(s[i][j] == jugador for j in range(3)) or  all(s[j][i] == jugador for j in range(3)):
                return True
        if all(s[i][i] == jugador for i in range(3)) or all(s[i][2 - i] == jugador for i in range(3)):
            return True
        return False

    for jugador in ['X', 'O']:
        if verificar_victoria(s, jugador):
            return True
    
    if all(cell != 'vacio' for row in s for cell in row):
        return True
    
    return False


def UTILITY(s):
    def verificar_victoria(s, jugador):
        for i in range(3):
            if all(s[i][j] == jugador for j in range(3)) or  all(s[j][i] == jugador for j in range(3)):
                return True
        if all(s[i][i] == jugador for i in range(3)) or all(s[i][2 - i] == jugador for i in range(3)):
            return True
        return False

    if verificar_victoria(s, 'X'):
        return 1
    
    if verificar_victoria(s, 'O'):
        return -1
    
    return 0
