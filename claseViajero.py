class ViajeroFrecuente:
    def __init__(self, num, dni, nombre, apellido, millas):
        self.__num_viajero=num
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def acumularMillas(self, millas):
        self.__millas_acum+=millas
        return self.__millas_acum

    def canjearMillas(self, millascanj):
        if millascanj<=self.__millas_acum:
            self.__millas_acum-=millascanj
            return self.__millas_acum
        else: print ("Error")
        
    def getNumViajero(self):
        return self.__num_viajero
    
    def __gt__(self, otro):
        return self.__millas_acum>otro.__millas_acum
    
    def __str__(self):
        return f"{self.__dni} {self.__nombre} {self.__apellido} {self.__millas_acum}"
    
    def __add__(self,millas):
        return self.acumularMillas(millas)
    
    def __radd__(self,millas):
        return self.__add__(millas)
            
    def __sub__(self,millas):
        return self.canjearMillas(millas)
    
    def __rsub__(self,millas):
        return self.canjearMillas(millas)
    
    def __eq__(self,millas):
        return self.__millas_acum==millas





