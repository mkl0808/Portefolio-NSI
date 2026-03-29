class CompteBancaire:
    __numeroCompte = 0
    __nom = ""
    __solde = 0.0
    __taux_interet = 0.03

    def __init__(self, numeroCompte, nom, solde):
        self.__numeroCompte = numeroCompte
        self.__nom = nom
        self.__solde = solde

    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print("Un versement de " + str(montant) + "€ a été effectué. Le nouveau solde est : " + str(self.__solde) + "€")
        else:
            print("Le montant du versement doit être positif.")

    def retrait(self, montant):
        if montant <= 0:
            print("Le montant du retrait doit être positif.")
        if self.__solde - montant < -500:
            print("Vous ne pouvez pas retirer ce montant car vous feriez un découvert supérieur à 500€")
        else:
            self.__solde -= montant
            print("Un retrait de " + str(montant) + "€ a été effectué. Le nouveau solde est : " + str(self.__solde) + "€")

    def agios(self):
        if self.__solde < 0:
            frais = abs(self.__solde) * 0.05
            self.__solde -= frais
            print("Des agios de " + str(frais) + "€ ont été appliqués. Le nouveau solde est : " + str(self.__solde) + "€")
        else:
            print("Il n'y a pas besoin d'Agios car le solde est positif")

    def changeTaux(self, nouveau_taux):
        if 0 < nouveau_taux < 1:
            self.__taux_interet = nouveau_taux
            print("Le nouveau taux d'intérêt est fixé à " + str(nouveau_taux * 100) + "%")
        else:
            print("Le taux doit être une valeur décimale comprise entre 0 et 1")

    def capitalisation(self, mois):
        if mois > 0:
            interets = self.__solde * ((1 + self.__taux_interet) ** mois - 1)
            self.__solde += interets
            print("Vous avez capitalisé sur " + str(mois) + " mois : Vous avez " + str(interets) + "€ d'intérêts. Le nouveau solde est : " + str(self.__solde) + "€")
        else:
            print("Le nombre de mois doit être positif.")

    def afficher(self):
        print("----- Détails du compte -----")
        print("Numéro de compte : " + str(self.__numeroCompte) )
        print("Titulaire        : " + str(self.__nom) )
        print("Solde            : " + str(self.__solde) + "€")
        print("Taux d'intérêt   : " + str(self.__taux_interet * 100) + "%")
