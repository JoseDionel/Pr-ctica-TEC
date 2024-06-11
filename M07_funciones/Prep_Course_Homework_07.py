#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:


def es_primo(numero):

    primo = True
    for n in range(2,numero):
        if numero % n == 0:
            primo = False
            break
    return primo

es_primo(6)
    


# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
# def es_primo(numero):

#     primo = True
#     for n in range(2,numero):
#         if numero % n == 0:
#             primo = False
#             print('No es primo')
#             break
#     return primo

def lista_de_numero(listacomoleta):
    lista_primos = []
    for i in listacomoleta:
        if es_primo(int(i)):
            lista_primos.append(i)
    return lista_primos

listacomoleta = [1,2,3,4,5,6,7,8,9,10,11.12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

lista_de_numero(listacomoleta)

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera


# In[33]:


def cuenta_de_numeros_repetidos(lista):
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
    return mas_reptido, max_rep

lista_num = [1,1,5,6,8,10,22,5,6,4,11,9,5]
conteo = cuenta_de_numeros_repetidos(lista_num)
print('el numero mas repetido es ', conteo[0], 'y se repite ', conteo[1], 'veces')


# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

# In[45]:
def cuenta_de_numeros_repetidos(lista, mayor = True):
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

lista_num = [1,1,5,6,8,10,22,5,6,4,11,9,5,1,1,1,2]
conteo = cuenta_de_numeros_repetidos(lista_num, True)
print('el numero mas repetido es ', conteo[0], 'y se repite ', conteo[1], 'veces')
conteo = cuenta_de_numeros_repetidos(lista_num, False)
print('el numero menor mas repetido es ', conteo[0], 'y se repite ', conteo[1], 'veces')


# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:

def convert_grados (unidad, grados_origen , grados_final):
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


convertidor_caf = convert_grados(100, 'celsius', 'farenheit')

print ('Celsius a Farenheit es : ', convertidor_caf)



# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:
def convert_grados (unidad, grados_origen , grados_final):
    if grados_origen == 'celsius':
        if grados_final == 'celsius':
            grados_convert = unidad
        elif grados_final == 'farenheit':
            grados_convert = (unidad * 9/5) + 32
        elif grados_final == 'kelvin':
            grados_convert = unidad + 273.15
        else:
            print( 'parametro incorrecto')
    elif grados_origen == 'farenheit':
        if grados_final == 'farenheit':
            grados_convert = unidad
        elif grados_final == 'celsius':
            grados_convert = (unidad - 32 ) * 5/9
        elif grados_final == 'kelvin':
            grados_convert = ((unidad -32 )* 5/9) + 273.15
        else:
            print( 'parametro incorrecto')
    elif grados_origen == 'kelvin':
        if grados_final == 'kelvin':
            grados_convert = unidad
        elif grados_final == 'celsius':
            grados_convert = (unidad - 273.15 ) 
        elif grados_final == 'farenheit':
            grados_convert = ((unidad - 273.15) * 9/5) +32
        else:
            print( 'parametro incorrecto')
    else:
        print('ingrese variable correcta ')

    return grados_convert

unidades_tem = ['celsius', 'farenheit','kelvin']

for i  in range(0,3):
    for j in range(0,3):
        #print(i, j)
        print('por cada grado de ', unidades_tem[i], 'equivale a ', unidades_tem[j], convert_grados(1,unidades_tem[i], unidades_tem[j]))


# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:


def num_fact(numero):
    if (type(numero) != int):
        return 'ingresa un numero entero'
    if (numero < 0):
        return 'ingresa un numero positivo'
    if (numero > 1):
        numero = numero * num_fact(numero - 1)
    return numero


print(num_fact(3))
print(num_fact(-2))
print(num_fact(1.2))
print(num_fact(23))
print(num_fact('d'))

# %%
