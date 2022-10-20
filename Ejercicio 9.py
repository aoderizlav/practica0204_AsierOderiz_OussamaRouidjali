filas = int(input("Introduzca el numero del triangulo: \n"))

for fila in range(filas + 1):
    for numeros in range(fila, 0, -1):
        print((numeros * 2 - 1), end="")
    print("")

