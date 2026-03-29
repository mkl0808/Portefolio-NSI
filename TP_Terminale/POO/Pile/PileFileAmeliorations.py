class PileFileAmeliorations :
    __liste = []
    
    def __init__(self):
        self.__liste = []
        
    def estVide(self):
        if len(self.__liste) == 0 :
            return True
        else:
            return False
        
        
    def empiler(self, element):
        self.__liste.append(element)
        
    def depiler(self):
        if not self.estVide():
            last = self.__liste[len(self.__liste)-1]
            self.__liste.pop() 
            return last
        else:
            print("La pile est vide")
            
    def enfiler(self, element):
        self.__liste.append(element)
            
    def defiler(self):
        if not self.estVide():
            first = self.__liste[0]
            self.__liste.pop(0)
        else:
            print("La file est vide")
            
    def taille(self):
        return len(self.__liste)
            
    def afficher(self):
        print (self.__liste)
        

