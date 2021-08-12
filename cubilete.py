print("bienvenido al juego del cubilete")
NombreDeUsuario=input("nombre deljugador 1 ")
NombreDelRival=input("nombre del jugador 2 ")
print("turno de: "+ NombreDeUsuario + ", estos son tus dados ")
pregunta = "Y"
while pregunta == "Y": #si no se pone correctamente con un espacio por alguna razon entra en un loop infinito 
    import random
    DadoNumero11 = random.randint(1,6)
    DadoNumero21 = random.randint(1,6)
    DadoNumero31 = random.randint(1,6)
    DadoNumero41 = random.randint(1,6)
    DadoNumero51 = random.randint(1,6)
    print(DadoNumero11 , DadoNumero21 , DadoNumero31 , DadoNumero41 , DadoNumero51)
    pregunta = input ("continuar? Y/N")
print ("turno de: " + NombreDelRival + ", estos son tus dados" )
pregunta = "Y"
while pregunta == "Y":
    import random
    DadoDelRival11 = random.randint(1,6)
    DadoDelRival21 = random.randint(1,6)
    DadoDelRival31 = random.randint(1,6)
    DadoDelRival41 = random.randint(1,6)
    DadoDelRival51 = random.randint(1,6)
    print(DadoDelRival11 , DadoDelRival21 , DadoDelRival31 , DadoDelRival41 , DadoDelRival51)
    pregunta = input ("continuar? Y/N")
print ("estos son los resultados: ")
print (NombreDelRival + " obtuvo: ")
print (DadoDelRival11 + DadoDelRival21 + DadoDelRival31 + DadoDelRival41 + DadoDelRival51) 
jugador21 = (DadoDelRival11 + DadoDelRival21 + DadoDelRival31 + DadoDelRival41 + DadoDelRival51)
print (NombreDeUsuario + " obtuvo: ")
print (DadoNumero11 + DadoNumero21 + DadoNumero31 + DadoNumero41 + DadoNumero51)
Jugador11 = (DadoNumero11 + DadoNumero21 + DadoNumero31 + DadoNumero41 + DadoNumero51)
if Jugador11<jugador21:
    print(NombreDelRival + " GANA")
elif Jugador11>jugador21:
    print(NombreDeUsuario + " GANA")
elif Jugador11 == jugador21:
    print(NombreDeUsuario + NombreDelRival + "obtuvieron un empate ")
print("FIN DE JUEGO ")




    
