from PileFile import PileFile
from arbre_eleve import arbre
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20, 6)

if __name__ == "__main__":
    a = [5,[3,[4,[2,[],[]],[1,[],[]]],[6,[7,[10,[],[]],[11,[],[]]],[8,[],[]]]],[2,[],[]]]
    b = [1,[2,[4,[8,[],[]],[9,[],[]]],[5,[10,[],[]],[]]],[3,[6,[],[]],[7,[],[]]]]
    c = [2, [1, [0, [], []], []], [5, [4, [3, [], []], []], [12,[9, [8, [6, [], [7, [], []]], []], [10, [], [11, [], []]]], [13, [], [14, [], [18, [17, [15, [], [16, [], []]],[]], [19, [], []]]]]]]]
    d = [20,[5,[3,[],[]],[12,[8,[6,[],[]],[]],[13,[],[]]]],[25,[21,[],[]],[28,[],[]]]]
    e = ["moi", ["père", ["grand-père_paternel", [], []], ["grand-mère_paternelle", [], []]], ["mère", ["grand-père_maternel", [], []], ["grand-mère_maternelle", [], []]]]

    
    arbre = arbre()

    noms = ["a", "b", "c", "d", "e"]
    arbres = [a, b, c, d, e]
    

    for i in range(len(noms)):
        print("Arbre " + noms[i] + ":")
        print("- Taille:", arbre.taille(arbres[i]))
        print("- Hauteur:", arbre.hauteur(arbres[i]))
        print("- Est vide:", arbre.est_vide(arbres[i]))
        print()
#        arbre.dessiner(arbres[i])
        
        print('Parcours par largeur :', arbre.parcours_largeur(arbres[i]))
        print()
        
        print('Parcours par profondeur :', arbre.parcours_profondeur(arbres[i]))
        print()

        print('Parcours par profondeur récursif préfixe :', arbre.parcours_profondeur_recursif_prefixe(arbres[i]))
        print()
        
        print('Parcours par profondeur récursif infixe :', arbre.parcours_profondeur_recursif_infixe(arbres[i]))
        print()
        
        print('Parcours par profondeur récursif postfixe :', arbre.parcours_profondeur_recursif_postfixe(arbres[i]))
        print()
        
        

        
    