
import sqlite3

con = sqlite3.connect("contactos.pf")
cursor = con.cursor()
query0 = """
CREATE TABLE  contactos(contactoid integer primary key autoincrement, nombrecontacto text, numerocontacto integer, correocontacto text); """

query2 = """ SELECT * FROM contactos; """
def insertar (nombrecontacto,numerocontacto,correocontacto):
   query1 = """ INSERT INTO contactos(nombrecontacto, numerocontacto, correocontacto) VALUES (?,?,?); """
   info_tupla = (nombrecontacto,numerocontacto,correocontacto)
   cursor.execute(query1, info_tupla)
   con.commit()
   print("Datos Guardados")
   
def busquedanombre(nombrecontacto):
    query3 = """ SELECT *  FROM contactos WHERE nombrecontacto = ? """
    cursor.execute(query3, (nombrecontacto,))
    res = cursor.fetchall()
    print(res)

def busquedaid(contactoid):
    query4 = """ SELECT * FROM contactos WHERE contactoid = ? """
    cursor.execute(query4, (contactoid,))
    res = cursor.fetchall()
    print(res)

def actualizarcontacto(nombrecontacto,numerocontacto,correocontacto,contactoid):
   query6 = """ UPDATE  contactos SET nombrecontacto = ?, numerocontacto = ?, correocontacto = ? where contactoid = ?; """
   cursor.execute(query6,[nombrecontacto,numerocontacto,correocontacto,contactoid])
   con.commit()

def borrar_Cont(nombrecontacto):
    query4 ="""DELETE FROM contactos WHERE nombrecontacto = ? """
    cursor.execute(query4, (nombrecontacto,))


def menu():
    print("Bienvenido a su agenda.")
    print("seleccione una opcion segun lo que dese hacer: ")
    print("1.Agregar nuevo contacto.")
    print("2.Ver lista de contactos.")
    print("3.Buscar contacto por nombre o id.")
    print("4.Actualizar un contacto.")
    print("5.Eliminar un contacto.")
    print("6.Salir.")

#cursor.execute(query0)


menu()
select = int(input("> "))
while select != 6:
    
    if select == 1: #agregar contacto
        print("Porfavor complete los siguientes campos")
        nombrecontacto = str(input("Nombre: "))
        numerocontacto = int(input("Numero: "))
        correocontacto = str(input("Correo Electronico: "))
        insertar(nombrecontacto,numerocontacto,correocontacto)             
        print("Desea agregar otro contacto?")
        print("1.Si")
        print("2.No")
        opt = int(input("> "))
        while opt == 1:
          print("Porfavor complete los siguientes campos")
          nombrecontacto = str(input("Nombre: "))
          numerocontacto = int(input("Numero: "))
          correocontacto = str(input("Correo Electronico: "))
          insertar(nombrecontacto,numerocontacto,correocontacto)             
          print("Desea agregar otro contacto?")
          print("1.Si")
          print("2.No")
          opt = int(input("> "))


        menu()
        select = int(input("> "))

    if select == 2: #Ver lista de contactos
       
       print("Lista de contactos: ")
       cursor.execute(query2)
       result = cursor.fetchall()
       print(result)
       input("Pulse cualquiera tecla para continuar ")
        
       menu()
       select = int(input("> "))
    
    if select == 3: #buscar contacto
        print("Desea buscar por nombre o id: ")
        print("1.Nombre")
        print("2.Id")
        sl2 = int(input("> "))
        if sl2 == 1:
           nb = str(input("Inserte nombre: "))
           busquedanombre(nb)
           input("Pulse cualquiera tecla para continuar ")
           menu()
           select = int(input("> "))
        elif sl2 == 2:
            nbb = int(input("Inserte id: "))
            busquedaid(nbb)
            input("Pulse cualquiera tecla para continuar ")
            menu()
            select = int(input("> "))
                        
    if select == 4:#Actualizar contacto
        cursor.execute(query2)
        result = cursor.fetchall()
        print(result)
        idconsult = int(input("Por favor ingrese el id del contacto (numero que antecede al nombre): "))
        nombrecontacto = str(input("Introduzca el nuevo nombre: "))
        numerocontacto = int(input("Introduzca el nuevo numero: "))
        correocontacto = str(input("Indroduzca el nuevo correo electronico: "))        
        actualizarcontacto(nombrecontacto,numerocontacto,correocontacto,idconsult)
        busquedanombre(nombrecontacto)
        print("contacto actualizado")
        input("Pulse cualquiera tecla para continuar ")
        
        menu()
        select = int(input("> "))        

    if select == 5:#Borrar contacto
        print("su eliminacion sera permanete")
        security = str(input("escriba (si) para confirmar: "))
        if security == "si":
            nb = str(input("Inserte nombre de el contacto a borrar: "))
            borrar_Cont(nb)
            print(" su Contacto fue borrado exitosamete.")
            print("Lista de contactos: ")
            cursor.execute(query2)
            result = cursor.fetchall()
            print(result)
            input("Pulse cualquiera tecla para continuar ")

            menu()
            select = int(input("> "))
            
if select == 6:#salir
    print()