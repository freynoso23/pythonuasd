# Condicional
# # Operacion par o impar.
# numero = 14
# if numero % 2 == 0:
#     print('Par')

# print('Gracias por usar mi programa')

# Ejemplo if
edad = input('Ingrese su edad:')
# edad = int(edad) # Convertimos el dato edad que es un string a intero para poder hacer la comparacion.
# # if int(edad) >= 18: Otra manera de convertir el dato edad a entero
 if edad >= 18:
    print('Usted es mayor de edad')
    print('Usted no es mayor de edad')

# Login ejemplo if : else

usuario = input('Ingrese su usuario:')
if usuario == 'admin':
    print('Acceso Correcto')
else:
    print('El Usuario es Incorrecto')

#dia = 4
dia = input('Ingrese el dia:')
if int(dia) == 1:
    print('Lunes')
elif int(dia) == 2:
    print('Martes')
elif int(dia) == 3:
    print('Miercoles') 
elif int(dia) == 4:
    print('Jueves') 
elif int(dia) == 5:
    print('Viernes')
else:
    print('Es fin de semana')

