#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:

class Vehiculo:
    def __init__(self, color, tipo, cilindra):
        self.color = color
        self.tipo = tipo
        self.cilindra = cilindra



# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:


class Vehiculo:
    def __init__(self, color, tipo, cilindra):
        self.color = color 
        self.tipo = tipo
        self.cilindra = cilindra 
        self.velocidad = 0
        self.direccion = 0

    def acelerar(self,vel):
        self.velocidad += vel
    
    def frenar(self,vel):
        self.velocidad -= vel
    
    def doblar(self,grados):
        self.direccion += grados 




# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:
class Vehiculo:
    def __init__(self, color, tipo, cilindra):
        self.color = color 
        self.tipo = tipo
        self.cilindra = cilindra 
        self.velocidad = 0
        self.direccion = 0

    def acelerar(self,vel):
        self.velocidad += vel
    
    def frenar(self,vel):
        self.velocidad -= vel
    
    def doblar(self,grados):
        self.direccion += grados 
car1 = Vehiculo('rojo','carro',1.6)
car2 = Vehiculo('negro','camion',3.5)
car3 = Vehiculo('blanco','moto',1)


print(car1.color, car1.tipo, car1.cilindra)

print(car2.acelerar(40))






# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:
class Vehiculo:
    def __init__(self, color, tipo, cilindra):
        self.color = color 
        self.tipo = tipo
        self.cilindra = cilindra 
        self.velocidad = 0
        self.direccion = 0

    def acelerar(self,vel):
        self.velocidad += vel
    
    def frenar(self,vel):
        self.velocidad -= vel
    
    def doblar(self,grados):
        self.direccion += grados 
    
    def estado(self):
        print('Velocidad', self.velocidad, 'Gira', self.direccion)

    def caracteristica(self):
        print('el vehiculo es ', self.tipo, 'de color ', self.color, 'de cilindraje', self.cilindra)


car1 = Vehiculo('rojo','carro',1.6)
car2 = Vehiculo('negro','camion',3.5)
car3 = Vehiculo('blanco','moto',1)

car1.caracteristica()
car2.caracteristica()
car3.caracteristica()





# In[13]:






# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:

class Funciones_7:

    def __init__ (self):
        pass
    def es_primo(self,numero):

        primo = True
        for n in range(2,numero):
            if numero % n == 0:
                primo = False
                break
        return primo
    
    def cuenta_de_numeros_repetidos(self,lista, mayor = True):
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
    
    def convert_grados (self, unidad, grados_origen , grados_final):
        if grados_origen == 'celsius':
            if grados_final == 'celsius':
                grados_convert = unidad
            elif grados_final == 'farenheit':
                grados_convert = (unidad * 9/5) + 32
            elif grados_final == 'kelvin':
                grados_convert == (unidad + 273,15)
            else:
                print( 'parametro incorrecto')
        elif grados_origen == 'farenheit':
            if grados_final == 'farenheit':
                grados_convert = unidad
            elif grados_final == 'celsius':
                grados_convert = (unidad - 32 ) * 5/9
            elif grados_final == 'kelvin':
                grados_convert == (unidad -32 )* 5/9 + 273,15
            else:
                print( 'parametro incorrecto')
        elif grados_origen == 'kelvin':
            if grados_final == 'kelvin':
                grados_convert = unidad
            elif grados_final == 'celsius':
                grados_convert = (unidad - 273,15 ) 
            elif grados_final == 'farenheit':
                grados_convert == (unidad - 273,15) * 9/5 +32
            else:
                print( 'parametro incorrecto')
        else:
            print('ingrese variable correcta ')

        return grados_convert
    
    def num_fact(self,numero):
        if (type(numero) != int):
            return 'ingresa un numero entero'
        if (numero < 0):
            return 'ingresa un numero positivo'
        if (numero > 1):
            numero = numero * num_fact(numero - 1)
        return numero


#print('el numero mas repetido es ', f.cuenta_de_numeros_repetidos[0], 'y se repite ', f.cuenta_de_numeros_repetidos[1], 'veces')
# 6) Probar las funciones incorporadas en la clase del punto 5


# In[28]:
class Funciones_7:

    def __init__ (self):
        pass
    def es_primo(self,numero):

        primo = True
        for n in range(2,numero):
            if numero % n == 0:
                primo = False
                break
        return primo
    
    def cuenta_de_numeros_repetidos(self,lista, mayor = True):
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
    
    def convert_grados (self, unidad, grados_origen , grados_final):
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
                grados_convert =(unidad - 273,15) * 9/5 +32
            else:
                print( 'parametro incorrecto')
        else:
            print('ingrese variable correcta ')

        return grados_convert
    
    def num_fact(self,numero):
        if (type(numero) != int):
            return 'ingresa un numero entero'
        if (numero < 0):
            return 'ingresa un numero positivo'
        if (numero > 1):
            numero = numero * self.num_fact(numero - 1)
        return numero

f = Funciones_7()

f.es_primo(13)

lista_num = [1,1,5,6,8,10,22,5,6,4,11,9,5,1,1,1,2]
moda, repe = f.cuenta_de_numeros_repetidos(lista_num, True)
print(' el valor de ', moda, ' y se repte ', repe )

f.convert_grados(19,'celsius','kelvin')

f.num_fact(8)





# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:

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
f = Funciones_7([1,4,5,6,8,10,22,5,6,4,11,9,5,1,1,1,2])
f.es_primo()
f.convert_grados('celsius','farenheit')
f.num_fact()
#f.convert_grados(lista_num,'celsius','farenheit')
# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:

from fun07 import *

f2 = Funciones_7([1,3,5,7,9,3,4,])

f2.es_primo()




# %%
