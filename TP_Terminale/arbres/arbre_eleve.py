from PileFile import PileFile
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20, 6)

class arbre:
    
    def __init__(self):
        pass
    
    def est_vide(self, t):
        if t == [] :
            return True
        else:
            return False
    
    def taille(self, t):
        if self.est_vide(t):
            return 0
        else:
            taille_gauche = self.taille(t[1])
            taille_droite = self.taille(t[2])
            return 1 + taille_gauche + taille_droite
    
    def hauteur(self, t):
        if self.est_vide(t):
            return -1
        else:
            hauteur_gauche = self.hauteur(t[1])
            hauteur_droite = self.hauteur(t[2])
            return 1 + max(hauteur_gauche, hauteur_droite)

    def dessiner_aux(self,t, rect, dy, labels, avl=False):
        if (self.est_vide(t)):
            return
        x1, x2, y1, y2=rect
        xm= (x1+x2) //2
        x, t1, t2 = t
        self.dessiner_aux(t1, (x1, xm, y1, y2-dy), dy, labels, avl)
        self.dessiner_aux(t2, (xm, x2, y1, y2-dy), dy, labels, avl)
        if labels:
            if avl:
                plt.text(xm, y2, str(x[0]), fontsize=12, horizontalalignment='center')
            else:
                plt.text(xm, y2, str(x), fontsize=12, horizontalalignment='center')
        if not self.est_vide(t1):
            a, b= ((xm, (x1+xm) //2), (y2, y2-dy))
            plt.plot(a, b, 'k', marker='o', markerfacecolor='c', markersize=25)
        if not self.est_vide(t2):
            c, d= ((xm, (x2+xm) //2), (y2, y2-dy))
            plt.plot(c, d, 'k', marker='o', markerfacecolor='c', markersize=25)

    def dessiner(self,t, labels=True, avl=False):
        d=512
        pad=20
        dy= (d-2*pad) / (self.hauteur(t))
        self.dessiner_aux(t, (pad, d-pad, pad, d-pad), dy, labels, avl)
        plt.axis([0, d, 0, d])
        plt.axis('off')
        plt.show()
        
    def parcours_largeur(self, t):
        visite = PileFile()
        lst = []
        visite.enfiler(t)
        while not visite.estVide():
            visite.afficher()
            noeud = visite.defiler()
            if type(noeud) == list and noeud != []:
                lst.append(noeud[0])
                if noeud[1] != []:
                    visite.enfiler(noeud[1])
                if noeud[2] != []:
                    visite.enfiler(noeud[2])
            else:
                lst.append(noeud)
        return lst
    
    def parcours_profondeur(self, t):
        visite = PileFile()
        lst1 = []
        visite.empiler(t)
        while not visite.estVide():
            visite.afficher()
            noeud = visite.depiler()
            if type(noeud) == list and noeud != []:
                lst1.append(noeud[0])
                if noeud[2] != []:
                    visite.empiler(noeud[2])
                if noeud[1] != []:
                    visite.empiler(noeud[1])
            else:
                lst1.append(noeud)
        return lst1
    
    def parcours_profondeur_recursif_prefixe(self, t):
        lst2 = []
        if type(t) == list and t != []:
            lst2.append(t[0])
            if t[1] != []:
                print(t)
                lst2.extend(self.parcours_profondeur_recursif_prefixe(t[1]))
            if t[2] != []:
                print(t)
                lst2.extend(self.parcours_profondeur_recursif_prefixe(t[2]))
        else:
            print(t)
            lst2.append(t)
        return lst2
    
    def parcours_profondeur_recursif_infixe(self, t):
        lst2 = []
        if type(t) == list and t != []:
            if t[1] != []:
                print(t)
                lst2.extend(self.parcours_profondeur_recursif_infixe(t[1]))
            lst2.append(t[0])
            if t[2] != []:
                print(t)
                lst2.extend(self.parcours_profondeur_recursif_infixe(t[2]))
        else:
            print(t)
            lst2.append(t)
        return lst2
    
    def parcours_profondeur_recursif_postfixe(self, t):
        lst2 = []
        if type(t) == list and t != []:
            if t[1] != []:
                print(t)
                lst2.extend(self.parcours_profondeur_recursif_postfixe(t[1]))
            if t[2] != []:
                print(t)
                lst2.extend(self.parcours_profondeur_recursif_postfixe(t[2]))
            lst2.append(t[0])
        else:
            print(t)
            lst2.append(t)
        return lst2





