from Manejador import Manejador
from Menu import Menu

def imprimir():
    print(" ")
    print("---------- MENU --------")
    print("Opciones disponibles:")
    print("1. Consultar viajeros ")
    print("2. Salir")
    print(" ")

def mostrar():
    print(" ")
    print("---------- MENU --------")
    print("Opciones disponibles:")
    print("1. Consultar Cantidad de Millas. ")
    print("2. Acumular Millas.")
    print("3. Canjear Millas.")
    print("4. Salir")
    print(" ")


def menu():
    band = True
    while band:
        imprimir()
        opcion=int(input("Ingrese Opcion: "))
        if opcion==1:
            manejadorViajero=Manejador()
            manejadorViajero.testViajero()
            num=int(input("Ingrese número de viajero para ver datos: "))
            indice = manejadorViajero.buscarViajero(num)
            if indice != -1:
                print('Se encontro en el lugar: ',indice)
                viajero=manejadorViajero.getViajero(indice)
                print(viajero)
                bandera=True
                while bandera:
                    mostrar()
                    memenu=Menu()
                    opcionesViajero=int(input("Ingrese una opción: "))
                    memenu.opcion(viajero,opcionesViajero)
                    if opcionesViajero == 4:
                        print("\nChau :)")
                        print(" ")
                        bandera=False
            else:
                print('El número de viajero no existe')
        elif opcion==2:
            print("\nChau :)")
            print(" ")
            band=False
        else:
            print("\n Opción no valida")

if __name__== '__main__':
    menu()