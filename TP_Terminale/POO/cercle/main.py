from Cercle import Cercle
from Cylindre import Cylindre
if __name__=='__main__':
    cercle=Cercle(3.0, (4, 5))
    cylindre=Cylindre(cercle, 2.0)
    print(str(cercle.perimetre())+'m')
    print(str(cercle.surface())+'m²')
    print(str(cylindre.Volume())+'m3')
    if cercle.testAppartenance((1, 5)):
        print('Le point appartient au cercle')
    else :
        print("Le point n'appartient pas au cercle")