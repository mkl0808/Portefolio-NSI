from tkinter import *


def afficher():
    """
    Affiche "Bonjour ", renvoie la valeur de la variable saisie et affiche "!"
    """
    global affichage, saisie
    affichage.set("Bonjour " + saisie.get() + " !")


fenetre = Tk()
fenetre.title("Salutations")

# Étiquette permettant d'afficher les instructions
texte = Label(fenetre, text='Comment vous appelez-vous ?', height=3)
texte.pack()

# Stockage de la réponse texte dans la variable affichage
affichage = StringVar()
# Définition de la fenêtre : largeur de la fenêtre, couleur du fond où sera affiché la réponse et couleur du texte
label = Label(fenetre, textvariable=affichage, width=50, fg='black', bg='white')
label.pack()

# Stockage de la réponse texte dans la variable saisie
saisie = StringVar()
# Définition de la barre où l'utilisateur saisie le texte
entree = Entry(fenetre, textvariable=saisie, width=20)
entree.pack()

# Bouton "Afficher"
bouton_afficher = Button(fenetre, text='Afficher', command=afficher)
bouton_afficher.pack()

# Gestionnaire d'événements
fenetre.mainloop()
