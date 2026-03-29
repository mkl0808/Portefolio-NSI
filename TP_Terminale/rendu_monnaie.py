def rendu_monnaie(prix, montant):
    rendu = []
    monnaie = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    if montant == prix :
        return 0
    if montant < prix :
        print("Vous n'avez pas mis assez d'argent")
    else:
        a_rendre = montant - prix
        for v in monnaie :
            while v <= a_rendre:
                rendu.append(v)
                a_rendre -= v
        return rendu
    
print(rendu_monnaie(200, 2968))