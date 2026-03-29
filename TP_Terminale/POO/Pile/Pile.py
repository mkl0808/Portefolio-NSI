class Pile :
    __liste = []
    __taille = 0
    
    def __init__(self, taille):
        self.__taille = taille
        self.__liste = [None] * self.__taille
    
    def estPleine(self):
        for element in self.__liste:
            if element is None:
                return False
        return True
        
    def estVide(self):
        for element in self.__liste:
            if element is not None:
                return False
        return True
        
    def empiler(self, element):
        if not self.estPleine():
            for indice in range(self.__taille):
                if self.__liste[indice] == None:
                    self.__liste[indice] = element
                    break
        else:
            print("La liste est pleine")
                
        
    def depiler(self):
        if not self.estVide():
            for indice in range(self.__taille):
                if self.__liste[indice] == None:
                    last = self.__liste[indice - 1]
                    self.__liste[indice - 1] = None
                    break
            return last
        else :
            print("La liste est vide")
    
    def afficher(self):
        print (self.__liste)
        