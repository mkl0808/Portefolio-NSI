import turtle
import aide

def positionner(x, y):
    #Positionne la tortue dans aux coordonnées (x, y)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def mur(x, y, largeur, hauteur):
    """
    Dessine le mur d'une maison.

    x       -- position x du coin inférieur gauche du mur
    y       -- position y du coin inférieur gauche du mur
    largeur -- largeur du mur
    hauteur -- hauteur du mur
    """
    # Implémenter le tracé ici
    positionner(x, y)                     # Positionnement de la tortue au point A
    turtle.goto(x, y + hauteur)           # Tracé du segment AB
    turtle.goto(x + largeur, y + hauteur) # Tracé du segment BC
    turtle.goto(x + largeur, y)           # Tracé du segment CD
    turtle.goto(x, y)                     # Tracé du segment DA

def toit(x, y, base, hauteur):
    """
    Dessine le toit d'une maison.

    x       -- position x du coin inférieur gauche du toit
    y       -- position y du coin inférieur gauche du toit
    base    -- largeur de la base du toit
    hauteur -- hauteur du toit
    """
    # Implémenter le tracé ici
    positionner(x, y)
    turtle.goto(x + base/2, y + hauteur) #Tracé du segment AB
    turtle.goto(x + base, y)             #Tracé du segment BC
    turtle.goto(x, y)                    #Tracé du segment CA

    


def maison(x, y):
    """
    Dessine une maison de 200px de largeur. Le mur fait 100px de hauteur et le toit, 50px de hauteur.

    x -- position x du coin inférieur gauche de la maison
    y -- position y du coin inférieur gauche de la maison
    """
    #Dimensions de la maison
    largeur = 200
    hauteur_mur = 100
    hauteur_toit = 50
    
    #Tracé de la maison
    mur(x, y, largeur, hauteur_mur)                 #Tracé du mur
    toit(x, y + hauteur_mur, largeur, hauteur_toit) #Tracé du toit
    


def dessiner_paysage():
    """Dessine un paysage de 3 maisons sous Turtle."""
    

# Tests
if __name__ == "__main__":
    aide.grille()
    mur(-300, 0, 200, 100)
    toit(-300, 150, 200, 50)
    maison(0, 0)
    turtle.mainloop()
