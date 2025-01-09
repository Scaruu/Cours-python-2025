# LES COLLECTIONS : LISTES / TUPLES
# Slices

"""
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoé"]

slices_noms = noms[:-1] # Affiche la liste sans le dernier element car [:-1] le dernier element est exclu : ["Zoé"]

slices_noms = noms[-2:] # Affiche les deux derniers élements["Christophe", "Zoé"]
# noms[0] = "Toto"

print(slices_noms)
# print(noms)
"""



# LES COLLECTIONS : LISTES / TUPLES
# Tris : Sort et sorted
"""
def tri_longueur_caracteres(nom): #fonction pour l'exemple ou l'on passe une fonction à sort() avec key.
    return len(nom)

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoé"]

# noms.sort() #in place, on a pas pris une nouvelle liste en mémoire on a travaillé sur la liste original, donc on l'a modifié on dis : "inplace"
# noms.sort(reverse=True) # Va en plus inverser l'ordre
noms.sort(key=lambda nom : len(nom)) # ici lambda permet d'écrire une fonction en mettant le code directement. La fonction sort() va appeler notre fonction lambda sur chaque élément de "noms", ici nommé nom mais aurait pu mettre x pour nous permettre de le transformer en sortie
# noms.sort(key=lambda nom : len(nom), reverse=True) # On peut meme cummuler avec reverse=True

noms.sort(key=tri_longueur_caracteres) # Fonction Callback donc sans les ()


noms_tries = sorted(noms) # va alouer à noms_tries une nouvelle liste (donc n'altere pas la première) triée
noms_tries = sorted(noms, reverse=True)  # Va en plus inverser l'ordre

noms_tries = sorted(noms, key=tri_longueur_caracteres, reverse=True) #avec fonction calback
print(noms)
# print(noms_tries)"""



# LES COLLECTIONS : LISTES / TUPLES
# Opetations sur les éléments : min, max, in, sum
"""
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoé"]
ages = [21, 20, 30, 25, 22]

# min et max
print(min(ages)) # donne la valeur minimum de la collection, ici 20
print(min(noms)) # donne "Christophe" car c'est le plus bas dans l'odre alphabétique
print(max(noms)) # donne "Zoé" car c'est le plus haut dans l'odre alphabétique
# MAIS A UTILISER QUE SUR DES VALEURS NUMERIQUES

#in avec un if / différent de in dans une boucle for(sensible à la case)
if "Jean" in noms: #si la valeur "Jean" est présente dans le tableau "noms"
    print("Présent")
else:
    print("Absent")
""
# sum
print(sum(ages)) #calcule la somme des valeurs de la liste, utilisable uniquement sur des collections qui on des valeurs numériques
"""



# LES COLLECTIONS : LISTES / TUPLES
# swapper deux éléments d'une liste (échanger de position)

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoé"]