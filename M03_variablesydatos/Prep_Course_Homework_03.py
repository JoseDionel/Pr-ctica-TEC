#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
a= 7
print(a)

# 2) Imprimir el tipo de dato de la constante 8.5

type(8.5)


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
type(a)

# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre = 'Alejandro'


# 5) Crear una variable que contenga un número complejo

# In[3]:

numero_complejo = 5 + 3 



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

type(numero_complejo)




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416
print(round(pi,4))
# In[1]:

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

variable = True
Variable2 = 'True'

# In[3]:


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(variable))
print(type(Variable2))

# In[5]:


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

Numero = 5 + 6.8
print(Numero)

# 11) Realizar una operación de suma de números complejos
a = 2 + 4
b = 5 + 7

print(a + b)
# In[2]:

# 12) Realizar una operación de suma de un número real y otro complejo

c = a + 9.3
print(c)
# In[4]:


# 13) Realizar una operación de multiplicación

print(8*2)
# In[5]:


# 14) Mostrar el resultado de elevar 2 a la octava potencia
print(8**2)
# In[6]:


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
d = 7/4 
print(d)
# In[8]:


# 16) De la división anterior solamente mostrar la parte entera
print(7//4)
# In[9]:



# 17) De la división de 27 entre 4 mostrar solamente el resto
print(7%4)
# In[1]:

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print (6*4+3)
# In[2]:



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
var1 = ' Colombia '
var2 = 'Bogota'

print(var1 + var2)
# In[3]:



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

print( 2 == '2')


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print( 2 == int('2'))


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

#a = float('3,8')# no se puede convertir un string en float 



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

e = 3 

e -= 1 

print(e)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:


print(1 << 2) # representa el desplazamiento de bits a la derecha 


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

#print(2 + '2') No se puede sumar str con int 




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

print ( 4 * 'Hola ' )

