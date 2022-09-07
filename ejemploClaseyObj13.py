#metodos Clase y Estaticos
#Instancia: Un objeto se crea usando el constructor
# de una clase
#Una vez que el objeto es creado
#se lo conoce como una instancia de la clase

#Tipos de metodos:
#*Metodos Estaticos
#*Metodos Clase
#*Metodos Instancia

#METODOS CLASE 
#@classmethod
#este metodo puede ser llamado sin crear
#un instancia de la clase
#Es decir no se utiliza __init__

class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes=ingredientes
    
    def __repr__(self):
        return f"pastel({self.ingredientes !r}"
    @classmethod

    def Pastel_chocolate(cls):
        return cls(["Harina","Leche","Chocolate"])

    @classmethod

    def Pastel_vainilla(cls):
        return cls(["Harina","Leche","Vainilla"])

print(Pastel.Pastel_chocolate())
print(Pastel.Pastel_vainilla())
