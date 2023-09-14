class Funciones:

    def __init__(self, lista):
        self.lista = lista

    def primo(self):
        for i in self.lista:
            if (self.__primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__grados(i, origen, destino),'grados',destino)
        
    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))

    def __primo(self, n): 
        r = True
        for i in range(2,n):
    
            if n%i !=0:
                continue
            else:
                r = False
                break
        return r  

    def repetidosorden(self, menor=True):
        if len(self.lista) == 0:  # Verificación si la lista está vacía
            return None  # Si la lista está vacía, se devuelve None
        if menor:  # Verificación del parámetro menor
            self.lista.sort(reverse=True)  # Ordena la lista de forma ascendente si menor es verdadero
        else:
            self.lista.sort()  # Ordena la lista de forma descendente si menor es falso
        c = 1
        a=self.lista[0]
        for i in self.lista:
            if self.lista.count(i)>=c:
                c = self.lista.count(i)
                a = i
        return a, c

    def __grados(self, valor, origen, destino):
        if origen == destino: 
            return valor, destino
        else: 
            if origen == 'C':
                if destino == 'F':
                    valor = (valor*9/5)+32
                elif destino == 'K':
                    valor = valor+273.15
            elif origen == 'F':
                if destino == 'C':
                    valor = (valor-32)*5/9
                elif destino == 'K':
                    valor = (valor-32)*5/9+273.15
            elif origen == 'K':
                if destino == 'C':
                    valor = valor-273.15
                elif destino == 'F':
                    valor = (valor-273.15)*9/5+32
            return valor, destino    
    
    def __factorial(self, x): 
        if type(x) != int:
            return "El número debe ser entero"
        elif x<0:
            return "El número debe ser positivo"
        else: 
            if x == 1:
                return x 
            elif x==0:
                return 1
            
            x = x*self.__factorial(x-1)

            return x