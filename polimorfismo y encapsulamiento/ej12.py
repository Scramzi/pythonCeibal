class Chef:
    def __init__(self, plato_del_dia):
        self.plato_del_dia = plato_del_dia
 
    def picantear(self):
        if self.plato_del_dia.puede_picantear():
            self.plato_del_dia.picantear()              
        else:
            raise Exception ('El plato ya está demasiado picante.')
 
# AYUDANTE
class AyudanteDeCocina:
    def suavizar(self, plato_del_dia):
            plato_del_dia.suavizar()
 
 
# PIZZA
class Pizza(Chef):
    def __init__(self):
        self.condimento = "adobo"
 
    def puede_picantear(self):
        return self.condimento != "cayena"
 
    def picantear(self):
        if self.puede_picantear():
            self.condimento = "cayena"
 
    def suavizar(self):
        self.condimento = "oregano"
 
# PASTA
class Pasta(Chef):
    def __init__(self):
        self.ajies = 0
 
    def puede_picantear(self):
        return self.ajies < 10
 
    def picantear(self):
        self.ajies += 5
 
    def suavizar(self):
        if self.ajies > 0:
            self.ajies -= 1