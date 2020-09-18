# python

def potencia(x, y):
    return x**y

potencia(2,3)


def letras():
    number = int(input("Ingrese un numero del 1 al 10"))
    if number==1:
        print("uno")
    elif number==2:
        print("dos")
    elif number==3:
        print("tres")
    elif number==4:
        print("cuatro")
    elif number==5:
        print("cinco")
    elif number==6:
        print("seis")
    elif number==7:
        print("siete")
    elif number==8:
        print("ocho")
    elif number==9:
        print("nueve")
    elif number==10:
        print("diez")
    else:
        print("Numero fuera de rango")


letras()


def esBisiesto(x):
    if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
        return "Verdadero"
    else:
        return "Falso"


esBisiesto(2020)

def iguales(a,b):
    if a==b:
        return "Verdadero"
    else:
        return "Falso"


iguales(12,12)

def palindromo3():
    res = 0
    for x in range(1,1000):
        for y in range(1,1000):
            p = x*y
            if p==int(str(p)[::-1]):
                if p>res:
                    res=p
    return res

palindromo3()


def cedula(x):
    if type(x)==int and len(str(x))==11:
        return "Es valida"
    else:
        return "No es valida"

cedula(45612385466)

def duplex(lista):
    res = []
    for num in lista:
        res.append(num)
        res.append(num)
    return res

duplex([1,2,6,7])


def tablas(x,y):
    for i in range(x,y+1):
        if i%6==0:
            print("Table {}".format(i))
            for k in range(1,11):
                print("{} x {} = {}".format(i,k,i*k))
            print("")


tablas(6,12)