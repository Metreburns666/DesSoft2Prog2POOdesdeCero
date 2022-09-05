#Herencia Parte Practica
# Funciones Integradas en Objetos



class Calculadora:
    def __init__(self,numero):
        self.n=numero
        self.datos=[0 for i in range(numero)]
    
    def ingresarDato(self):
        self.datos=[int(input("Ingresar datos"+str(i+1)+"= ")) for i in range(self.n)]

class OpBasicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    
    def suma(self):
        a,b,=self.datos
        s= a + b
        print("El resultado de la suma es: ",s)
    
    def resta(self):
        a,b,=self.datos
        r=a-b
        print("El resultado de la resta es: ", r)
    
    def multiplicacion(self):
        a,b,=self.datos
        m= a * b
        print("El resultado de la multiplicacion es: ",m)
    
    def division(self):
        a,b,=self.datos
        d=a/b
        print("El resultado de la division es: ",d)

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    
    def raizCuadrada(self):
        import math
        a, = self.datos
        print("El resultado es: ",math.sqrt(a))

ejemplo=OpBasicas()
print(ejemplo.ingresarDato())
print(ejemplo.suma())
ejemplo2=Raiz()
print(ejemplo2.ingresarDato())
print(ejemplo2.raizCuadrada())

print(isinstance(ejemplo,OpBasicas))#isinstance verifica que el objeto este trabajando
print(isinstance(ejemplo2,OpBasicas))#con el metodo seleccionado, con true o false
print(issubclass(Raiz,Calculadora))#issubclass verifica que la subclase pertenezca
print(issubclass(OpBasicas,Raiz))#a la clase madre, devuelve true o false