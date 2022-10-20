password_real = "asier"
password_intr = input("Introduzca su contraseña:\n ")

if password_real == password_intr.lower():
    print("Contraseña Correcta")
else:
    print("Contraseña incorrecta")
