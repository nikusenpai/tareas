N = int(input("ingrese un numero"))
def numeros_primos():
    numero = 2
    yield numero
    while True:
        T = numero
        while True:
            T += 1
            contador = 1
            numero_de_divisores = 0
            while contador <= T:
                if T % contador == 0:
                    numero_de_divisores += 1
                if numero_de_divisores > 2:
                    break
                contador += 1
            if numero_de_divisores == 2:
                yield T
            
i = numeros_primos()
primos = [next(i) for _ in range(N)]
print(primos)