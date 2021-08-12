articulo1 = input("cual es su primer articulo? ")
articulo2 = input("cual es tu segundo articulo? ")
articulo3 = input("cual es tu tercer articulo? ")
articulo4 = input("cual es tu ultimo articulo? ")
listaDelSuper = {articulo1 , articulo2 , articulo3 , articulo4}
print ("esta es tu lista del super" , listaDelSuper)
res = input("quieres agregar algo más? y/n ")
while res == "y":
    agregado1 = input("que articulo quieres agregar? ")
    if agregado1 in listaDelSuper:
        print ("eso ya esta en la lista")
    elif agregado1 not in listaDelSuper:
        print("tu articulo fue agregado a la lista <3 ")
        listaDelSuper.add(agregado1)
        print ("esta es tu lista del super " , listaDelSuper)
    res = input("quieres agregar algo mas? y/n ")
re3 = input("quieres buscar un articulo? y/n ")
while re3 == "y":
    encontrar = input("que articulo buscas? ")
    if encontrar in listaDelSuper:
        print ("esta en la lista")
    elif encontrar not in listaDelSuper:
        print ("no esta en la lista :c")
    res3 = input("quieres buscar otro objeto? y/n ")
re2 = input("quieres eliminar algo de la lista? y/n ")
while re2 == "y":
    elemento = input("quieres eliminar el ultimo articulo agregado? ")
    for elemento in listaDelSuper:
        print (elemento)
        listaDelSuper.remove(elemento)
        print (listaDelSuper)
    res2 = input ("quieres seguir eliminando? ")

	





