temp = int(input("Quel est la température de l'eau ? "))
if int(temp) >= 100:
           print ("L'eau est à l'état gazeux")
elif int(temp) <= 0:
           print ("L'eau est à l'état solide")
else:
    print ("L'eau est à l'état liquide")