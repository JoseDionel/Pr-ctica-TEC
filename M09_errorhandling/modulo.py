class Herramientas:

    def __init__(self, lista_numeros):
        if type(lista_numeros) != list:
            self.lista= []
            raise ValueError('Se esperaba una lista de enteros')
        else:
            self.lista = lista_numeros

    def primo(self):
        for i in self.lista:
            if self.__primo(i):
                print(i, 'es primo')
            else:
                print (i, 'no es primo')

    def __primo(self,nro):
        es_primo = True
        for i in range(2,nro):
            i = int(i)
            if nro % i == 0:
                es_primo= False
                break
        return(es_primo)
    
    def modal(self):
        conteo = dict()
        for i in self.lista:
            if i not in conteo:
                conteo[i] = 1
            else:
                conteo[i] += 1

        mayor = 0
        for j in conteo:
            if conteo[j] > mayor:
                mayor = conteo[j]
                numero = j
                
        print('El', numero ,'se repite', mayor, 'veces')

    def grados(self, origen, destino):
        parametros = ['Celsius','Farenheit', 'Kelvin']
        if origen not in parametros:
            return('Error en la unidad de origen')
        elif destino not in parametros:
            return('Error en la unidad de destino')
        else:
            for i in self.lista:
                print(i, "grados", origen, 'son', self.__grados(i,origen,destino),'grados',destino)

    
    def __grados(self, valor, origen, destino):
        c = 'Celsius'
        f = 'Farenheit'
        k = 'Kelvin'
        if origen == c:
            if destino == c:
                valor_final = valor
                unidad = '°C'
            elif destino == f:
                valor_final = (valor*9/5) + 32
                unidad = '°F'
            elif destino == k:
                valor_final = valor + 273
                unidad = '°K'
        elif origen == f:
            if destino == c:
                valor_final = (valor - 32)*5/9 
                unidad = '°C'
            elif destino == f:
                valor_final = valor
                unidad = '°F'
            elif destino == k:
                valor_final = (valor + 459.67) * 5/9
                unidad = '°K'
        elif origen == k:
            if destino == c:
                valor_final = valor -273
                unidad = '°C'
            elif destino == f:
                valor_final = valor*9/5 - 459.67
                unidad = '°F'
            elif destino == k:
                valor_final = valor
                unidad = '°K'   
        return (valor_final)
    
    def factorial(self):
        for i in self.lista:
            print('el factorial de', i, 'es', self.__factorial(i))

    
    def __factorial(self, nro):
        fact = 1
        if type(nro) == int:
            if nro >= 0:
                for i in range(1,nro+1):
                    fact *= i 
                return fact
            else:
                print('se debe ingresar un positivo')         
        else:
            print('se debe ingresar un entero')

