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
        super().__init__(combustible=100)
        self.pasajeros = 0
        
    
    def cargar_combustible(self, litros):
        super().cargar_combustible(litros)
        self.combustible += 0
        self.pasajeros = 0
        

    def entran_personas(self, cantidad):
        return cantidad >= 0

    def recorrer(self, cantidad):
        self.combustible -= cantidad * 2

# tests
print(Auto.entran_personas(4, 2)) # false
print(Auto.entran_personas(4, 7)) # false
print(Moto.entran_personas(4, 1)) # true
print(Moto.entran_personas(4, 4)) # false