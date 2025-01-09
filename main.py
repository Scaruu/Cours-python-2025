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
# print(noms_tries)