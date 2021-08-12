import sys,os
from mainMenu import mainMenu
def main(args):
    tareas_terminadas = {}
    tareas_pendientes = {}
    condicion = True
    while condicion:
        
        mainMenu()
        opcion = input("Selecciona una opcion ")
        if not mainMenu(opcion):
            print("Opcion no valida")
        if int(opcion)==1:
            print(tareas_pendientes)
        if int(opcion)==2:
            tareas_pendientes.add(input("Que quieres añadir? "))
        if int(opcion)==3:
            if input("Introduce lo que quieres buscar? ") in tareas_pendientes:
                print("Si se encontro")
            else:
                print("No se encontro")
        if int(opcion)==4:
            elementoparaborrar= input("Introduce lo que quieres buscar? ")
            if elementoparaborrar in tareas_pendientes:
                tareas_pendientes.remove(elementoparaborrar)
                tareas_pendientes.clear()
                tareas_pendientes.remove(elementoparaborrar)
                print("Se borro")
            else:
                print("No se encontro")
        if int(opcion)==6:
            os.system('cls' if os.name=="nt" else "clear")
        if int(opcion)==7:
            tareas_pendientes.sort()
            print (tareas_pendientes)



if __name__=='__main__':
    main(sys.argv)