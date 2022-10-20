edad = int(input("introduzca su edad: \n"))
ingresos = int(input("introduzca sus ingresos: \n"))

if edad > 16:
   if ingresos > 1000:
    print('Si puede tributar')
else:
    print('No puede tributar')
