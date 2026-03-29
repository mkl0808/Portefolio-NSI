annee = input("En quelle année es-tu né ? ")
if annee.isdigit() == False:
    exit("Erreur, saisie un nombre")
if int(annee) >= 2024:
    exit("Erreur, saisie une année comprise entre 1900 et 2024")
if int(annee) <= 1900:
    exit("Erreur, saisie une année comprise entre 1900 et 2024")
majeur = int(annee) + 18
age = 2024 - int(annee)
if age >= 18:
    print("Tu as", age, "ans et tu es majeur. Tu est devenu majeur en", majeur)
else:
    print ("Tu as", age, "ans et tu es mineur. Tu seras majeur en", majeur)