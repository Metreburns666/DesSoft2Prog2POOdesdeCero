#Metodo Constructor
#Modificar un Atributo


class Email:
    def __init__(self):#se le da un valor inicial de Falso al atributo
        self.enviado = False
    def enviarCorreo(self):# Se crea un metodo para cambiar el valor del atributo
        self.enviado = True

miCorreo = Email()# Se instancia el objeto
print(miCorreo.enviado)
miCorreo.enviarCorreo()#Aca se llama al metodo para cambiar el valor del atributo del objeto
print(miCorreo.enviado)
