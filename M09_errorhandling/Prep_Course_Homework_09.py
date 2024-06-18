#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:


import sys 

sys.path.append(r'/Users/macbookpro/Documents/Programacion /Python /Repositorio hub /Python-Prep/M09_errorhandling/fun07.py')

import fun07 as f 

f1 = f.Funciones_7(1,2,3,4,5)


# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:
import fun07 as f 
import importlib

importlib.reload(f)

f1 = f.Funciones_7([1,2,3,4,5])

#f1.convert_grados(1,2)

f1.convert_grados('celsius','farenheit')



# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# 
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

# In[9]:

import fun07 as f
import unittest

class Pruebas (unittest.TestCase):

    def test_prueba_crear_objeto(self):
        objeto = 'producto'
        self.assertRaises(ValueError,f.Funciones_7,objeto)
    def test_prueba_crear_objeto_correcta(self):
        objeto = [1,2,3,4,5,2]
        f1 = f.Funciones_7(objeto)
        self.assertAlmostEqual(f1.lista, objeto)
    def test_valor_primos(self):
        lis = [1,2,3,4,1,6,7,8]
        f1 = f.Funciones_7(lis)
        mas_repetido , max_rep = f1.__cuenta_de_numeros_repetidos(False)
        mas_repetido = [mas_repetido]
        mas_repetido.append(max_rep)
        result = [1,2]
        self.assertEqual(mas_repetido, result, 'no es igual')



unittest.main(argv=[''], verbosity=2, exit=False)

# if __name__ == '__main__':
#     unittest.main()

# 4) Probar una creación incorrecta y visualizar la salida del "raise"

# In[13]:


import unittest

f2 = f.Funciones_7('numero')

unittest.main(argv=[''], verbosity=2, exit=False)
# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

# In[14]:

class Test_probando_primos (unittest.TestCase):

    def test_verifica_primos(self):
        lis = [1,2,3,4,5,6,7]
        f1 = f.Funciones_7(lis)
        primos = f1.es_primo()
        primos_esperado = [True,False,True,False,False]
        self.assertEqual(primos, primos_esperado)

unittest.main(argv=[''], verbosity=2, exit=False)
# 7) Agregar casos de pruebas para el método conversion_grados()

# In[17]:

class Test_probando_grados(unittest.TestCase):

    def test_verifica_grados(self):
        lis = [1,2,33,4,14]
        f1 = f.Funciones_7(lis)
        grados = f1.convert_grados('celsius','farenheit')
        grados_esperado = [32,45,33,12,11]
        self.assertEqual(grados, grados_esperado)

    unittest.main(argv=[''], verbosity=2 , exit=False)



# 8) Agregar casos de pruebas para el método factorial()

# In[20]:

class Test_probando_fact(unittest.TestCase):

    def test_verifica_fafct(self):
        lis = [1,2,33,4,14]
        f1 = f.Funciones_7(lis)
        num_fact = f1.num_fact()
        fact_esperado = [32,45,33,12,11]
        self.assertEqual(num_fact, fact_esperado)

    unittest.main(argv=[''], verbosity=2 , exit=False)




# %%
