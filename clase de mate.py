resultado1 = int(input("ingrese el resultado del primer examen "))
if resultado1>=85:
    print ("ve al siguiente examen")
    resultado2 = int(input("ingresar el resultado del segundo examen "))
    if resultado2>=90:
        print("ve al siguiente exmane")
        resultado3 = int(input("ingresar el ultimo resultado "))
        if resultado3>=95:
            print("vas en la clase 103")
        elif resultado3<95:
            print("vas a la clase 102")
    elif resultado2<90:
        print ("vas en la clase 102")
elif resultado1<85:
    print ("vas a la clase 101")
