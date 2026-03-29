import turtle

def carre(longueur):
    i = 0
    while i < 4 :
        turtle.forward(longueur)
        turtle.left(90)
        i += 1
        
def triangle(longueur):
    i = 0
    while i < 3 :
        turtle.forward(longueur)
        turtle.left(240)
        i += 1
        
def polygone(n, longueur):
    i = 0
    while i < n :
        turtle.forward(longueur)
        turtle.right(360/n)
        i = i + 1

if __name__ == "__main__" :
    carre(50)
    triangle(50)
    polygone(6, 50)