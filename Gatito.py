def imprimir_tablero(tablero):
    print("\n")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("-----------")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("-----------")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
    print("\n")

def verificar_ganador(tablero, jugador):
    
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  #filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  #columnas
        [0, 4, 8], [2, 4, 6]              #diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == jugador:
            return True
    return False

def juego_gato():

    tablero = [" " for _ in range(9)]
    jugador_actual = "X"
    movimientos = 0

    print("¡Bienvenido al juego del Gato (Tic-Tac-Toe)!")
    print("Instrucciones: Ingresa un número del 1 al 9 para colocar tu marca en el tablero.")
    imprimir_tablero(tablero)

    while True:

        try:
            jugada = int(input(f"Jugador {jugador_actual}, elige una posición (1-9): ")) - 1
            if jugada < 0 or jugada > 8:
                print("Por favor, ingresa un número válido entre 1 y 9.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            continue


        if tablero[jugada] != " ":
            print("Esa posición ya está ocupada. Intenta de nuevo.")
            continue

       
        tablero[jugada] = jugador_actual
        movimientos += 1
        imprimir_tablero(tablero)

       
        if verificar_ganador(tablero, jugador_actual):
            print(f"¡Felicidades! El jugador {jugador_actual} ha ganado.")
            break

       
        if movimientos == 9:
            print("¡Es un empate!")
            break

        
        jugador_actual = "O" if jugador_actual == "X" else "X"

juego_gato()