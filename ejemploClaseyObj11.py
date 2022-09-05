#Herencia Multiple

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("Llamando...")
    def ocupado(self):
        print("Ocupado...")
class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("Tomando Fotos...")
class Reproduccion:
    def __init__(self):
        pass
    def reproducirAudio(self):
        print("Reproduciendo Audio...")
    def reproducirVideo(self):
        print("Reproducir Video...")

class Smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print("Telefono Apagado")

nokia=Smartphone()
#print(dir(nokia))#el termino dir permite ver todas las acciones que puede realizar la var
print(nokia.llamar())
print(nokia.reproducirVideo())
