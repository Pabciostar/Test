precio_1 = 2500
precio_2 = 5000
precio_3 = 1000
tipo_entrada = 0
cant_1 = 0
cant_2 = 0
cant_3 = 0
dia_semana = 0
llave_inicio = True
llave = True
llave_boleta = True
seguir_comprando = 0

while llave_inicio == True :
    try:
        print(">>> Bienvenidx al torneo Buena Ventura <<<")
        while llave == True :
            print("\n A continuación se muestran las entradas que tenemos disponibles")
            print("1.- Entrada niños (de 5 a 12 años) --> $2.500")
            print("2.- Entrada general (de 13 a 64 años) --> $5.000")
            print("3.- Entrada adultxs mayores (de 65 para arriba) --> $1.000")
            print("4.- Salir")
            tipo_entrada = int(input("\nIngrese el número de la opción que desee: "))

            if tipo_entrada == 1 :
                cant_1 = int(input("\nIngrese la cantidad de entradas que desea del tipo que escrogió: \nIngrese 0 para volver al menú"))
                if cant_1 > 0 :
                    seguir_comprando = int(input("Desea seguir comprando?: \n1.-Si\n2.-No"))
                    if seguir_comprando == 1 :
                        llave = True
                    elif seguir_comprando == 2 :
                        llave = False
                        llave_boleta = False
                elif cant_1 == 0 :
                    llave = True
                else :
                    print("Por favor: Ingrese un valor válido")
                    llave = True

            elif tipo_entrada == 2 :
                cant_2 = int(input("\nIngrese la cantidad de entradas que desea del tipo que escrogió: \nIngrese 0 para volver al menú"))
                if cant_2 > 0 :
                    seguir_comprando = int(input("Desea seguir comprando?: \n1.-Si\n2.-No"))
                    if seguir_comprando == 1 :
                        llave = True
                    elif seguir_comprando == 2 :
                            llave = False
                            llave_boleta = False
                elif cant_2 == 0 :
                    llave = True
                else :
                    print("Por favor: Ingrese un valor válido")
                    llave = True

            elif tipo_entrada == 3 :
                cant_3 = int(input("\nIngrese la cantidad de entradas que desea del tipo que escrogió: \nIngrese 0 para volver al menú"))
                if cant_3 > 0 :
                    seguir_comprando = int(input("Desea seguir comprando?: \n1.-Si\n2.-No"))
                    if seguir_comprando == 1 :
                        llave = True
                    elif seguir_comprando == 2 :
                        llave = False
                        llave_boleta = False
                elif cant_3 == 0 :
                    llave = True
                else :
                    print("Por favor: Ingrese un valor válido")
                    llave = True
            
            elif tipo_entrada == 4 :
                print("Gracias, vuelva pronto")
                llave_inicio = False
            
            else :
                print("Ingrese una opción válida")
                llave_inicio = True

        while llave_boleta == False :
            dia_semana = int(input("1.-Lunes\n2.-Martes\n3.-Miércoles\n4.-Jueves\n5.-Viernes\n6.-Sábadp\n7.-Domingo\nIngrese el número asociado al día en que irán: "))
            if dia_semana > 0 and dia_semana < 8 :
                if dia_semana == 5 :
                    descuento_1 = 0.1
                    descuento_2 = 0.05
                else:
                    descuento_1 = 0
                    descuento_2 = 0
            print("A continuación se muestra su boleta:")
            print("~~~~~~~~~~~~~~~~~~~~~~BOLETA~~~~~~~~~~~~~~~~~~~~~~")
            print("__________________________________________________")
            print(f"{cant_1} Entrada(s) para Niño(s) ---> ${cant_1*precio_1}")
            print(f"{cant_2} Entrada(s) para Niño(s) ---> ${cant_2*precio_2}")
            print(f"{cant_3} Entrada(s) para Niño(s) ---> ${cant_3*precio_3}")
            print("___________________________________________________")
            print(f"Subtotal:       $ {cant_1*precio_1+cant_2*precio_2+cant_3*precio_3}")
            print(f"Descuentos:     $ {cant_1*precio_1*descuento_1+cant_2*precio_2*descuento_2}")
            print("___________________________________________________")
            print(f"Total a pagar:  $ {(cant_1*precio_1+cant_2*precio_2+cant_3*precio_3)-(cant_1*precio_1*descuento_1+cant_2*precio_2*descuento_2)}")
            print("\n~~~~~~~~~~~~~~Gracias por su compra!~~~~~~~~~~~~~~")
            llave_boleta = True
            llave_inicio = False
    
    except:
        print("Ingrese un valor válido")
        llave_inicio = True


                







