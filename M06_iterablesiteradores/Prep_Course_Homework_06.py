#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:

num_neg = []
numero = -15
while (numero < 0):
    numero += 1 
    num_neg.append(numero)
print(num_neg) 


# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
lista_pares = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,19,20]
n = 0
while (n < len(lista_pares)):
    if n % 2 != 0:   
        print(lista_pares[n])
    n += 1



# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

lista_pares = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,19,20]

for i in range(len(lista_pares)):
    if i % 2 != 0:
        print(lista_pares[i])



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

for i in lista_pares[:3]:
               print(i)



# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

for i in enumerate(lista_pares):
      print(i)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
lista = [1,2,5,7,8,10,13,14,15,17,20]

n = 1 
while (n <= 20):
    if ( not (n in lista)):
        lista.insert((n-1), n)
    n += 1
print(lista)
      

# In[11]:


n = 1



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:

lisnumero = [0,1]
indice = 2 
while indice < 30:
     lisnumero.append(lisnumero[indice-1]+lisnumero[indice-2])
     n += 1 
print(lisnumero)




# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

nuevalista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sumaden = 0
for n in nuevalista:
     sumaden += n
print(sumaden)


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:
nuevalista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

primeros = 15
n = primeros - 5
while(n < primeros):
    print(nuevalista[n]/nuevalista[n-1])
    n += 1

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola Mundo'

print(cadena.index('n'))

for i, c in enumerate(cadena):
    if c == 'n':
        print(i)



# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

Dictiona = {'Continente': ['America', 'Oceania','Europa','Asia','Africa'],
            'Paises':['Colombia','Chile','Mexico','España','Egipto','Japon','Australia'],
            'Ciudades':['Bogota','Santiago','Ciudad de Mexico','Sidney','Tokio','Cairo','Madrid','Cancun','Barselona']
}

print(Dictiona.keys())
for k in Dictiona:
     print(k)
# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:

cadena = 'Hola Mundo'
lista_cadena = list(cadena)

for l in lista_cadena:
     print(l)

# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

la = [1,2,3,4,5,6,7,8,9,10]
lb = ['a','b','c','d','e','f','g','h','i','j','k','g']
t = zip(la, lb)

print(list(t))



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
numero_divi_7 = []
for s in lis:
     if s % 7 == 0:
          numero_divi_7.append(s)
print(numero_divi_7)
          




# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

print(len(lis))

# In[51]:

elemento = 0
for e in lis:
     elemento +=1
print(elemento)



# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lista_convertida = []
for e in lis:
     if type(e) != list:
          lis.append([e])
print(lis)


# %%


# %%
