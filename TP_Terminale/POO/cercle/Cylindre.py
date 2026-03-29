import math
from Cercle import Cercle

class Cylindre(Cercle) :
    __cercle=Cercle(0.0, 0.0)
    __hauteur=0.0
    def __init__(self, cercle, hauteur):
        self.__cercle=cercle
        self.__hauteur=hauteur
        
    def Volume(self):
        return self.__cercle.surface()*self.__hauteur