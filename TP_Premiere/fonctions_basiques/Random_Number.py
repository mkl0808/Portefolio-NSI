import random
secret = random.randint(0, 100)
user = int(input("Essaie de trouver mon nombre entre 0 et 100 "))

if int(user) > 100:
    exit("Erreur, saisie un nombre compris entre 0 et 100")
if int(user) < 0:
    exit("Erreur, saisie un nombre compris entre 0 et 100")

while user != secret:
    if user > secret:
        user = int(input("Ton nombre est trop grand, réessaye "))
    elif user < secret:
        user = int(input("Ton nombre est trop petit; réessaye "))

print("Bravo ! Mon nombre secret était bien", secret)