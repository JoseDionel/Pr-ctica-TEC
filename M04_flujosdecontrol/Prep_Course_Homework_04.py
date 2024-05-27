#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

Variable = 3

if Variable > 0:
    print(f'{Variable}Es mayor que 0')
elif Variable < 0:
    print(f'{Variable}Es menor que 0')
else :
    print(f'{Variable}Es igual que 0')


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a = 4
b = 2.3

if type(a) == type(b):
    print('son el mismo tipo de datos')
else:
    print('no son el mismo tipo de datos')



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for n in range(1,21):
    if n % 2 == 0:
        print(f'{n}','' ,'es par')
    else:
        print(f'{n}', '','es impar')



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for n in range(0,6):
    print('El valor', str(n), 'elevado a la 3 es ', str(n**3))

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

numero = 4

for n in range(0,numero):
    print(n)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

Variable = 3

if Variable == int(Variable):
    if (Variable > 0):
        factorial = Variable
        while (Variable > 2):
            Variable -=  1
            factorial = factorial * Variable
        print('el factorial es', factorial)
    else:
        print('el numero es menor que cero')
else:
    print('el numero no es entero')


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

i = 0 

while (numero < 5):
    numero += 1
    for i in range(0,numero):
        print('el', 'for', i)
        print('el', 'while', numero)
print('fin')
    


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

n = 5

for i in range(1,n):
    while (i < 5):
        i += 1
        print('for', i)
        print('while', n)

# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

Rango = 30 
numero = 0
primo = True

while numero < Rango:
    for prim in range(2,numero):
        if numero % prim == 0:
            primo = False
        
    if (primo):
        print(numero)
    else:
        primo = True
        
    numero += 1


        
# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
Rango = 30 
numero = 0
primo = True

while numero < Rango:
    for prim in range(2,numero):
        if numero % prim == 0:
            primo = False
            break
    if (primo):
        print(numero)
    else:
        primo = True
        
    numero += 1





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

# En parar la iteraciòn al momento de encontrar el primer divisior y evitar iteraciones innesesarias


# In[57]:




# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# In[58]:

#Si, ya que la al aumnentar el rango, incrementa las iteraciones 



# In[59]:




# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

numero = 0

while (numero <= 300):
    numero += 1
    if numero % 12 != 0:
        continue
    else:
        print(numero)

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

# Primo = True

# while True:
#     numero_ingresado = int(input('ingresa numero, escribe 1 para terminar :   '))
#     if numero_ingresado == 1:
#         break
#     try:
#         for i in range(2,numero_ingresado):
#             if numero_ingresado % i == 0:
#                 primo = False
#                 print(f'{numero_ingresado}','No es primo')
#                 break
#         if (primo):
#             print(f'{numero_ingresado}', 'Es primo')
#     except ValueError:
#         print('Numero mayor que 2')
    


# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:


rango_max = 300
rango_min = 100 

print( 'hola ')
for i in range(rango_min, rango_max):
    numerodiv = i // 3 
    print ( numerodiv)

