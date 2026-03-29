import timeit

def somme_nombres(N):
    return N * (N+1)/2

# print(somme_nombres(5))

def somme_nombres2(N):
    r = 0
    for i in range(0, N+1):
        r += i
    return r

# print(somme_nombres2(5))

def somme_nombres_recursif(N):
    if N == 1:
        return 1
    return N + somme_nombres_recursif(N-1)

# print(somme_nombres_recursif(5))

def somme_geometrique(N, q):
    if q == 1:
        return N
    return (1 - q**N) / (1 - q)

# print(somme_geometrique(10, 2))

def somme_geometrique_non_recursive(N, q):
    somme = 0
    terme = 1
    for _ in range(N):
        somme += terme
        terme *= q
    return somme

# print(somme_geometrique_non_recursive(10, 2))

def somme_geometrique_recursive(N, q):
    if N == 0:
        return 0
    return (q ** (N - 1)) + somme_geometrique_recursive(N - 1, q)

# print(somme_geometrique_recursive(10, 2))

fonctions = [
("somme_nombres", somme_nombres),
("somme_nombres2", somme_nombres2),
("somme_nombres_recursif", somme_nombres_recursif),
("somme_geometrique", somme_geometrique),
("somme_geometrique_non_recursive", somme_geometrique_non_recursive),
("somme_geometrique_recursive", somme_geometrique_recursive),
]

results = [["Fonction",'       ' "Temps (s)"]]

for nom, fonction in fonctions:
    debut = timeit.default_timer()
    if "geometrique" in nom:
        for i in range (20000):
            fonction(10, 2)
    else:
        for i in range(20000):
            fonction(10)
    duree = timeit.default_timer() - debut
    results.append([nom, duree])

for nom, temps in results:
    if nom == "Fonction":
        print(nom, temps)
    else:
        print(nom, ":", temps)

