#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
a=14
print(a)

# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
type(8.5)

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
type(a)

# 4) Crear una variable que contenga tu nombre

# In[2]:
minombre = 'Maria Laura'

# 5) Crear una variable que contenga un número complejo

# In[3]:
nrocomplejo = 2j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
type(nrocomplejo)

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
pi = 3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
Truestring = 'True'
Truebooleano= True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
Print(Type (Truestring))
Print(Type (Trueboolenao)) 

# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
var = 1 + 2.5

# 11) Realizar una operación de suma de números complejos

# In[2]:
 2J +3J

# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
10 +5j

# 13) Realizar una operación de multiplicación

# In[5]:
8*5

# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
Print(2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
x=27
y=4
print(x/y)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
x=27/4
print(int(x))


# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
x=27
y=4
print(x%y)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

resul= 4*6+3

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
a= 'Buen'
b= 'día'
saludo = a + b




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
"no es igual porque uno es string y el otro entero o float
int('2') + int(2)
4
str(2) + str('2')
22
float('2') +float(2)
0.4
float(2) +float('2?)  
4.0


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
2 == int('2)




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
#porque '3,8' es string




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
a=3
-= 1
print(a)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
1 << 2
#el sitema bnario esta representado por 0 y 1
# el 1 en binario es 0001
#  1 << 2 signifca correr a la  izquierda 2 posiciones y quedaria 0100


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
=el operando es igual pero tipo de dato es distinto

# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
2 +int(´2´)
