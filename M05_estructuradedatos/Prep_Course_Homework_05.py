#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:


paises = ['Colombia', 'Peru', 'Mexico', 'Alemania', 'Argentina', 'Estados unidos']
print(paises)

# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

paises = ['Colombia', 'Peru', 'Mexico', 'Alemania', 'Argentina', 'Estados unidos']
print(paises[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

paises = ['Colombia', 'Peru', 'Mexico', 'Alemania', 'Argentina', 'Estados unidos']
print(paises[1:5:1])



# 4) Visualizar el tipo de dato de la lista

# In[12]:

paises = ['Colombia', 'Peru', 'Mexico', 'Alemania', 'Argentina', 'Estados unidos']
print(type(paises))



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

paises = ['Colombia', 'Peru', 'Mexico', 'Alemania', 'Argentina', 'Estados unidos']
print(paises[2:])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

paises = ['Colombia', 'Peru', 'Mexico', 'Alemania', 'Argentina', 'Estados unidos']
print(paises[:5])

    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

paises = ['Colombia', 'Peru', 'Mexico', 'Alemania', 'Argentina', 'Estados unidos']
paises.append('Argentina')
paises.append('Alemania')
print(paises)






# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

paises.insert(3, 'Venezuela')
print(paises)



# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:
paises_asia = ['japon', 'Korea', 'china', 'mongolia']
paises.extend(paises_asia)
print(paises)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

print(paises.index('Argentina'))



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

# print(paises.index('Uruguay'))
#   <module>
#     print(paises.index('Uruguay'))
#           ^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: 'Uruguay' is not in list




# 12) Eliminar un elemento de la lista

# In[25]:

paises.remove('japon')
print(paises)



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

# paises.remove('indonesia')
# print(paises)
# <module>
#     paises.remove('indonesia')
# ValueError: list.remove(x): x not in list


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

last = paises.pop()
print(last)



# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(paises * 4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

numeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(numeros)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(numeros[9:15])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

print(20 in numeros)
print(30 in numeros)



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

nuevo = 'francia'
if not nuevo in paises == True:
    paises.append(nuevo)
    print('Ingresa ', nuevo)
else:
    print('ya esta en lista')




# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

print(numeros.count(9))
print(paises.count('Argentina'))



# 21) Convertir la tupla en una lista

# In[52]:

numeros = list(numeros)
print(type(numeros))



# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:


n1,n2,n3,n4,n5,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_, = numeros
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:


diccio = { 'Pais': paises,
          'Ciudades': ['Bogota','Lima','Ciudad de mexico','Caracas','Berlin', 'Buenos Aires', 'Washinton','Bejgin'],
          'Continente': ['America', 'Europa', 'Asia']}
print(diccio)



# 24) Imprimir las claves del diccionario

# In[59]:

print(diccio.keys())


# 25) Imprimir las ciudades a través de su clave
print(diccio['Ciudades'])
# In[61]:




