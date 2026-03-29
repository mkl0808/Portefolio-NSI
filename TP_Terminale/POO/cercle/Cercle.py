import math

class Cercle :
    __rayon=0.0
    __centre=(0.0, 0.0)
    
    def __init__(self, rayon, centre):
        self.__rayon=rayon
        self.__centre=centre
        
    def perimetre(self):
        return 2*math.pi*self.__rayon
    
    def surface(self):
        return math.pi*self.__rayon**2
    
    def testAppartenance(self, cercle):
        return (cercle[0]-self.__centre[0])**2+(cercle[1]-self.__centre[1])**2 == self.__rayon**2