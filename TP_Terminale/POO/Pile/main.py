from Pile import Pile
from PileFile import PileFile
from PileFileAmeliorations import PileFileAmeliorations

if __name__ == '__main__':
    
    print('test de la classe Pile')
    liste = Pile(5)
    liste.empiler(5)
    liste.empiler(6)
    valeur_depilee = liste.depiler()
    liste.empiler(8)
    liste.empiler(9)
    liste.empiler(1)
    liste.afficher()
    print('La valeur dépilée est : ', valeur_depilee)
    
    print('test de la classe PileFile')
    liste2 = PileFile(5)
    liste2.enfiler(5)
    liste2.enfiler(6)
    f0 = liste2.defiler()
    liste2.enfiler(8)
    liste2.enfiler(9)
    f1 = liste2.defiler()
    liste2.afficher()
    print('La valeur f0 =', f0, ' et la valeur f1 =', f1)
    
    print('test de la classe PileFileAmeliorations')
    liste3 = PileFileAmeliorations()
    if liste3.estVide():
        print("La liste est vide")
    else:
        print("La liste n'est pas vide")
    liste3.empiler(1)
    liste3.enfiler(2)
    liste3.empiler(3)
    liste3.enfiler(4)
    liste3.empiler(5)
    liste3.enfiler(6)
    liste3.depiler()
    liste3.defiler()
    liste3.afficher()
    if liste3.estVide():
        print("La liste est vide")
    else:
        print("La liste n'est pas vide")
    
    
    
    