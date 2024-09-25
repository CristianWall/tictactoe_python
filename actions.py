def ACTIONS(s):
    """
    Devuelve una lista de movimientos legales en el estado dado.
    
    Parámetros:
    s (list of list): Matriz 3x3 que representa el estado del juego.
    
    Retorna:
    list of tuples: Lista de coordenadas (i, j) de las posiciones vacías donde se puede realizar un movimiento.
    """
    movimientos_legales = []
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 'vacio':
                movimientos_legales.append((i, j))
    
    return movimientos_legales

# Ejemplo de uso
estado = [['vacio', 'vacio', 'X'],
          ['vacio', 'vacio', 'O'],
          ['vacio', 'vacio', 'vacio']]

# Determina los movimientos legales
movimientos = ACTIONS(estado)
print(f"Movimientos legales: {movimientos}")
