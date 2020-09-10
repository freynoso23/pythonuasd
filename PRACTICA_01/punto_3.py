# Evalúe si un número es par o impar y muerstre en la consola el mensaje.
numeroIngresado = (input("Ingrese el numero:"))
if int(numeroIngresado) % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')