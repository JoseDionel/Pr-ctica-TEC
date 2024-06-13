class Funciones_7:

    def __init__ (self, lista_de_numeros):
        self.lista = lista_de_numeros
        pass
    def es_primo(self):
        primo = True
        for i in self.lista:
           for n in range(2,i):
                if i % n == 0:
                    primo = False
                    print(i, 'no es numero primo')
                else:
                    (i, 'es numero primo')
    def convert_grados(self, grados_origen, grados_destino):
        for i in self.lista:
            print(i, 'grados',grados_origen, ' es igual a', self.__convert_grados(i,grados_origen,grados_destino),'grados',grados_destino)

    def num_fact (self):
        for i in self.lista:
            print('numero fact de ', i ,' es', self.__num_fact(i))

    def __es_primo(self,numero):
        primo = True
        for n in range(2,numero):
            if numero % n == 0:
                primo = False
                break
        return primo
    
    def __cuenta_de_numeros_repetidos(self,lista, mayor = True):
        conteo_numeros = {}
        for num in lista:
            if num in conteo_numeros:
                conteo_numeros[num] +=1
            else:
                conteo_numeros[num] = 1
        mas_reptido = ''
        max_rep = 0

        for num, repeticiones in conteo_numeros.items():
            if repeticiones > max_rep:
                mas_reptido = num
                max_rep = repeticiones
            elif repeticiones == max_rep:
                if mayor:
                    if num > mas_repetido:
                        mas_repetido = num
                else:
                    if num < mas_repetido:
                        mas_repetido = num

        return mas_reptido, max_rep
    
    def __convert_grados (self, unidad, grados_origen , grados_final):
        if grados_origen == 'celsius':
            if grados_final == 'celsius':
                grados_convert = unidad
            elif grados_final == 'farenheit':
                grados_convert = (unidad * 9/5) + 32
            elif grados_final == 'kelvin':
                grados_convert = (unidad + 273,15)
            else:
                print( 'parametro incorrecto')
        elif grados_origen == 'farenheit':
            if grados_final == 'farenheit':
                grados_convert = unidad
            elif grados_final == 'celsius':
                grados_convert = (unidad - 32 ) * 5/9
            elif grados_final == 'kelvin':
                grados_convert = (unidad -32 )* 5/9 + 273,15
            else:
                print( 'parametro incorrecto')
        elif grados_origen == 'kelvin':
            if grados_final == 'kelvin':
                grados_convert = unidad
            elif grados_final == 'celsius':
                grados_convert = (unidad - 273,15 ) 
            elif grados_final == 'farenheit':
                grados_convert = (unidad - 273,15) * 9/5 +32
            else:
                print( 'parametro incorrecto')
        else:
            print('ingrese variable correcta ')

        return grados_convert
    
    def __num_fact(self,numero):
        if (type(numero) != int):
            return 'ingresa un numero entero'
        if (numero < 0):
            return 'ingresa un numero positivo'
        if (numero > 1):
            numero = numero * self.__num_fact(numero - 1)
        return numero