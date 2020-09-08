# # while 
c = 1
while c < 10:
    print(c)
    c = c + 1
print('El blucle ha finalizado')

# # Para ver los numeros pares usando un while.
c = 1
while c < 10:
    if c % 2 == 0:
        print(c)
    c = c + 1
print('El blucle ha finalizado')

# # Hacer una calculadora para ingresar numeros por teclado.
n = input('Ingres un numero para ver su tabla:')
x = 1

while x <= 12:
     print(int(n) * x)
     x += 1  # += trae el valor de n (esto seria lo mismo que hacer c = c + 1)

# # Hacer una calculadora para ingresar numeros por teclado, pero mas bonita
 n = input('Ingres un numero para ver su tabla:')
 c = 1

while c <= 12:
    resultado = (int(n) * c)
    print(f'{n} X {c} = {resultado}')
    c += 1  

########### For ###########

for c in range(10):
    print(c + 1)