import csv
from ViajeroFrecuente import ViajeroFrecuente

class Manejador:
    # __listaViajeros=[]

    def __init__(self):
        self.__listaViajeros=[]


    def agregarViajero(self,unViajero):
        self.__listaViajeros.append(unViajero)

    def mostrasViajeros(self):
        for viajero in self.__listaViajeros:
            print(viajero)

    def testViajero(self):
        archivo=open('viajeros.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            numeroViajero=int(fila[0])
            dni=int(fila[1])
            nombre=fila[2]
            apellido=fila[3]
            acumMillas=int(fila[4])
            unViajero= ViajeroFrecuente(numeroViajero,dni,nombre,apellido,acumMillas)
            self.agregarViajero(unViajero)

    def buscarViajero (self,identificador):
        print(" ")
        print(f"IDENTIFICADOR: {identificador}")
        for i, unViajero in enumerate(self.__listaViajeros):
            if unViajero.getNumeroViajero()==identificador:
                return i
        return -1

    def getViajero(self, indice):
        return self.__listaViajeros[indice]

    def __str__(self):
        s=""
        for viajero in self.__listaViajeros:
            s+=str(viajero)+ '\n'
        return s


#if __name__ == "__main__":
#    manejador = Manejador()
#    manejador.testViajero()
