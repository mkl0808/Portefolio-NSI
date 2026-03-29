class Rectangle :
    __longueur=0.0
    __largeur=0.0
    def __init__(self, lar, lon):
        self.__longueur=lon
        self.__largeur=lar
        
    def perimetre(self):
        return (self.__largeur+self.__longueur)*2
    
    def surface(self):
        return self.__largeur*self.__longueur
    
class Parallelepipede(Rectangle):
    __rect=Rectangle(0.0,0.0)
    __hauteur=0.0
    def __init__(self, rect, hauteur):
        self.__rect=rect
        self.__hauteur=hauteur
        
    def Volume(self):
        return self.__rect.surface()*self.__hauteur