#Que almacene monto, cantidad de cuotas y porcentaje de interes anual de un prestamo y calcule las cuotas mensuales.
capitalPrestado = 20000
cuotas = 12
tipoInteres = 10

fi_1 = 1 + tipoInteres ** cuotas
fi_2 = tipoInteres * fi_1 / fi_1 - 1
res = float(capitalPrestado) * fi_2
print(res)