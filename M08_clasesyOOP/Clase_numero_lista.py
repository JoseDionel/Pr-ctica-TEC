class Numeros_lista:
    def __init__(self, lista):
        self.lista=lista

    def Numero_primo(self):
        for i in self.lista:
            if self.__Numero_primo(i):
                print(i, 'es un número primo')
            else:
                print(i, 'no es un número primo')

    def Convertir_grados(self,origen,destino):
        for i in self.lista:
            print(i,'°',origen,'son',self.__Convertir_grados(i,origen,destino),'°',destino)

    def Factorial(self):
        for i in self.lista:
            print('el factorial de',i, 'es', self.__Factorial(i))
    

    def __Numero_primo(self, nro):
        primo=True
        for i in range(2,nro):
            if nro%i==0:
                primo=False
        return(primo)
    
    def Numero_modal(self):
        temporal=0
        popular_temporal=0
        for i in self.lista:
            conteo=self.lista.count(i)
            if conteo>temporal:
                temporal=conteo
                popular_temporal=i
        return print('el numero modal es',popular_temporal, 'que ser repite',temporal)
    
    def __Convertir_grados(self,valor,origen,destino):
        if origen=='C':
            if destino=='F':
                grados=round(((valor*9/5)+32),2)
            elif destino=='K':
                grados= round((valor+273.15),2)
            elif destino=='C':
                grados= round((valor),2)
            else:
                grados='la unidad de destino no es válido'
        elif origen=='F':
            if destino=='C':
                grados=round(((valor-32)*5/9),2)
            elif destino=='K':
                grados= round((((valor-32)*5/9)+273.15),2)
            elif destino=='F':
                grados= round((valor),2)
            else:
                grados='la unidad de destino no es válido'
        elif origen=='K':
            if destino=='F':
                grados=round((((valor-273.15)*9/5)+32),2)
            elif destino=='C':
                grados= round((valor-273.15),2)
            elif destino=='K':
                grados= round((valor),2)
            else:
                grados='la unidad de destino no es válido'
        else:
            grados='la unidad de origen no es válida'
        return grados
    
    def __Factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__Factorial(numero - 1)
        return numero