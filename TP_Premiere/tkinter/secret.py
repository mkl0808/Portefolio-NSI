from tkinter import *
import random
secret=random.randint(1,100)

def verifier(event=None):
    if int(saisie.get()) == secret:
        affichage.set("Bravo tu as trouvé")
    elif int(saisie.get()) < secret:
        affichage.set("Trop petit")
    else:
        affichage.set("Trop grand")

fenetre = Tk()
fenetre.geometry("400x300")
fenetre.title('Nombre secret')

label = Label(fenetre, text="Trouve le nombre secret entre 1 et 100", fg="RoyalBlue1")
label.pack(padx=90, pady=60)

affichage = StringVar()
label = Label(fenetre, textvariable=affichage, width=50, fg='black')
label.pack()

saisie = StringVar()
entree = Entry(fenetre, textvariable=saisie, width=20)
entree.pack()
entree.focus_set()

bouton_fermer = Button(fenetre, text="Fermer", command=fenetre.destroy)
bouton_fermer.pack(side=BOTTOM)

bouton_verifier = Button(fenetre, text="Vérifier", command=verifier)
bouton_verifier.pack(side=BOTTOM)
fenetre.bind('<Return>', verifier)

fenetre.mainloop()