from CompteBancaire import CompteBancaire

if __name__ == "__main__":
    compte = CompteBancaire(2579, 'Mickael Mai-Emery', 500.0)
    compte.afficher()
    compte.versement(500)
    compte.retrait(200)
    compte.retrait(2000)
    compte.agios()
    compte.changeTaux(0.05)
    compte.capitalisation(6)
    compte.afficher()