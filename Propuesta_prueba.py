llave = True
datos =[]


while llave == True:
    print("Ingrese el número de la acción que desea realizar: ")
    print("1.- Grabar datos")
    print("2.- Buscar por rut")
    print("3.- Listar datos de solterxs")
    print("4.- Salir")
    opción_menu_princ = int(input("Ingrese el número de la opción que desee: "))

    if opción_menu_princ == 1:
        lista_aux = []
        print("___Ingreso de datos nuevos___")
        print("A continuación se le pedirán los datos de la persona que desea registrar.\nIngrese los datos de acuerdo el formato solicitado.")
        rut = input("Ingrese el rut considerando el siguiente formato '12.345.678-a' :")
        lista_aux.append(rut)
        nom = input("Ingrese su nombre y apellido considerando el ejemplo 'Pablo Lopez': ")
        lista_aux.append(nom)
        edad = input ("Ingrese su edad en años siguiendo el ejemplo '28': ")
        lista_aux.append(edad)
        estado_civil = input ("Ingrese el número de la opción de su estado civil:\n1.- Solterx\n2.-Casadx\n3.-Viudx")
        lista_aux.append(estado_civil)
        fec_afil = input ("Ingrese la fecha de afiliación considerando el siguiente formato DD-MM-YYY ejemplo '05-04-2023': ")
        lista_aux.append(fec_afil)
        datos.append(lista_aux)
        print(datos)
    elif opción_menu_princ == 2:
        print("___Busqueda de datos___")
        print("Ingrese el número de rut de la persona que desea buscar, considere el siguiente formato '12.345.678-a': ")
    elif opción_menu_princ == 3:
        print("___Lista de solterxs___")
