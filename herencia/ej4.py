class Dispositivo:
    def __init__(self, bateria):
        self.bateria = bateria
    
    def tiene_bateria(self):
        return self.bateria > 20

    def tiene_bateria_maxima(self):
        return self.bateria == 100
    
    def cargar_a_tope(self):
        self.bateria = 100
        
class Tablet(Dispositivo):
    def utilizar(self, tiempo):
        if tiempo == 60:  
            self.bateria -= 30
        elif tiempo == 30:  
            self.bateria -= 15
        elif tiempo == 50: 
            self.bateria -= 25
        
        if self.bateria < 0:
            self.bateria = 0

class Notebook(Dispositivo):
    def utilizar(self, tiempo):
        if tiempo == 30:  
            self.bateria -= 30
        elif tiempo == 50:  
            self.bateria -= 50
        elif tiempo == 60: 
            self.bateria -= 60

        if self.bateria < 0:
            self.bateria = 0