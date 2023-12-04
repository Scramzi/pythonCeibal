class Tablet:
    def __init__(self, bateria):
        self.bateria = bateria
    
    def utilizar(self, tiempo):
        if tiempo == 60:  
            self.bateria -= 30
        elif tiempo == 30:  
            self.bateria -= 15
        elif tiempo == 50: 
            self.bateria -= 25
        
        if self.bateria < 0:
            self.bateria = 0
    
    def tiene_bateria(self):
        return self.bateria > 20

    def tiene_bateria_maxima(self):
        return self.bateria == 100
    
    def cargar_a_tope(self):
        self.bateria = 100

    

mi_tablet = Tablet(100) # creas la tablet con 100 bateria.
mi_tablet.utilizar(60)  # uso de la tablet, 60 min, 30 min, etc.
print(mi_tablet.bateria) # bateria restante.