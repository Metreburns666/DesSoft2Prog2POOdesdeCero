#Herencia

# class NombreSubClase(NombreClaseSuperior):
# class ClaseBase:
#       Cuerpo de la clase Base
# class DerivadoClase(ClaseBase):
#       Cuerpo de la clase derivada

class Pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre= nombre
        self.tipo= tipo
    def descripcion(self):
        return "{} Es un Pokemon de tipo: {}".format(self.nombre,self.tipo)
class Pikachu(Pokemon):
    def ataque(self,tipoAtaque):
        return"{} Tipo de Ataque: {}".format(self.nombre,tipoAtaque)

class Charmander(Pokemon):
    def ataque(self,tipoAtaque):
        return"{} Tipo de Ataque: {}".format(self.nombre,tipoAtaque)

newPokemon=Pikachu("Chispita","Electrico")
newPokemon2=Charmander("Flama","Fuego")
print(newPokemon.descripcion())
print(newPokemon.ataque("Rayo"))
print(newPokemon2.descripcion())
print(newPokemon2.ataque("Llamarada"))

