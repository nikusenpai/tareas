altura = int(input("ingresar altura"))
edad = int(input("ingresar edad"))

PDE = altura/edad**2 #PDE es Poder Entrar

if PDE<20:
    print("no puede entrar")
elif 20 < PDE <40:
    print("puede entrar")
else:
    print("tal vez")

print("tu estado de admision es: ")
print("PDE") 