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
print("FIN DE LA RONDA 1 ------------------------------------------------------------------------------") #aquí acaba la primera ronda ----------------------------------------------------------------------------------------------------------------------------
while pregunta == "Y":  
    import random
    DadoNumero12 = random.randint(1,6)
    DadoNumero22 = random.randint(1,6)
    DadoNumero32 = random.randint(1,6)
    DadoNumero42 = random.randint(1,6)
    DadoNumero52 = random.randint(1,6)
    print(DadoNumero12 , DadoNumero22 , DadoNumero32 , DadoNumero42 , DadoNumero52)
    pregunta = input ("continuar? Y/N")
print ("turno de: " + NombreDelRival + ", estos son tus dados" )
pregunta = "Y"
while pregunta == "Y":
    import random
    DadoDelRival12 = random.randint(1,6)
    DadoDelRival22 = random.randint(1,6)
    DadoDelRival32 = random.randint(1,6)
    DadoDelRival42 = random.randint(1,6)
    DadoDelRival52 = random.randint(1,6)
    print(DadoDelRival12 , DadoDelRival22 , DadoDelRival32 , DadoDelRival42 , DadoDelRival52)
    pregunta = input ("continuar? Y/N")
print ("estos son los resultados: ")
print (NombreDelRival + " obtuvo: ")
print (DadoDelRival12 + DadoDelRival22 + DadoDelRival32 + DadoDelRival42 + DadoDelRival52) 
jugador22 = (DadoDelRival12 + DadoDelRival22 + DadoDelRival32 + DadoDelRival42 + DadoDelRival52)
print (NombreDeUsuario + " obtuvo: ")
print (DadoNumero12 + DadoNumero22 + DadoNumero32 + DadoNumero42 + DadoNumero52)
Jugador12 = (DadoNumero12 + DadoNumero22 + DadoNumero32 + DadoNumero42 + DadoNumero52)
if Jugador12<jugador22:
    print(NombreDelRival + " GANA")
elif Jugador12>jugador22:
    print(NombreDeUsuario + " GANA")
elif Jugador12 == jugador22:
    print(NombreDeUsuario + NombreDelRival + "obtuvieron un empate ")
print("FIN DE LA RONDA 2 ---------------------------------------------------------------------------------") #FIN DE LA RONDA 2 --------------------------------------------------------------------------------------------------------------------------------
while pregunta == "Y": 
    import random
    DadoNumero13 = random.randint(1,6)
    DadoNumero23 = random.randint(1,6)
    DadoNumero33 = random.randint(1,6)
    DadoNumero43 = random.randint(1,6)
    DadoNumero53 = random.randint(1,6)
    print(DadoNumero13 , DadoNumero23 , DadoNumero33 , DadoNumero43 , DadoNumero53)
    pregunta = input ("continuar? Y/N")
print ("turno de: " + NombreDelRival + ", estos son tus dados" )
pregunta = "Y"
while pregunta == "Y":
    import random
    DadoDelRival13 = random.randint(1,6)
    DadoDelRival23 = random.randint(1,6)
    DadoDelRival33 = random.randint(1,6)
    DadoDelRival43 = random.randint(1,6)
    DadoDelRival53 = random.randint(1,6)
    print(DadoDelRival13 , DadoDelRival23 , DadoDelRival33 , DadoDelRival43 , DadoDelRival53)
    pregunta = input ("continuar? Y/N")
print ("estos son los resultados: ")
print (NombreDelRival + " obtuvo: ")
print (DadoDelRival13 + DadoDelRival23 + DadoDelRival33 + DadoDelRival43 + DadoDelRival53) 
jugador23 = (DadoDelRival13 + DadoDelRival23 + DadoDelRival33 + DadoDelRival43 + DadoDelRival53)
print (NombreDeUsuario + " obtuvo: ")
print (DadoNumero13 + DadoNumero23 + DadoNumero33 + DadoNumero43 + DadoNumero53)
Jugador13 = (DadoNumero13 + DadoNumero23 + DadoNumero33 + DadoNumero43 + DadoNumero53)
if Jugador13<jugador23:
    print(NombreDelRival + " GANA")
elif Jugador13>jugador23:
    print(NombreDeUsuario + " GANA")
elif Jugador13 == jugador23:
    print(NombreDeUsuario + NombreDelRival + "obtuvieron un empate ")
print("FIN DE LA RONDA 3 -----------------------------------------------------------------------------------------")
ResultadoFinal1 = (Jugador11 + Jugador12 + Jugador13)
ResultadoFinal2 = (jugador21 + jugador22 + jugador23)
print("reultados finales: ")
print (NombreDeUsuario + " obtuvo: ")
print (ResultadoFinal1)
print (NombreDelRival + " obtuvo: ")
print (ResultadoFinal2)
if ResultadoFinal1<ResultadoFinal2:
    print(NombreDelRival + " GANA EL JUEGO")
elif ResultadoFinal1>ResultadoFinal2:
    print(NombreDeUsuario + " GANA EL JUEGO")
elif ResultadoFinal1 == ResultadoFinal2:
    print("AMBOS JUGADORES EMPATARON")
print ("FIN DEL JUEGO ")
