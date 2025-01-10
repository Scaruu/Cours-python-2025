# Exercice 4 : Calcul avec des variables
#Créez un programme qui demande à l'utilisateur de saisir deux nombres, les additionne, et affiche le résultat.

# Instructions :
# Déclarez deux variables pour stocker les entrées de l'utilisateur.
# Convertissez ces entrées en nombres entiers ou flottants.
# Calculez la somme et affichez-la.

nombre1 = input("Entrez-un le premier nombre : ")
nombre2 = input("Entrez-un le second nombre : ")

# Solution sans variable intermédiaire
print(float(nombre1) + float(nombre2))

# Solution avec variable intermédiaire
nombre1_float = float(nombre1)
nombre2_float = float(nombre2)

print(nombre1_float + nombre2_float)