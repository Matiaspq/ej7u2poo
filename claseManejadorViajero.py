import csv
from claseViajero import ViajeroFrecuente
from menu import menu
class ManejadorClaseViajero:
    def __init__(self):
        self.__viajeros=[]

    def cargaViajero(self):
        archivo = open('viajerofrecuente.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            viajero=ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
            self.__viajeros.append(viajero)

    def buscaViajero(self,num):
        i = 0
        while i < len(self.__viajeros) and self.__viajeros[i].getNumViajero() != num:
            i+=1
        menu(self.__viajeros[i],num)

    def mayorCantidaddeMillas(self):
        viajerosmax=[]
        viajeromax=max(self.__viajeros).cantidadTotalMillas()
        print(f"El o los viajeros con mas millas acumuladas son:")
        for viajero in self.__viajeros:
            if viajero.cantidadTotalMillas()==viajeromax:
                viajerosmax.append(viajero)
        for viajero in viajerosmax:
            print(viajero)

    def acumularMillasadd(self):
        #v=ViajeroFrecuente(4,1587452,"Angel","Mercado",5000)
        self.__viajeros[0]+100
        #v=v+100
        #self.__viajeros.append(v)

    def canjearMillassub(self):
        #v=ViajeroFrecuente(5,2584712,"Martin","Perez",6000)
        self.__viajeros[0]-100
        #v=v-100
        #self.__viajeros.append(v)
    
    def comparamillas(self):
        millas=int(input("Ingresa millas"))
        print(self.__viajeros[0]==millas)
        print(millas==self.__viajeros[0])

    def acumularMillasrsub(self):
        100+self.__viajeros[0]

    def canjearMillasrsub(self):
        1000-self.__viajeros[0]

    def mostrar(self):
        for viajero in self.__viajeros:
                print(viajero)