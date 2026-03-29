from Rectangle import Rectangle
from Rectangle import Parallelepipede
if __name__=='__main__':
    rect=Rectangle(4.5,5.5)
    parallelepipede=Parallelepipede(rect, 2)
    print(str(rect.perimetre())+'m')
    print(str(rect.surface())+'m²')
    print(str(parallelepipede.Volume())+'m3')
    