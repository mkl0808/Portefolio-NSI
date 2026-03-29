def generer_plateau():
    """
    Génère un plateau de jeu vide.
    Renvoie un tableau doublement indexé de taille 3x3 ne contenant que des zéros.
    """
    return [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]


def case_plateau(valeur):
    """
    Convertit la valeur entière d'une case en son symbole d'affichage.

    Paramètre :
        valeur - La valeur de la case (0 pour vide, 1 pour X, 2 pour O)
    """
    if valeur == 0:
        return " "
    elif valeur == 1:
        return "X"
    else:
        return "O"


def afficher_plateau(plateau):
    """
    Affiche le plateau de jeu dans la console.

    Paramètre :
        plateau - Le plateau de jeu sous forme d'un tableau doublement indexé.
    """
    affichage = ""
    for i_ligne in range(len(plateau)):
        # Construit la chaine d'affichage des pions d'une ligne du plateau.
        affichage += ' ' + '|'.join([case_plateau(case) for case in plateau[i_ligne]]) + '\n'

        # Construit la ligne horizontale de séparation.
        if i_ligne < 2:
            affichage += ('—' * 7) + '\n'

    print(affichage)

def demander_coup_joueur(joueur):
    """generer_plateau()
    Demande au joueur de saisir son coup sous la forme '{ligne}{colonne}'.
    La saisie "11" signifie que le joueur joue dans la première case en haut à gauche du plateau de jeu (plateau[0][0]).

    La fonction renvoie un tuple des coordonnées (ligne, colonne) du coup choisi.
    La saisie "32" (ligne 3, colonne 2) entraine le renvoi du tuple (2, 1).

    Paramètre :
        joueur - Numéro du joueur (1 ou 2)
    """
    saisie = input("Joueur " + case_plateau(joueur) + " : ")
    return traiter_saisie_joueur(saisie)


def traiter_saisie_joueur(saisie):
    """
    Renvoie la convertion de la saisie du joueur un tuple des coordonnées (ligne, colonne).

    Paramètre :
        saisie - La chaîne saisie par le joueur (format : '{ligne}{colonne}')
    """
    coup = (int(saisie[0])-1, int(saisie[1])-1)
    return coup


def jouer_coup_joueur(plateau, joueur, coup):
    """
    Place le symbole du joueur sur le plateau aux coordonnées spécifiées.

    Paramètres :
        plateau - Plateau de jeu sous forme d'un tableau doublement indexé
        joueur - Numéro du joueur
        coup - Tuple des coordonnées (ligne, colonne) où placer le symbole
    """
    plateau[coup[0]][coup[1]] = joueur


def tester_victoire(plateau, joueur):
    """
    Vérifie si le joueur spécifié a gagné la partie.
    Renvoie True si joueur a gagné, False sinon.

    Paramètres :
        plateau - Le plateau de jeu sous forme d'un tableau doublement indexé
        joueur - Le numéro du joueur à tester (1 ou 2)
    """
    if plateau[0][0] == plateau [1][0] == plateau [2][0] == joueur:
        return True
    elif plateau[0][1] == plateau [1][1] == plateau [2][1] == joueur:
        return True
    elif plateau[0][2] == plateau [1][2] == plateau [2][2] == joueur:
        return True
    elif plateau[0][2] == plateau [1][1] == plateau [2][0] == joueur:
        return True
    elif plateau[0][0] == plateau [1][1] == plateau [2][2] == joueur:
        return True
    elif plateau[0][0] == plateau [0][1] == plateau [0][2] == joueur:
        return True
    elif plateau[1][0] == plateau [1][1] == plateau [1][2] == joueur:
        return True
    elif plateau[2][0] == plateau [2][1] == plateau [2][2] == joueur:
        return True
    else:
        return False

def tester_match_nul(plateau):
    """
    Vérifie si la partie est un match nul.
    Renvoie True si le match est nul, False sinon.

    Paramètre :
        plateau - Le plateau de jeu sous forme d'un tableau doublement indexé
    """
    for i in range(3):
        if 0 in plateau[0]:
            return False
        if 0 in plateau[1]:
            return False
        if 0 in plateau[2]:
            return False
        else:
            return True

def afficher_victoire(joueur):
    """
    Affiche le message de victoire pour le joueur spécifié.

    Paramètre :
        joueur - Numéro du joueur gagnant (1 ou 2)
    """
    print("Le joueur " + case_plateau(joueur) + " a gagné !")


def afficher_nul():
    """ Affiche le message de match nul. """
    print("Match nul !")


def lancer_jeu():
    plateau = generer_plateau()
    joueur = 1
    while True:
        afficher_plateau(plateau)
        coup = demander_coup_joueur(joueur)
        jouer_coup_joueur(plateau, joueur, coup)
        # Vérifie victoire
        if tester_victoire(plateau, joueur):
            afficher_plateau(plateau)
            afficher_victoire(joueur)
            break
        # Vérifie match nul
        if tester_match_nul(plateau):
            afficher_plateau(plateau)
            afficher_nul()
            break
        # Changer de joueur
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
        
        
        
    
    