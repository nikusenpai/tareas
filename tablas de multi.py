n1 = int(input("ingrese la tabla que quiere"))
n2 = int(input("ingresa el limite"))
def tablas (n):
    limite = n1
    contador = 1
    while contador<=limite:
        resultado = contador * n
        print (n1, "X",contador, "=", resultado)
        contador = contador + 1
tablas(n1)

