import matplotlib.pyplot as plt
import math

def n_suiv(s):
    """
    Renvoie le nombre suivant de celui représenté par s
    en appliquant le procédé de lecture de la suite de Conway.

    Paramètre :
    s (str) : nombre sous forme de chaîne de caractères

    Retour :
    str : nombre suivant sous forme de chaîne de caractères
    """
    result = ''                                         # Chaîne qui contiendra le résultat final
    i = 0                                               # Indice de parcours de la chaîne s

    while i < len(s):                                   # Parcours de la chaîne caractère par caractère
        occurence = 1                                   # Compte le nombre de fois où le caractère courant se répète
        while i + 1 < len(s) and s[i] == s[i+1]:        # Tant que le caractère suivant est identique
            occurence += 1                              # On augmente le compteur
            i += 1                                      # On avance dans la chaîne
        result += str(occurence) + s[i]                 # Ajoute le nombre d'occurrences suivi du chiffre lu
        i += 1                                          # On avance dans la chaîne
    return result                                       # On renvoie le nombre obtenu

s = '1211'
print(n_suiv(s))


def nb_suiv_N(s, N):
    """
    Renvoie le nombre obtenu après N étapes de la suite de Conway.

    Paramètres :
    s (str) : nombre de départ sous forme de chaîne de caractères
    N (int) : nombre d'étapes à effectuer

    Retour :
    str : nombre obtenu après N transformations
    """
    for i in range(N):                                  # Applique N fois la fonction n_suiv
        s = n_suiv(s)                                   # Met à jour s à chaque étape
    return s                                            # Renvoie le résultat final

print(nb_suiv_N('1', 3))


def anagrammes(mot, prefixe=""):
    """
    Affiche tous les anagrammes possibles d’un mot
    à l’aide d’une fonction récursive.

    Paramètres :
    mot (str) : mot dont on veut afficher les anagrammes
    prefixe (str) : début de l’anagramme en cours de construction
    """
    if len(mot) == 0:                                               # Si le mot est vide, on a trouvé un anagramme complet
        print(prefixe)                                              # On affiche l’anagramme
    else:
        for i in range(len(mot)):                                   # On parcourt toutes les lettres du mot
            anagrammes(mot[:i] + mot[i+1:], prefixe + mot[i])       # Appel récursif en retirant la lettre choisie
            
print(anagrammes('acb'))


def binaire(n):
    """
    Renvoie la représentation binaire d’un entier strictement positif
    sous forme de liste de chiffres.

    Paramètre :
    n (int) : entier strictement positif

    Retour :
    list : liste contenant les chiffres de l’écriture binaire de n
    """
    if n == 0:                                             # Cas de base : si n vaut 0, on renvoie une liste vide
        return []
    return binaire(n // 2) + [n % 2]                       # Appel récursif sur le quotient et ajout du reste (0 ou 1)

print(binaire(13))


def carreDroit(n):
    """
    Trace un carré droit centré en (0, 0) dont la demi-longueur du côté est n,
    puis appelle récursivement la fonction carrePenche pour tracer le carré
    penché inscrit.

    Paramètre
    ---------
    n : float
        Demi-longueur du côté du carré droit.
        La récursion s'arrête lorsque n devient inférieur à 1.
    """
    if n < 1:                      # condition d'arrêt, si le carré devient trop petit
        return                     # sert a terminer la fonction si la condition d'arrêt est respectée    
    x = [-n, n, n, -n, -n]         # coordonnées du carré droit 
    y = [-n, -n, n, n, -n]
    plt.plot(x, y)                 # trace le carré avec matplotlib
    carrePenche(n)                 # appel récursif de l'autre fonction pour la récursion mutuelle


def carrePenche(n):
    """
    Trace un carré penché (losange) centré en (0, 0) dont les sommets sont
    situés sur les axes, à une distance n du centre.
    Appelle ensuite récursivement la fonction carreDroit pour tracer
    le carré droit inscrit.

    Paramètre
    ---------
    n : float
        Distance du centre aux sommets du carré penché.
        La récursion s'arrête lorsque n devient inférieur à 1.
    """
    if n < 1:                      # condition d'arrêt, si le carré devient trop petit
        return                     # sert a terminer la fonction si la condition d'arrêt est respectée  
    x = [0, n, 0, -n, 0]           # coordonnées du carré penché
    y = [-n, 0, n, 0, -n]
    plt.plot(x, y)                 # trace le carré penché avec matplotlib
    carreDroit(n / 2)              # appel récursif de l'autre fonction avec n/2 pour que la taille diminue de moitié

plt.figure(figsize=(6, 6))         # crée une figure matplotlib de 6 pouces de hauteur et 6 pouces de largeur
carreDroit(8)                      # lance le dessin, 8 est la demi longueur du premier carré
plt.axis("equal")                  # force la même échelle sur les axes x et y
plt.show()                         # affiche la figure à l'écran


def carre(n):
    """
    Trace récursivement une suite de carrés imbriqués :
    un carré droit suivi d'un carré penché,
    tous deux centrés en (0, 0).

    À chaque appel récursif, la taille du carré est divisée par 2,
    jusqu'à ce que la valeur de n devienne inférieure à 1.

    Paramètre
    ---------
    n : float
        Demi-longueur du côté du premier carré droit.
    """
    if n < 1:                      # condition d'arrêt, si le carré devient trop petit
        return                     # sert a terminer la fonction si la condition d'arrêt est respectée
    x_d = [-n, n, n, -n, -n]       # coordonnées du carré droit
    y_d = [-n, -n, n, n, -n]
    plt.plot(x_d, y_d)             # trace le carré droit avec matplotlib
    x_p = [0, n, 0, -n, 0]         # coordonnées du carré penché
    y_p = [-n, 0, n, 0, -n]
    plt.plot(x_p, y_p)             # trace le carré penché avec matplotlib
    carre(n / 2)                   # appel récursif avec la taille divisée par 2

plt.figure(figsize=(6, 6))         # crée une figure matplotlib de 6 pouces de hauteur et 6 pouces de largeur
carre(8)                           # lance le dessin, 8 est la demi longueur du premier carré
plt.axis("equal")                  # force la même échelle sur les axes x et y                  
plt.show()                         # affiche la figure à l'écran


def flocon_koch(x, y, angle, longueur, n):
    if n == 0:                                                                  # Cas de base : on trace un segment simple
        x2 = x + longueur * math.cos(angle)
        y2 = y + longueur * math.sin(angle)
        plt.plot([x, x2], [y, y2], 'k')                                         # Dessin du segment
        return x2, y2, longueur, 0                                              # On renvoie la position finale, la longueur tracée et aucune aire ajoutée
    longueur /= 3                                                               # On divise la longueur du segment par 3
    x, y, L1, A1 = flocon_koch(x, y, angle, longueur, n - 1)                    # Premier segment
    x, y, L2, A2 = flocon_koch(x, y, angle + math.pi / 3, longueur, n - 1)      # Deuxième segment (rotation +60°)
    x, y, L3, A3 = flocon_koch(x, y, angle - math.pi / 3, longueur, n - 1)      # Troisième segment (rotation -120°)
    x, y, L4, A4 = flocon_koch(x, y, angle, longueur, n - 1)                    # Quatrième segment
    aire = (math.sqrt(3) / 4) * longueur ** 2                                   # Aire du petit triangle ajouté à cette étape
    longueur_totale = L1 + L2 + L3 + L4                                         # Somme des longueurs
    aire_totale = A1 + A2 + A3 + A4 + aire                                      # Somme des aires
    return x, y, longueur_totale, aire_totale                                   # Renvoie la position finale du tracé ainsi que la longueur et la surface du flocon à l’étape n

x, y = 0, 0                                                     # Point de départ
L = 1                                                           # Longueur du côté initial
N = 4
x, y, L1, A1 = flocon_koch(x, y, 0, L, N)                       # Tracé des 3 côtés du triangle (flocon)
x, y, L2, A2 = flocon_koch(x, y, -2 * math.pi / 3, L, N)
x, y, L3, A3 = flocon_koch(x, y, 2 * math.pi / 3, L, N)
plt.axis('equal')                                               # force la même échelle sur les axes x et y
plt.show()                                                      # affiche la figure à l'écran

# Calcul final
longueur = L1 + L2 + L3
surface = (math.sqrt(3) / 4) * L ** 2 + A1 + A2 + A3
print("Longueur :", longueur)
print("Surface :", surface)