# Exercice 5 : Portée des variables

compteur = 10

def incrementer_local():
    compteur = 5
    compteur += 1
    print("Valeur locale :", compteur)

def incrementer_global():
    global compteur
    compteur += 1
    print("Valeur globale :", compteur)

incrementer_local()  # Affichera : 6
incrementer_global()  # Affichera : 11
print("Valeur finale :", compteur)  # Affichera : 11