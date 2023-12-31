class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible

    def cargar_combustible(self, litros):
        self.combustible += litros
   
    def entran_personas(self, cantidad):
        return cantidad > 0 and cantidad <= self.maximo_personas()


class Auto(MedioDeTransporte):
    def maximo_personas(self):
        return 5

    def recorrer(self, cantidad):
        self.combustible -= cantidad / 2


class Moto(MedioDeTransporte):
    def maximo_personas(self):
        return 2

    def recorrer(self, cantidad):
        self.combustible -= cantidad

class Colectivo(MedioDeTransporte):
    def __init__(self, pasajeros):
        self.pasajeros = pasajeros

    def entran_personas(self, cantidad):
        return cantidad <= 0
        


# tests
print(Auto.entran_personas(4, 2)) # false
print(Auto.entran_personas(4, 7)) # false
print(Moto.entran_personas(4, 1)) # true
print(Moto.entran_personas(4, 4)) # false