n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    1) Sumar 
    2) Restar 
    3) Multiplicar 
    4) Cambiar ambos numeros
    5) elevar a la potencia 
    6) obtener el cociente 
    7) dividir 
    8) apagar la calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO: ",n1+n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: ",n1-n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO:" ,n1*n2)
    elif opcion == 4:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
    elif opcion == 5:
        print (" ")
        print ("RESULTADO: ", n1**n2)
    elif opcion == 6:
        print (" ")
        print ("RESULTADO: ",n1 // n2)
    elif opcion == 7:
        print (" ")
        print ("RESULTADO: ", n1 / n2)
    elif opcion == 8:
        print (" ")
        print ("tenga buen dia <3")
        break
    else:
        print("Opción incorrecta")