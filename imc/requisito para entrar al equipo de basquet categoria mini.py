altura = int(input("ingresar altura "))
edad = float(input("ingresa edad"))

PDE = altura*edad

if PDE<2250:
    print("te falta tiempo")
elif 2250 < PDE <3299:
    print("si")
elif 3300<PDE<3999:
    print("no eres para esta categoria")
else:
    print("ni de broma")

print("tu PDE es: ")
print(PDE)
