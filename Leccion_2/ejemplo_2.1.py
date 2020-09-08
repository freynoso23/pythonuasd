# Calculardora de ISR

top01 = 416220.00
top02 = 624329.00
top03 = 867123.00

salario = float(input('Ingrese su sueldo mensul:'))
salarioAnual = salario * 12
isr = 0

if salarioAnual <= top01:
    print('Esta Exenta')
elif salarioAnual <= top02:
    excedente = salarioAnual - top01
    isr = excedente * 0.15
elif salarioAnual <= top03:
    excedente = salarioAnual - top02
    isr = 31216.00 + (excedente * 0.20)     #Ejemplo con el parentesis para denotar que la multiplicacion va primero
else: 
    excedente = salarioAnual - top03
    isr = 79776.00 + excedente * 0.25       #Ejemplo sin el parentisis para denotar que hace lo mismo con o sin el parentisis.

print(isr / 12)