#constructor

from mailbox import NoSuchMailboxError


class Persona:
    pass
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año

    def descripcion(self):#todos los metodos necesitan un self
        return "{} tiene {} años ".format(self.nombre,self.año)

    def comentario(self,frase):
        return "{} dice: {}".format(self.nombre,frase)

doctor=Persona("Lucas",25)
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario("Tengo hambre"))

