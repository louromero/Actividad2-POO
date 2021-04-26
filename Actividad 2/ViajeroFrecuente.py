import csv

class ViajeroFrecuente:
    __numeroViajero = None
    __dni = None
    __nombre = None
    __apellido = None
    __acumMillas = None

    def __init__(self,numeroViajero,dni,nombre,apellido,acumMillas):
        self.__numeroViajero = numeroViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__acumMillas = acumMillas

    def __str__(self):
        # return "{} {} {} {} {}".format(self.__numeroViajero,self.__dni,self.__nombre,self.__apellido,self.__acumMillas)
        # return "%d %d %s %s %d" %(self.__numerosViajero,self.__dni,self.__nombre,self.__apellido,self.__acumMillas)
        return 'Numero de viajero: {} \nDNI: {} \nNombre: {} \nApellido: {} \nMillas acumuladas: {}'.format(self.__numeroViajero,self.__dni,self.__nombre,self.__apellido,self.__acumMillas)

    def getNumeroViajero (self):
        return self.__numeroViajero

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def cantidadTotaldeMillas(self):
        return self.__acumMillas

    def acumularMillas(self, millas):            
        self.__acumMillas+=millas

    def canjearMillas(self,millas):
        if millas <= self.__acumMillas:
            self.__acumMillas -= millas
        else:
            print("Error de operación.")
