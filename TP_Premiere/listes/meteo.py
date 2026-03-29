# [NSI1RE06] TP1 - Problème météo
# Heure début : 09h50
# Heure fin   : 11h00




def rapport(temperatures_2021):
    mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    for i in range (len(mois)):
        print (mois[i] + " : " + str(temperatures_2021[i]))
        i+=1
    print ("Température moyenne annuelle : " + str(moyenne(tab)))
    print ("Température moyenne maximale : " + str(maximum(tab)))
        
def moyenne(tab):
    total = 0
    for v in tab:
        total += v
    t = total / len(tab)
    return t

def maximum(tab):
    max = tab[0]
    for v in tab:
        if v > max:
            max = v
    return max
  

if __name__ == '__main__':
    # Températures mensuelles moyennes de l'année 2021
    temperatures_2021 = [4.6, 6.5, 5.6, 10.0, 11.3, 14.4, 15.7, 17.6, 14.5, 10.3, 7.3, 5.2]
    tab = temperatures_2021

    # Affichage du rapport
    rapport(temperatures_2021)
    moyenne (tab)
    maximum(tab)
    