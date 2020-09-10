# Almacene cuatro notas 90, 95, 77, 92 y las promedie. Al final debe decir su calificacion en letras.
# A, B, C, D, E o F

nota1 = 90
nota2 = 95 
nota3 = 77
nota4 = 92

promedio = (nota1 + nota2 + nota3 + nota4) / 4
# print(promedio)

if promedio > 89:
    print("Su calificacion es A")
elif promedio > 79:
    print("Su calificacion es B")
elif promedio > 69:
    print("Su calificacion es C")
elif promedio > 59:
    print("Su calificacion es D")
elif promedio> 49:
    print("Su calificacion es E")
else:
    print("Su calificacion es F")
    
    