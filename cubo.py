
largo=int(input("largo"))
ancho=int(input("ancho"))
for i in range(largo):
    print("* ", end="")
print()

for i in range(ancho - 2):
    print("* ", end="")
    for j in range(largo - 2):
        print("  ", end="")
    print("*")

for i in range(ancho):
    print("* ", end="")
        
