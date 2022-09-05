#Funciones para Atributos

class Persona:
    edad=27
    nombre= "Victor"
    pais="Brasil"

doctor=Persona()
print("La edad es: ",doctor.edad)
print("La edad es: ",getattr(doctor,"edad"))#getattr te trae el valor en especifico de un objeto"
print("El doctor tiene una edad?",hasattr(doctor,"edad"))#hasattr devuelve true or false
print("El doctor tiene un apellido?",hasattr(doctor,"apellido"))#hasattr si existe el valor o no
print("antes era: ",doctor.nombre)
setattr(doctor,"nombre","Lucas")#setattr sirve para cambiar el valor de un atributo en un obj
print("ahora es: ",doctor.nombre)
delattr(Persona,"pais")#delattr sirve para eliminar un atributo de una Clase.
