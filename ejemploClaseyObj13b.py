#metodos Clase y Estaticos
#Instancia: Un objeto se crea usando el constructor
# de una clase
#Una vez que el objeto es creado
#se lo conoce como una instancia de la clase

#Tipos de metodos:
#*Metodos Estaticos
#*Metodos Clase
#*Metodos Instancia

#*Metodo Estatico
#*@staticmethod
#*Pueden ser llamados sin tener una instancia
#*de la clase, ademas este tipo de metodos
#*no tienen acceso al exterior
#*Por lo cual no pueden acceder a ningun otro
#*Atributo o llamar a ninguna otra funcion dentro
#*de la clase
import math
class Pastel:
    def __init__(self,ingredientes,tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    def __repr__(self):
        return(f"Pastel({self.ingredientes},"f"{self.tamaño})")
    def area(self):
        return self.tamaño_area(self.tamaño)
    @staticmethod
    def tamaño_area(A):
        return A ** 2 *math.pi  # los 2 ** significa igual igual es lo mismo que ==

nuevo_pastel= Pastel(["Harina","Huevo","Azucar","Leche","Limon"],4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño_area(12))
