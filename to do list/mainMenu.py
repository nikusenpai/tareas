def mainMenu():
    print("1.- mostrar la lista ")
    print("2.- añadir a la lista ")
    print("3.- buscar en la lista ")
    print("4.- borrar de la lista ")
    print("5.- modificar lista ")
    print("6.- limpiar la lista ")
    print("7.- organizar lista ")
    print("8.- mostrar tareas terminadas ")
    print("9.- mostrar tareas completadas ")
    print("10.- terminar tarea  ")
    print("11.- abrir tarea ")
    print("12.- sali de la aplicacion ")

def validareMenu(opcion):
    if int (opcion)<1 or int (opcion)>12:
        return False
    return True