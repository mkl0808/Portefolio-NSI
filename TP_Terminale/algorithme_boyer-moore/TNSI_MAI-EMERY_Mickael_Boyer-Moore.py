# -*- coding: utf-8 -*-
"""
Éditeur de Spyder


"""
import timeit


def rechStupide(texte, motif):
    for i in range(len(texte)-len(motif)):
        isPres = True
        for j in range(len(motif)):
            if(texte[i+j] == motif[j]):
                isPres = True and isPres
            else:
                isPres = False and isPres
        if(isPres):
            return True
    return isPres

def calculADroite(motif):
    """
    Construit le dictionnaire des positions les plus à droite
    de chaque caractère du motif.

    Le dictionnaire associe à chaque caractère la dernière position
    (la plus à droite) où il apparaît dans le motif. Si un caractère apparaît 
    plusieurs fois, seule sa position la plus à droite est conservée.

    Arguments
    ----------
    motif : str
        Le motif dont on veut analyser les caractères.

    Returns
    -------
    dict
        Un dictionnaire où chaque clé est un caractère du motif,
        et chaque valeur est son indice le plus à droite.
    """
    aDroite = {}                   # création du dictionnaire aDroite vide
    for i in range(len(motif)):    # parcours du motif de l'indice 0 à len(motif)-1
        aDroite[motif[i]] = i      # On assigne à chaque caractère sa position actuelle i. Si le caractère apparaît plusieurs fois, la dernière position (la plus à droite) reste.
    return aDroite                 # on retourne le dictionnaire contenant la position la plus à droite de chaque caractère

def droite(c, aDroite):
    """
    Renvoie la position la plus à droite du caractère c dans le motif,
    à partir du dictionnaire aDroite construit par calculADroite.

    Arguments
    ----------
    c : str
        Le caractère recherché dans le dictionnaire.
    aDroite : dict
        Le dictionnaire contenant les positions les plus à droite des caractères.

    Returns
    -------
    int
        La position du caractère dans le motif si c est présent.
        -1 si le caractère n'est pas dans le motif.
    """
    if c in aDroite:               # vérification de la présence du caractère dans le dictionnaire aDroite
        return aDroite[c]          # si le caractère est présent on renvoie sa position la plus à droite dans le motif
    else:                      
        return -1                  # sinon on retourne -1 pour indiquer que le cractère n'est pas présent dans le motif.
    
def decalage(j, c, aDroite):
    """
    Calcule le décalage à appliquer
    - Si le caractère c ne figure pas dans le motif, le décalage est j + 1.
    - Si c apparaît dans le motif à la position r (la plus à droite),
      alors le décalage est d = j - r.
      Si d <= 0, on renvoie 1.

    Arguments
    ----------
    j : int
        L'indice du motif où la comparaison a échoué.
    c : str
        Le caractère du texte qui ne correspond pas.
    aDroite : dict
        Le dictionnaire renvoyé par calculADroite.

    Returns
    -------
    int
        Le décalage calculé
    """
    r = droite(c, aDroite)         # on utilise la fonction droite pour obtenir la position la plus à droite du caractère dans la variable r
    if r == -1 :                   # si le caractère n'est pas dans le motif
        return j + 1               # si c n'apparait pas dans le motif on décale de j + 1 pour passer au prochain caractère
    else :
        d = j - r                  # sinon on donne j - r a la variable d dès le début
        if d <= 0:                 # ensuite on vérifie le signe de d
            return 1               # si d est négatif alors d prendra la valeur 1
        else:
            return d               # sinon on retourne d qui était déjà j - r (du coup si d est positif)
            
def cherche_BoyerMoore(texte, motif):
    """
    Recherche un motif dans un texte
    en utilisant l'algorithme de Boyer-Moore-Horspool.

    Les comparaisons se font de droite à gauche dans le motif.
    Les décalages sont calculés grâce à la fonction decalage.

    Arguments
    ----------
    texte : str
        Le texte dans lequel on cherche le motif.
    motif : str
        Le motif à rechercher.

    Returns
    -------
    list
        La liste des indices où le motif est trouvé dans le texte.
        Liste vide si aucune occurrence n'est trouvée.
    """
    n = len(texte)                                      # longueur du texte
    m = len(motif)                                      # longueur du motif
    aDroite = calculADroite(motif)                      # on construit le dictionnaire des positions les plus à droite pour chaque caractère du motif.
    positions = []                                      # liste pour stocker les positions où le motif est trouvé
    i = 0                                               # position actuelle dans le texte
    while i <= n - m:                                   # tant que le motif peut tenir dans le texte
        j = m - 1                                       # j correspond à l'indice du caractère qu'on va comparer dans le motif (le dernier caractère du motif)
        while j >= 0 and motif[j] == texte[i + j]:      # Tant que j n’est pas négatif (0 est le premier indice) et que le caractère du motif (motif[j]) correspond au caractère du texte (texte[i+j])
            j -= 1                                      # On passe au caractère précédent du motif
        if j < 0:                                       # si un motif a été trouvé (tous les caractères du motif ont correspondus)
            positions.append(i)                         # on ajoute la position a laquelle on a trouvé le motif dans la liste positions
            i += m                                      # on décale le motif de m pour ne pas avoir à vérifier des positions qui ne peuvent pas correspondre
        else:                                           # au moins un caractère ne correpspond pas
            d = decalage(j, texte[i + j], aDroite)      # calcul du décalage en utilisant la fonction decalage
#            print(f"décalage  de {d}")                  # affichage des décalages pour cette itération
            i += d                                      # on avance le motif dans le texte du nombre de position calculé
    return positions

def cherche_BoyerMoore_verb(texte, motif):
    """
    Version verbale de la recherche Boyer-Moore-Horspool.
    Renvoie la position de la première occurrence du motif
    et le nombre total de comparaisons effectuées.

    Arguments
    ----------
    texte : str
        Le texte dans lequel on effectue la recherche.
    motif : str
        Le motif recherché.

    Returns
    -------
    tuple (int, int)
        - La position où le motif est trouvé (ou -1 si absent)
        - Le nombre total de comparaisons effectuées
    """
    n = len(texte)                                      # longueur du texte
    m = len(motif)                                      # longueur du motif
    aDroite = calculADroite(motif)                      # on construit le dictionnaire des positions les plus à droite pour chaque caractère du motif.
    i = 0                                               # position actuelle dans le texte
    comparaisons = 0                                    # compteur de comparaisons
    while i <= n - m:                                   # tant que le motif peut tenir dans le texte
        j = m - 1                                       # j correspond à l'indice du caractère qu'on va comparer dans le motif (le dernier caractère du motif m-1)
        while j >= 0 and motif[j] == texte[i + j]:      # Tant que j n’est pas négatif (0 est le premier indice) et que le caractère du motif (motif[j]) correspond au caractère du texte (texte[i+j])
            comparaisons += 1                           # on ajoute 1 au compteur si la comparaison est réussie
            j -= 1                                      # On passe au caractère précédent du motif
        if j >= 0:                                      # Si j est encore positif, la boucle précédente s'est arrêtée car une comparaison a échouée
            comparaisons += 1                           # on ajoute 1 au compteur pour la dernière comparaison qui a échouée
        if j < 0:                                       # si un motif a été trouvé (tous les caractères du motif ont correspondus)
            return (i, comparaisons)                    # on renvoie la position où le motif a été trouvé et le nombre de comparaisons
        d = decalage(j, texte[i + j], aDroite)          # calcul du décalage en utilisant la fonction decalage
        i += d                                          # on avance le motif dans le texte du nombre de position calculé
    return (-1, comparaisons)                           # le motif est introuvable donc on retourne -1 pour indiquer que c'est introuvable et le nombre de comparaisons qui a été effectué.


texte = "Lorem ipsum ljdqnf msdnfm  jqfnmqj mjdlfn KQFNMLNC  lmksvdn mlkv psum ljdqnf msdnfm  jqfnmqj mjdlfn KQFNMLNC ùmkn:lkjn kln "
motif = "ùmkn:lkjn kln"


tic = timeit.default_timer()
print(rechStupide(texte,motif))
print(timeit.default_timer()-tic)

tic = timeit.default_timer()
print(cherche_BoyerMoore_verb(texte, motif))
print(timeit.default_timer()-tic)


print('')
print('Test de la fonction calculADroite')
aDroite = calculADroite(motif)
print('dictionnaire aDroite :', aDroite)


print('')
print('Test de la fonction droite')
c = 'n'
print(f"valeur contenue dans le dictionnaire pour '{c}' :", droite(c, aDroite))


print('')
print('Test de la fonction decalage')
j = 1
print(f"Décalage à appliquer pour le caractère '{c}' en position {j} :", decalage(j, c, aDroite))


print('')
print('Test de la fonction cherche_BoyerMoore')
positions = cherche_BoyerMoore(texte, motif)
if positions != [] :
    print("Motif trouvé aux positions :", positions)
else:
    print("Motif non trouvé dans le texte.")
    

print('')
print('Test de la fonction cherche_BoyerMoore_verb')
pos, comp = cherche_BoyerMoore_verb(texte, motif)
if pos != -1:
    print("Motif trouvé aux positions :", pos)
else:
    print("Motif non trouvé dans le texte.")
print("Nombre de comparaisons effectuées :", comp)
resultat = cherche_BoyerMoore_verb(texte, motif)
print("tuple retrouné par la fonction cherche_BoyerMoore_verb :", resultat)

