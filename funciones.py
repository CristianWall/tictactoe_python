
def PLAYER(s):

    # contar x y o
    count_X = sum(row.count('X') for row in s)
    count_O = sum(row.count('O') for row in s)
    
    # a quien le toca jugar
    if count_X < count_O:
        return 'X'
    else:
        return 'O'

# ejepmplo
S0 = [['vacio', 'vacio', 'X'],
      ['vacio', 'vacio', 'O'],
      ['vacio', 'vacio', 'vacio']]

# imprimir a quien le toca
turno = PLAYER(S0)
print(f"Es el turno de: {turno}")


def ACTIONS(s):

    movimientos_legales = []
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 'vacio':
                movimientos_legales.append((i, j))
    
    return movimientos_legales

# estado
estado = [['vacio', 'vacio', 'X'],
          ['vacio', 'vacio', 'O'],
          ['vacio', 'vacio', 'vacio']]

# imprime los moviemitnos posibles
movimientos = ACTIONS(estado)
print(f"Movimientos legales: {movimientos}")

def RESULT(s, a, jugador):
    
    # reempla estado
    nuevo_estado = [row.copy() for row in s]
    
    i, j = a
    
    if nuevo_estado[i][j] == 'vacio':
        nuevo_estado[i][j] = jugador
    
    return nuevo_estado

# ejemplo
estado = [['vacio', 'vacio', 'X'],
          ['vacio', 'vacio', 'O'],
          ['vacio', 'vacio', 'vacio']]

# accion
accion = (1, 0)
jugador = 'X'

# determinar nuevo estado
nuevo_estado = RESULT(estado, accion, jugador)
print("Estado después de la acción:")
for fila in nuevo_estado:
    print(fila)


def TERMINAL(s):

    def verificar_victoria(s, jugador):
        # filas, columans y diagonales
        for i in range(3):
            if all(s[i][j] == jugador for j in range(3)) or  all(s[j][i] == jugador for j in range(3)):
                return True
        
        if all(s[i][i] == jugador for i in range(3)) or all(s[i][2 - i] == jugador for i in range(3)):
            return True
        
        return False
    
    # quien gana
    for jugador in ['X', 'O']:
        if verificar_victoria(s, jugador):
            return True
    
    # hay mas moviemitnos o no
    if all(cell != 'vacio' for row in s for cell in row):
        return True
    
    return False

# ejmplo
estado1 = [['X', 'O', 'X'],
           ['X', 'O', 'O'],
           ['O', 'X', 'X']]  # empate

estado2 = [['X', 'O', 'X'],
           ['O', 'X', 'O'],
           ['O', 'X', 'vacio']]  # posbule


estado3 = [['X', 'O', 'X'],
           ['X', 'X', 'O'],
           ['O', 'X', 'O']]  # lleno

print(f"Estado1 es terminal: {TERMINAL(estado1)}")
print(f"Estado2 es terminal: {TERMINAL(estado2)}")
print(f"Estado4 es terminal: {TERMINAL(estado3)}")



def UTILITY(s):
    
    def verificar_victoria(s, jugador):
        # Verificar filas, columnas y diagonales para una victoria
        for i in range(3):
            if all(s[i][j] == jugador for j in range(3)) or  all(s[j][i] == jugador for j in range(3)):
                return True
        
        if all(s[i][i] == jugador for i in range(3)) or all(s[i][2 - i] == jugador for i in range(3)):
            return True
        
        return False
    
    # gana x
    if verificar_victoria(s, 'X'):
        return 1
    
    # gana o
    if verificar_victoria(s, 'O'):
        return -1
    
    # empate
    return 0

# ejemplo
estado1 = [['X', 'O', 'X'],
           ['X', 'O', 'O'],
           ['O', 'X', 'X']]  # empate

estado2 = [['X', 'O', 'X'],
           ['O', 'X', 'O'],
           ['O', 'X', 'vacio']]  # no gano nadie aun

estado3 = [['X', 'X', 'X'],
           ['O', 'O', 'O'],
           ['vacio', 'vacio', 'vacio']]  # X ha ganado

estado4 = [['X', 'vacio', 'O'],
           ['X', 'X', 'O'],
           ['O', 'X', 'O']]  # O ha ganado

print(f"Estado1: {UTILITY(estado1)}")  
print(f"Estado2: {UTILITY(estado2)}")  
print(f"Estado3: {UTILITY(estado3)}")  
print(f"Estado4: {UTILITY(estado4)}")  
