#Metodos

class Calculadora:
    def __init__(self,n1,n2):
        self.suma= n1 + n2
        self.resta= n1 - n2
        self.producto= n1 * n2
        self.division= n1 / n2

operacion =Calculadora(2,3)    
print(operacion.suma)
print(operacion.resta)
print(operacion.producto)
print(operacion.division)
