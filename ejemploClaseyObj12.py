#f-strings
#fomart %
# distintas formas de escribir rapido
#nombre = "Lucas"
#edad = 30
#print("Hola soy {} y mi edad es {} años.".format(nombre,edad))
#print("Hola soy, % s y tengo % s  años."%(nombre,edad))
#print(f"Hola soy {nombre} y mi edad es de: {edad} años")

class Estudiantes:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):#metodo para printear solamente 
        return f"Buenas!!! mi nombre y Apellido son: {self.nombre} {self.apellido} y mi edad es de: {self.edad}"
    def __repr__(self):#metodo para devolver valores reales
        return f"Buenas!!! mi nombre y Apellido son: {self.nombre} {self.apellido} y mi edad es de: {self.edad}"


nuevoEstudiante=Estudiantes("Lucas","Metrebian",30)
print(f"{nuevoEstudiante}")
print(f"{nuevoEstudiante !r}")
