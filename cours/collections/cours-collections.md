# COURS PYTHON : COLLECTIONS

## Sommaire

1. [Tuples](#tuples)
2. [Listes](#listes)
   - [Ajouter ou retirer un élément](#ajouter-ou-retirer-un-élément)
   - [Ajouter plusieurs éléments](#ajouter-plusieurs-éléments-à-une-liste)
   - [Supprimer un élément](#supprimer-un-élément-dune-liste)
   - [Listes et fonctions](#listes-et-fonctions--modifications-globales)
   - [Méthodes utiles](#méthodes-utiles-pour-les-listes)
3. [Slices](#les-slices)
4. [Dictionnaires](#le-dictionnaire)
   - [Définition et syntaxe](#définition-et-syntaxe)
   - [Opérations courantes](#opérations-courantes-sur-les-dictionnaires)
   - [Exemple pratique : Dictionnaire imbriqué](#exemple-pratique--dictionnaire-imbriqué)
5. [Comparaison : Dictionnaire vs Listes](#dictionnaire-vs-listes)
6. [Exercice : Questionnaire interactif](#exercice--questionnaire-interactif-en-python)

# TUPLES

Les **tuples** font partie des collections en Python (comme les tableaux ou les listes).  
Un tuple est une **collection ordonnée et immuable** utilisée pour contenir plusieurs éléments. Contrairement aux listes, les tuples ne peuvent pas être modifiés après leur création, ce qui les rend idéaux pour stocker des données constantes ou des ensembles d’informations que l’on ne souhaite pas modifier.

Exemple : Une chaîne de caractères est en réalité un Tuple, pour <code>fruit = "Pomme"</code> le premier caratère s'affichera en faisant <code>fruit[0]</code>

Le cas de <code>range</code> : range est en réalité un Tuple

```python
for i in range(0, 5)

valeurs = range(0, 5) # Un Tuple contenant (0,1,2,3,4)
print(valeurs[-1]) # Affichera 4 car il contient des valeurs de 0 à 4
```

### Exemple 1 :

```python
personnes = ("Mélanie", "Jean", "Martin", "Alice") # Tuple car entre ()
print(len(personnes)) # Affichera la longueur/nombre d'éléments du Tuple : 4
print(personnes[0]) # Affichera l'élément à l'index [0] fonctionne aussi sur les listes : Mélanie
print(personnes[-1]) # Affichera le dernier élémént du Tuple: Alice

# Affiche le nom de la personne à l'index i correspondant à chaque tour
# Mélanie
# Jean
# Martin
# Alice
for i in range(0, len(personnes)):
    print(personnes[i])

# On peut aussi écrire comme ça :
for i in personnes:
    print(i)

# Ou comme ceci :
for personne in personnes:
    print(personne)
```

### Explications :

- **Ordonné** : Les éléments du tuple sont rangés dans un ordre spécifique, ce qui permet d’y accéder à l’aide de leur index.  
  Exemple : `personnes[0]` retourne `"Mélanie"`.

- **Immuable** : Une fois créé, il est impossible d’ajouter, de supprimer ou de modifier les éléments d’un tuple.

- **Utile pour les données constantes** : Les tuples sont utilisés lorsqu'on souhaite s'assurer que les données restent inchangées, comme des coordonnées géographiques ou des constantes.

- **Différence avec les listes** : Contrairement aux listes, les tuples sont plus rapides et consomment moins de mémoire.

- **Types mélangés** : Un tuple peut contenir des éléments de différents types.  
  Exemple : `mon_tuple = (42, "Python", 3.14)`.

En résumé, les tuples sont parfaits pour des données fixes et permettent une manipulation efficace grâce à leur immuabilité.

# LISTES

```python
personnes = ["Mélanie", "Jean", "Martin", "Alice"] # Liste car entre []
```

## Ajouter ou retirer un élément

Pour **ajouter un élément** à une liste, on utilise la méthode `append()` :

```python
nom_liste.append(élément_à_ajouter)
```

## Ajouter plusieurs éléments à une liste

1. **`extend()`** :

   - Ajoute les **éléments** d’une autre liste, un par un.

     ```python
     nom_liste = ["Jean", "Sophie"]
     elements_a_ajouter = ["Christophe", "Zoé"]
     nom_liste.extend(elements_a_ajouter)
     print(nom_liste)  # ['Jean', 'Sophie', 'Christophe', 'Zoé']
     ```

2. **Opérateur `+=`** :

   - Semblable à `extend()` :

     ```python
     nom_liste += elements_a_ajouter
     ```

3. **Ajouter une sous-liste entière avec `append()`** :

   - La liste est ajoutée comme un **élément unique** :

     ```python
     nom_liste.append(elements_a_ajouter)
     ```

## Supprimer un élément d'une liste

Pour **retirer un élément**, plusieurs options s'offrent à nous :

1. **Supprimer par index** :

   ```python
   del noms[index]
   ```

2. **Supprimer un élément spécifique** :

   ```python
   noms.remove(valeur)
   ```

3. **Supprimer et récupérer l’élément** :

   ```python
   noms.pop(index)
   ```

### Suppression avec une boucle

Si tu veux supprimer plusieurs éléments d'une liste à l'aide d'une boucle, il est **préférable de commencer par la fin de la liste** (en utilisant l'index `-1`).  
Cela permet d'éviter des erreurs liées à la modification des index pendant la suppression des éléments.

**Exemple :**

```python
ma_liste = [1, 2, 3, 4, 5]

# ici le -1 supplémentaire permet d'indiquer le sens de la boucle
for i in range(len(ma_liste) - 1, -1, -1):  # Boucle de la fin vers le début
    del ma_liste[i]
print(ma_liste)  # Affiche : []
#ou
for personne in reversed(personnes):  # reversed renvoie les éléments dans l'ordre inverse
    personnes.remove(personne)
print(ma_liste)  # Affiche : []
```

## Listes et Fonctions : Modifications globales

Contrairement à une variable simple (comme un entier ou un float), les **listes** passées en paramètre à une fonction sont modifiées globalement si elles sont altérées dans la fonction. Cela est dû à la manière dont Python gère les références des objets mutables.

### Exemple :

```python
def modifier_valeur(a):
     a[0] = 10

test = [1, 2, 3, 4]
print(test)  # Affichera : [1, 2, 3, 4]
modifier_valeur(test)
print(test)  # Affichera : [10, 2, 3, 4]
```

### Explications :

1. **Les listes sont des objets mutables :**

   - En Python, une liste est un **objet mutable**, ce qui signifie qu’elle peut être modifiée directement.
   - Lorsqu’une liste est passée en paramètre à une fonction, ce n’est pas une copie de la liste qui est transmise, mais une **référence** vers l'objet d'origine.

2. **Impact des modifications :**

   - Dans l'exemple, lorsque `modifier_valeur` modifie `a[0]`, elle modifie en réalité la liste originale référencée par `test`.

3. **Différence avec une variable simple :**

   - Les variables simples comme les entiers ou les floats sont des **objets immuables**. Lorsqu'elles sont passées en paramètre, une **copie** de leur valeur est utilisée, et leur valeur d'origine reste inchangée.

     **Exemple avec une variable simple :**

   ```python
   def modifier_variable(x):
       x = 10

   y = 5
   print(y)  # Affichera : 5
   modifier_variable(y)
   print(y)  # Affichera : 5 (pas modifié)
   ```

4. **Pourquoi cela se produit-il ?**
   - Les objets mutables (comme les listes) transmettent leur **référence mémoire**, pas une copie.
   - Les objets immuables (comme les entiers) transmettent leur **valeur**, donc toute modification dans la fonction n'affecte pas l'objet d'origine.

### Comment éviter les modifications globales ?

Pour éviter que la liste originale ne soit modifiée :

1. **Faire une copie de la liste avant modification** :

   ```python
   originale = [1, 2, 3]
   copie = originale.copy()  # Copie superficielle
   copie[0] = 10
   print(originale)  # [1, 2, 3]
   print(copie)      # [10, 2, 3]
   ```

2. **Utiliser une tranche pour copier** :

   ```python
   originale = [1, 2, 3]
   copie = originale[:]
   copie[0] = 10
   print(originale)  # [1, 2, 3]
   print(copie)      # [10, 2, 3]
   ```

3. **Pour des structures imbriquées**, utiliser une copie **profonde** :

   ```python
   import copy

   originale = [[1, 2], [3, 4]]
   copie_profonde = copy.deepcopy(originale)

   copie_profonde[0][0] = 10
   print(originale)  # [[1, 2], [3, 4]] (inchangée)
   print(copie_profonde)  # [[10, 2], [3, 4]] (modifiée)
   ```

---

### Résumé :

- **Les listes sont modifiées globalement lorsqu'elles sont passées en paramètre** si elles sont altérées dans la fonction.
- Pour éviter ce comportement :
  - Utilise `copy()` ou une tranche (`[:]`) pour créer une **copie superficielle**. Ces méthodes sont adaptées pour des listes simples (sans sous-listes ou objets imbriqués).
  - Si la liste contient des sous-listes ou des objets imbriqués, utilise `copy.deepcopy()`. Cela permet de dupliquer également les éléments imbriqués sans affecter l'original.
- **Pourquoi utiliser `copy()` ?**
  - Plus explicite : Le lecteur comprend immédiatement que tu veux créer une copie.
  - Modernité et clarté : `copy()` est une méthode standard, intuitive et lisible.
  - Alternative avec `[:]` ou `list()` : Ces méthodes restent valides et équivalentes pour des listes simples.
- **Quand utiliser quoi ?**
  - **`copy()` ou `[:]`** : Pour des listes simples, sans imbrication.
  - **`copy.deepcopy()`** : Si la liste est complexe et contient des sous-listes ou des objets.

## Méthodes utiles pour les listes

| **Méthode**        | **Description**                                                  | **Exemple**                               |
| ------------------ | ---------------------------------------------------------------- | ----------------------------------------- |
| `append(x)`        | Ajoute l’élément `x` à la fin de la liste                        | `ma_liste.append(5)`                      |
| `extend(iterable)` | Ajoute les éléments d’un itérable (liste, tuple, etc.)           | `ma_liste.extend.extend(["Zoé", "Paul"])` |
| `insert(i, x)`     | Insère `x` à l’index `i`                                         | `ma_liste.extend.insert(0, "Jean")`       |
| `remove(x)`        | Supprime la **première occurrence** de `x`                       | `ma_liste.remove(3)`                      |
| `pop([i])`         | Supprime et renvoie l’élément à l’index `i` (dernier par défaut) | `ma_liste.pop(2)`                         |
| `sort()`           | Trie la liste **en place** par ordre alphabétique 0-9 A-Z a-z    | `ma_liste.sort()`                         |
| `reverse()`        | Inverse l’ordre des éléments de la liste                         | `ma_liste.reverse()`                      |
| `index(x)`         | Renvoie l’index de la première occurrence de `x`                 | `ma_liste.index(4)`                       |
| `count(x)`         | Compte le nombre d’occurrences de `x` dans la liste              | `ma_liste.count(4)`                       |
| `copy()`           | Renvoie une copie superficielle de la liste                      | `nouvelle_liste = ma_liste.copy()`        |
| `clear()`          | Supprime tous les éléments de la liste                           | `ma_list.clear()`                         |

### Résumé des bonnes pratiques :

1. Pour ajouter :

   - **Un élément** : `append(x)`
   - **Plusieurs éléments** : `extend()` ou `+=`
   - **À une position** : `insert(index, valeur)`

2. Pour supprimer :
   - **Par index** : `del`
   - **Par valeur** : `remove(x)`
   - **Dernier élément** : `pop()`

- **Supprimer un élément à un index précis** : Utilise `del`.
- **Supprimer un élément spécifique** : Utilise `remove()`.
- **Suppression en boucle** :

  - Si tu veux supprimer des éléments en manipulant les **index**, parcours la liste **en partant de la fin** avec `range`.
  - Si tu veux supprimer des éléments sans utiliser d'index, parcours la liste **en sens inverse** avec `reversed()` :

    ```python
    for element in reversed(ma_liste):
        ma_liste.remove(element)
    ```

Cette approche est fiable et te protège contre les bugs lorsque tu modifies une liste dans une boucle, en évitant les problèmes liés au décalage des index.

## Différence entre Listes et Tuples

En Python, **les listes** et **les tuples** sont des collections permettant de stocker plusieurs éléments, mais ils ont des caractéristiques et des usages différents.

### 1. **Mutabilité**

- **Listes** : Modifiables (mutables). Les éléments d'une liste peuvent être ajoutés, supprimés ou modifiés après sa création.
  ```python
  ma_liste = [1, 2, 3]
  ma_liste[0] = 10  # Modification possible
  print(ma_liste)  # [10, 2, 3]
  ```
- **Tuples** : Non modifiables (immuables). Une fois créé, un tuple ne peut plus être modifié.
  ```python
  mon_tuple = (1, 2, 3)
  # mon_tuple[0] = 10  # Erreur : impossible de modifier un tuple
  ```

---

### 2. **Performance**

- **Listes** : Moins rapides et consomment plus de mémoire que les tuples, car elles doivent gérer leur mutabilité.
- **Tuples** : Plus rapides et consomment moins de mémoire, ce qui les rend idéaux pour des données constantes.

---

### 3. **Utilisation**

- **Listes** : Utilisées lorsque les données doivent être modifiées ou manipulées fréquemment.

  ```python
  fruits = ["pomme", "banane", "cerise"]
  fruits.append("orange")  # Ajout d'un élément
  print(fruits)  # ["pomme", "banane", "cerise", "orange"]
  ```

- **Tuples** : Utilisés pour des données constantes ou immuables (par exemple, des coordonnées, des jours de la semaine, des paramètres fixes).

  ```python
  jours = ("lundi", "mardi", "mercredi")
  print(jours[0])  # "lundi"
  ```

---

### 4. **Syntaxe**

- **Listes** : Définies avec des crochets `[]`.

  ```python
  ma_liste = [1, 2, 3]
  ```

- **Tuples** : Définis avec des parenthèses `()`.

  ```python
  mon_tuple = (1, 2, 3)
  ```

---

### Résumé des différences :

| **Caractéristique** | **Liste**                            | **Tuple**                              |
| ------------------- | ------------------------------------ | -------------------------------------- |
| **Mutabilité**      | Modifiable                           | Non modifiable                         |
| **Performance**     | Plus lente, consomme plus de mémoire | Plus rapide, consomme moins de mémoire |
| **Utilisation**     | Données changeantes                  | Données constantes                     |
| **Définition**      | Crochets `[]`                        | Parenthèses `()`                       |
| **Exemple**         | `[1, 2, 3]`                          | `(1, 2, 3)`                            |

En conclusion, utilise des **listes** si tu prévois de modifier les données, et des **tuples** si tes données doivent rester fixes et immuables.

# FONCTIONS ET TUPLES

En Python, une fonction peut retourner **plusieurs valeurs** en utilisant un **tuple**. Cela est particulièrement utile lorsque tu souhaites renvoyer un ensemble de données liées entre elles, comme des informations détaillées sur une personne.

---

## Exemple 1 : Retourner plusieurs valeurs avec un tuple

```python
def obtenir_informations():
    return "Mélanie", 20, 1.60  # Retourne un tuple contenant plusieurs valeurs de différents types

infos = obtenir_informations()  # Le tuple est stocké dans la variable `infos`

# Accès aux éléments du tuple via leurs index
print(f"nom : {infos[0]}")
print(f"age : {infos[1]}")
print(f"taille : {infos[2]}")
```

### Explications :

1. **Retourner un tuple :**

   - La fonction `obtenir_informations` retourne un **tuple** contenant les informations sous forme de valeurs distinctes (`str`, `int`, `float`).
   - Les parenthèses sont optionnelles ici : Python comprend automatiquement que les valeurs séparées par des virgules constituent un tuple.

2. **Accès via les index :**
   - Les éléments du tuple peuvent être consultés à l’aide de leurs **index** : `infos[0]` pour le nom, `infos[1]` pour l’âge, etc.
   - Bien que fonctionnel, cela rend le code moins lisible que d’utiliser des variables nommées.

---

## Exemple 2 : Passer un tuple en tant que paramètres d'une fonction

```python
def afficher_informations(nom, age, taille):
    print(f"Informations : Nom : {nom}, age: {age}, taille {taille}")

infos = obtenir_informations()  # Le tuple est stocké dans `infos`
afficher_informations(*infos)  # "Ouvrir" le tuple pour le passer en arguments

# infos à récupérer nom, age, taille sous forme de Tuple via le return de la fonction "obtenir_information", maintenant via *infos ou c'est comme si on faisait afficher_informations(valeur_nom, valeur_age, valeur_taille)

print(*infos) # c'est comme si on fait print(valeur_nom, valeur_age, valeur_taille)
#affichera "Mélanie 37 1.6"
```

### Explications :

1. **Définition de la fonction `afficher_informations` :**

   - Cette fonction prend trois paramètres (`nom`, `age`, `taille`) et affiche les informations dans un format lisible.

2. **Passage d’un tuple avec `*` :**
   - L’opérateur `*` "ouvre" le tuple `infos` et transmet ses éléments comme des arguments individuels à la fonction `afficher_informations`. On dit que l'on unpack le Tuple.
   - Sans `*`, Python essaierait de passer le tuple entier comme un seul argument, ce qui provoquerait une erreur.

---

## Exemple 3 : Meilleure manière de décomposer un tuple

```python
def obtenir_informations():
    return "Mélanie", 20, 1.60

def afficher_informations(nom, age, taille):
    print(f"Informations : Nom : {nom}, age: {age}, taille {taille}")

# Décomposition du tuple directement en variables
nom, age, taille = obtenir_informations()

# Passage des variables nommées
afficher_informations(nom, age, taille)
```

### Explications :

1. **Décomposition du tuple :**

   - Lors de l’appel à `obtenir_informations`, le tuple retourné est **décomposé** directement en trois variables (`nom`, `age`, `taille`).
   - Cela rend le code plus lisible et les variables sont accessibles par des noms explicites.

2. **Utilisation des variables décomposées :**
   - Les variables `nom`, `age`, `taille` sont passées directement à la fonction `afficher_informations`, sans avoir besoin d'utiliser `*`.

---

## Résumé des bonnes pratiques

- Si une fonction retourne plusieurs valeurs liées, utilise un **tuple**.
- Utilise l’opérateur `*` pour "ouvrir" un tuple et transmettre ses éléments comme arguments individuels à une autre fonction.
- **Décompose les tuples en variables nommées** pour rendre ton code plus lisible et maintenable :
  ```python
  nom, age, taille = obtenir_informations()
  afficher_informations(nom, age, taille)
  ```

---

# LES SLICES

Les **slices** permettent de découper ou de parcourir des collections en Python.  
Ils s'appliquent aux **listes**, aux **tuples**, et même aux **chaînes de caractères**, car ces dernières sont des collections immuables similaires aux tuples.

---

## Syntaxe d'un slice

```python
[start:end:step]
```

### Paramètres :

1. **`start`** : L'index de début du slice (inclus). Si omis, commence au début de la collection.
2. **`end`** : L'index de fin du slice (exclu). Si omis, va jusqu'à la fin de la collection.
3. **`step`** : Le pas du slice. Définit l'incrément entre chaque élément.
   - Par défaut, `step=1` (parcourt la collection élément par élément).
   - Peut être négatif pour parcourir la collection en sens inverse.

---

## Exemple avec un tuple

```python
personnes = ("Mélanie", "Jean", "Martin", "Alice", "Pierre", "Paul")

# Slice simple
for personne in personnes[0:1]:  # Affiche l'élément à l'index 0
    print(personne)  # Affiche "Mélanie", mais pas "Jean"

# Slice avec un `step`
for personne in personnes[::2]:  # Step de 2 (affiche un élément sur deux)
    print(personne)  # Affiche "Mélanie", "Martin", "Pierre"

# Slice inversé avec un `step` négatif
for personne in personnes[::-1]:  # Parcourt le tuple en sens inverse
    print(personne)  # Affiche "Paul", "Pierre", "Alice", ..., "Mélanie"
```

### Explications :

1. **`[0:1]`** : Affiche uniquement l'élément à l'index `0` (`start=0`, `end=1` exclu).
2. **`[::2]`** : Ignore les paramètres `start` et `end`, mais avance de `step=2`.
3. **`[::-1]`** : Parcourt tous les éléments en **ordre inverse** grâce au `step=-1`.

---

## Exemple avec des chaînes de caractères

Les slices fonctionnent également sur les chaînes de caractères, car elles sont considérées comme des **collections immuables**.

```python
nom = "Jean"

# Slices simples
print(nom[0:3])  # Affiche "Jea" (car `end=3`, donc le caractère à l'index 3 est exclu)
print(nom[1:3])  # Affiche "ea" (commence à l'index 1, exclut l'index 3)

# Slices avec step
print(nom[::2])  # Affiche "Ja" (une lettre sur deux)
print(nom[::-1])  # Affiche "naeJ" (inverse la chaîne)
```

### Explications :

1. **`[0:3]`** : Commence à l'index `0` et s'arrête avant l'index `3`.
2. **`[1:3]`** : Commence à l'index `1` et s'arrête avant l'index `3`.
3. **`[::2]`** : Avance d'un pas de `2`, affichant une lettre sur deux.
4. **`[::-1]`** : Affiche la chaîne en **ordre inverse**.

---

## Résumé des bonnes pratiques

- Utilise **`start` et `end`** pour limiter les éléments à parcourir ou afficher.
- Utilise **`step`** pour sauter des éléments ou inverser l’ordre.
- Les slices sont idéaux pour :
  - Extraire des parties d’une collection (comme des sous-listes ou sous-chaînes).
  - Parcourir les collections en **ordre inversé** sans écrire de logique complexe.

Avec les slices, ton code reste concis, puissant et lisible ! 😊

---

# LE DICTIONNAIRE

Un **dictionnaire** est une collection en Python qui permet d'associer des **clés** à des **valeurs**.  
Il est particulièrement utile pour structurer des données avec des champs et améliorer l'efficacité de certains algorithmes.

---

## Définition et syntaxe

Un dictionnaire est défini avec des **accolades `{}`**, et chaque paire clé-valeur est séparée par un deux-points `:`.

### Exemple de base :

```python
personne = {'nom': 'Mélanie', 'age': 25, 'profession': 'Développeuse'}
print(personne['nom'])  # Affiche : Mélanie
print(personne['age'])  # Affiche : 25
```

# Caractéristiques des dictionnaires

## Clés uniques :

- Chaque clé doit être unique dans un dictionnaire.
- Si une clé est répétée, sa dernière valeur remplace la précédente.

```python
d = {'a': 1, 'b': 2, 'a': 3}  # La clé 'a' est répétée
print(d)  # Affiche : {'a': 3, 'b': 2}
```

## Clés immuables :

- Les clés doivent être des objets immuables (chaînes, nombres, tuples immuables).
- Les listes ou autres objets mutables ne peuvent pas être utilisés comme clés.

## Valeurs flexibles :

- Les valeurs peuvent être de n'importe quel type : chaînes, nombres, listes, tuples, dictionnaires, etc.

---

# Opérations courantes sur les dictionnaires

## Ajouter ou mettre à jour une clé-valeur

```python
personne = {}
personne['ville'] = 'Paris'  # Ajoute une nouvelle clé 'ville'
personne['age'] = 26         # Met à jour la valeur associée à la clé 'age'
print(personne) # affiche {'ville': 'Paris', 'age': 26}
```

## Supprimer une clé-valeur

```python
del personne['profession']  # Supprime la clé 'profession'
print(personne)
```

## Vérifier l'existence d'une clé

```python
if 'nom' in personne:
    print("Clé 'nom' présente dans le dictionnaire")
```

## Parcourir un dictionnaire

### Par les clés uniquement :

```python
for cle in personne:
    print(cle)  # Affiche chaque clé du dictionnaire
```

### Par les valeurs uniquement :

```python
for valeur in personne.values():
    print(valeur)  # Affiche chaque valeur du dictionnaire
```

### Par les paires clé-valeur :

```python
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")  # Affiche chaque clé avec sa valeur
```

---

## Obtenir une valeur en toute sécurité

Utilise la méthode `get()` pour éviter une erreur si la clé n'existe pas :

```python
ville = personne.get('ville', 'Inconnue')  # Renvoie 'Inconnue' si la clé 'ville' n'existe pas
print(ville)
```

---

# Avantages des dictionnaires

## Accès rapide :

- Les dictionnaires permettent un accès rapide aux valeurs grâce à leurs clés.

## Flexibilité :

- Ils peuvent contenir des types de données variés et même être imbriqués.

## Utile pour structurer des données complexes :

- Les dictionnaires sont parfaits pour représenter des objets du monde réel ou des structures JSON.

---

# Exemple pratique : Dictionnaire imbriqué

```python
etudiants = {
    '001': {'nom': 'Mélanie', 'age': 25, 'notes': [15, 18, 20]},
    '002': {'nom': 'Jean', 'age': 22, 'notes': [12, 14, 16]},
}
```

# Accéder aux informations d'un étudiant

print(etudiants['001']['nom']) # Affiche : Mélanie

# Ajouter une note à un étudiant

etudiants['001']['notes'].append(19)
print(etudiants['001']['notes']) # Affiche : [15, 18, 20, 19]

---

# Résumé

- Un dictionnaire associe des **clés uniques** à des **valeurs**.
- Les **clés** doivent être **immuables**, mais les **valeurs** peuvent être de n'importe quel type.
- Les dictionnaires permettent de structurer des données complexes de manière lisible et efficace.

---

# Dictionnaire VS Listes

En Python, **les dictionnaires** et **les listes** sont deux structures de données couramment utilisées, mais elles diffèrent par leur structure et leurs cas d'utilisation. Voici une comparaison entre les deux pour manipuler des données comme `nom`, `âge`, et `taille`.

---

## Manière de faire avec une liste

# Liste contenant des tuples (nom, âge, taille)

```Python
personnes = [
    ("Mélanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacques", 35, 1.75),
    ("Martin", 16, 1.65)
]
```

# Fonction pour obtenir les informations d'une personne par son nom

```Python
def obtenir_information(nom, liste):
    for i in liste:
        if i[0] == nom:  # Vérifie si le nom correspond
            return i
    return None  # Retourne None si le nom n'est pas trouvé

infos = obtenir_information("Jacques", personnes)
print(infos)  # Affiche : ('Jacques', 35, 1.75)
```

### Inconvénients :

1. **Recherche lente** : La recherche d’un élément dans une liste nécessite de parcourir tous les éléments un par un (`O(n)` en complexité).
2. **Lisibilité réduite** : Les données ne sont pas nommées, donc on doit utiliser des index (`i[0]`, `i[1]`) pour accéder aux informations, ce qui peut rendre le code moins intuitif.

---

## Manière de faire avec un dictionnaire

# Dictionnaire associant le nom à un tuple (âge, taille)

```Python
personnes_dict = {
    'Mélanie': (25, 1.6),
    'Paul': (29, 1.8),
    'Jacques': (35, 1.75),
    'Martin': (16, 1.65)
}
```

# Recherche dans le dictionnaire

```Python
infos = personnes_dict.get('Jacques')  # Renvoie les infos de Jacques
print(infos)  # Affiche : (35, 1.75)
```

# Recherche d'une clé inexistante

```Python
infos = personnes_dict.get('Claire')  # Renvoie None si la clé n'existe pas
if not infos:  # Vérifie si aucune information n'est trouvée
    print("La clé n'existe pas")
else:
    print(infos)
```

### Avantages :

1. **Recherche rapide** : La recherche dans un dictionnaire est instantanée (`O(1)` en complexité), quelle que soit la taille des données.
2. **Code lisible** : Les clés permettent de nommer les données, rendant leur manipulation plus intuitive.
3. **Gestion des erreurs simplifiée** : La méthode `get()` permet de gérer facilement l'absence d'une clé sans provoquer d'erreur.

---

## Comparaison entre listes et dictionnaires

| **Caractéristique**     | **Liste**                               | **Dictionnaire**                               |
| ----------------------- | --------------------------------------- | ---------------------------------------------- |
| **Structure**           | Collection ordonnée                     | Collection de paires clé-valeur                |
| **Accès aux données**   | Basé sur des index                      | Basé sur des clés                              |
| **Recherche**           | Parcourt tous les éléments (`O(n)`)     | Recherche instantanée par clé (`O(1)`)         |
| **Lisibilité**          | Moins intuitive avec des index (`i[0]`) | Plus lisible grâce aux clés nommées            |
| **Gestion des erreurs** | Doit être codée manuellement            | Méthode `get()` pour gérer l'absence d'une clé |

---

### Résumé :

- Utilise une **liste** si l'ordre des éléments est important ou si tu manipules un petit ensemble de données.
- Privilégie un **dictionnaire** lorsque tu as besoin d'accéder rapidement aux données ou que tu souhaites une structure plus lisible et intuitive.

---

# Exercice : Questionnaire interactif en Python

Dans cet exercice, nous allons développer un **questionnaire interactif** en Python qui permet de poser des questions à l'utilisateur, de vérifier ses réponses, et de calculer un score final. Ce code utilise des **fonctions**, des **boucles**, et des **structures de données** comme les tuples pour structurer les questions.

---

## 1. Fonction : `demander_reponse_numerique`

Cette fonction demande une réponse numérique à l'utilisateur tout en vérifiant que la réponse est un entier compris entre une borne minimale (`min`) et maximale (`max`). Si l'utilisateur entre une valeur invalide, la fonction redemande une réponse.

### Code :

```Python
def demander_reponse_numerique(min, max):
    reponse_utilisateur_str = input(f"Votre réponse (Entre {min} et {max}) : ")

    try:
        reponse_utilisateur_int = int(reponse_utilisateur_str)
        if min <= reponse_utilisateur_int <= max:
            return reponse_utilisateur_int

        print(f"ERREUR: Veuillez entrer un nombre entre {min} et {max}) : ")
    except:
        print(f"ERREUR: Veuillez entrer uniquement des chiffres (Entre {min} et {max}) ")
    return demander_reponse_numerique(min, max)
```

### Explications :

1. **Vérification de la validité** :

   - Utilise un `try-except` pour vérifier que l'entrée est un entier.
   - Si l'utilisateur entre une valeur non numérique ou hors des bornes, un message d'erreur est affiché.

2. **Récursivité** :
   - La fonction se rappelle elle-même (`return demander_reponse_numerique`) jusqu'à ce que l'utilisateur fournisse une réponse valide.
   - Cette approche simplifie la gestion des erreurs.

---

## 2. Fonction : `poser_question`

Cette fonction pose une question à l'utilisateur, affiche les options disponibles, et détermine si la réponse est correcte ou non.

### Code :

```Python
def poser_question(question):
    bonne_reponse = question[2]  # Stocke la bonne réponse
    print("QUESTION")
    print("  " + question[0] )

    # Boucle pour afficher les choix
    choix = question[1]
    for i in range(len(choix)):
         print("   ", i+1,"-", choix[i])

    print()
    resultat_reponse_correcte = False
    reponse_utilisateur_int = demander_reponse_numerique(1, len(choix))
    if choix[reponse_utilisateur_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        resultat_reponse_correcte = True
    else:
        print("Mauvaise réponse")
    print()
    return resultat_reponse_correcte
```

### Explications :

1. **Affichage des choix** :

   - La fonction utilise une boucle pour afficher les options (`for i in range(len(choix))`).
   - Cela permet de s'adapter dynamiquement au nombre d'options.

2. **Validation de la réponse** :

   - La réponse de l'utilisateur (`reponse_utilisateur_int`) est convertie en index (`reponse_utilisateur_int - 1`) pour accéder à la bonne option.
   - Les comparaisons sont insensibles à la casse grâce à `.lower()`.

3. **Retour de la fonction** :
   - Renvoie `True` si la réponse est correcte, sinon `False`.

---

## 3. Fonction : `lancer_questionnaire`

Cette fonction parcourt une série de questions, pose chaque question à l'utilisateur, et calcule le score final.

### Code :

```Python
def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score +=1
    print("Score final :", score, "sur", len(questionnaire))
```

### Explications :

1. **Parcours des questions** :

   - Utilise une boucle `for` pour parcourir toutes les questions du questionnaire.
   - Chaque question est traitée par la fonction `poser_question`.

2. **Calcul du score** :

   - Le score est incrémenté (`score += 1`) chaque fois que la réponse de l'utilisateur est correcte.

3. **Affichage final** :
   - Affiche le score de l'utilisateur par rapport au nombre total de questions.

---

## 4. Structure des données : Questionnaire

Les questions sont organisées dans un **tuple** de tuples, où chaque tuple contient :

- Le texte de la question.
- Une liste des réponses possibles.
- La bonne réponse.

### Exemple de structure :

```Python
questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Rome", "Bruxelles", "Pise", "Florence"), "Bruxelles")
)
```

### Avantages de cette structure :

1. **Lisibilité** :

   - Chaque question est clairement structurée avec ses réponses et la bonne réponse.

2. **Flexibilité** :
   - Il est facile d'ajouter ou de modifier des questions sans changer le code.

---

## Résumé des points importants

1. **Récursivité** :

   - La fonction `demander_reponse_numerique` utilise la récursivité pour gérer les erreurs et redemander une entrée valide.

2. **Boucles pour afficher les choix** :

   - Les choix des questions sont affichés dynamiquement à l'aide d'une boucle, ce qui rend le code adaptable à un nombre variable de réponses.

3. **Gestion des réponses** :

   - Comparaison insensible à la casse (`.lower()`) pour vérifier si la réponse est correcte.
   - Utilisation de `get()` dans le dictionnaire pour éviter les erreurs lors de la récupération des réponses.

4. **Structure des données** :

   - Les tuples sont utilisés pour structurer les questions, offrant une lisibilité et une efficacité accrues.

5. **Score final** :
   - La fonction `lancer_questionnaire` parcourt toutes les questions et calcule un score final pour l'utilisateur.

Avec ce programme, vous avez un **questionnaire interactif** qui gère les erreurs, affiche dynamiquement les options, et fournit un score final à l'utilisateur.

# Les Ensembles (Sets) en Python

Les **ensembles (sets)** sont une structure de données en Python conçue pour stocker des éléments uniques de manière non ordonnée. Ils sont particulièrement utiles pour :

- Éliminer les **doublons** dans une collection.
- Effectuer des **opérations d'ensemble** comme l'union, l'intersection et la différence.

---

## Définition et syntaxe

Un ensemble est défini avec des **accolades `{}`** ou la fonction `set()`. Contrairement aux listes et aux tuples, les ensembles **n'acceptent pas les doublons**.

```Python
# Définir un ensemble
fruits = {"pomme", "banane", "orange", "pomme"}  # Les doublons sont ignorés
print(fruits)  # Affichera : {'pomme', 'banane', 'orange'}

# Création d'un ensemble vide
ensemble_vide = set()  # Utilisez set() et non {}
```

---

## Caractéristiques des ensembles

1. **Non ordonnés** : Les éléments ne sont pas indexés, donc il est impossible d'accéder directement à un élément par un index comme pour les listes ou tuples.

```Python
fruits = {"pomme", "banane", "orange"}
# fruits[0]  # Provoquerait une erreur
```

2. **Unicité** : Les doublons sont automatiquement supprimés.

```Python
nombres = {1, 2, 3, 2, 4}
print(nombres)  # Affichera : {1, 2, 3, 4}
```

3. **Mutabilité partielle** : Les ensembles eux-mêmes sont modifiables (on peut ajouter ou supprimer des éléments), mais leurs éléments doivent être immuables (comme des nombres, chaînes, ou tuples).

```Python
fruits = {"pomme", "banane"}
fruits.add("orange")  # Ajoute un élément
print(fruits)  # {'pomme', 'banane', 'orange'}
```

---

## Opérations courantes sur les ensembles

### Ajouter ou supprimer des éléments

1. **Ajouter un élément avec `add()`** :

```Python
ensemble = {1, 2, 3}
ensemble.add(4)
print(ensemble)  # {1, 2, 3, 4}
```

2. **Supprimer un élément avec `remove()`** :

```Python
ensemble.remove(2)
print(ensemble)  # {1, 3, 4}
```

3. **Supprimer un élément en toute sécurité avec `discard()`** :

- Contrairement à `remove()`, cette méthode ne provoque pas d'erreur si l'élément n'existe pas.

```Python
ensemble.discard(5)  # Ne fait rien si 5 n'est pas dans l'ensemble
```

4. **Supprimer tous les éléments avec `clear()`** :

```Python
ensemble.clear()
print(ensemble)  # Affiche : set()
```

---

### Opérations d'ensemble

1. **Union (`|` ou `union()`)** :
   Combine les éléments de deux ensembles.

```Python
ensemble1 = {1, 2, 3}
ensemble2 = {3, 4, 5}
union = ensemble1 | ensemble2
print(union)  # {1, 2, 3, 4, 5}
```

2. **Intersection (`&` ou `intersection()`)** :
   Récupère les éléments communs à deux ensembles.

```Python
intersection = ensemble1 & ensemble2
print(intersection)  # {3}
```

3. **Différence (`-` ou `difference()`)** :
   Récupère les éléments présents dans le premier ensemble mais pas dans le second.

```Python
difference = ensemble1 - ensemble2
print(difference)  # {1, 2}
```

4. **Différence symétrique (`^` ou `symmetric_difference()`)** :
   Récupère les éléments présents dans un seul des deux ensembles.

```Python
sym_diff = ensemble1 ^ ensemble2
print(sym_diff)  # {1, 2, 4, 5}
```

---

## Conversion entre collections

Python permet de convertir facilement les **listes**, **tuples**, et **dictionnaires** en **ensembles**, et inversement.

### Convertir une liste en ensemble

```Python
nombres = [1, 2, 2, 3, 4]
ensemble = set(nombres)
print(ensemble)  # {1, 2, 3, 4}
```

### Convertir un ensemble en liste ou tuple

```Python
ensemble = {1, 2, 3}
liste = list(ensemble)
tuple_ = tuple(ensemble)
print(liste)  # [1, 2, 3]
print(tuple_)  # (1, 2, 3)
```

### Extraire les clés d'un dictionnaire sous forme d'ensemble

```Python
dictionnaire = {"a": 1, "b": 2, "c": 3}
cle_set = set(dictionnaire.keys())
print(cle_set)  # {'a', 'b', 'c'}
```

---

# Cas pratiques

### Exemple 1 : Suppression des doublons

Les ensembles sont parfaits pour éliminer les doublons dans une collection.

```Python
noms = ["Alice", "Bob", "Alice", "Eve", "Bob"]
unique_noms = set(noms)
print(unique_noms)  # {'Alice', 'Bob', 'Eve'}
```

---

### Exemple 2 : Comparer deux listes

Avec les ensembles, on peut facilement trouver les éléments communs ou différents entre deux listes.

```Python
liste1 = [1, 2, 3, 4]
liste2 = [3, 4, 5, 6]

# Convertir en ensembles
set1 = set(liste1)
set2 = set(liste2)

# Intersection
print(set1 & set2)  # {3, 4}

# Différence
print(set1 - set2)  # {1, 2}
```

---

### Exemple 3 : Vérifier la présence d'un élément

Les ensembles permettent une recherche rapide grâce à leur structure.

```Python
voyelles = {"a", "e", "i", "o", "u"}
print("e" in voyelles)  # True
print("z" in voyelles)  # False
```

---

## Résumé : Pourquoi utiliser les ensembles ?

| **Cas d'utilisation**                             | **Avantage des ensembles**                             |
| ------------------------------------------------- | ------------------------------------------------------ |
| Suppression des doublons                          | Les ensembles suppriment automatiquement les doublons. |
| Opérations d'ensemble (union, intersection, etc.) | Simplifie les calculs mathématiques sur les ensembles. |
| Recherche rapide                                  | Recherche plus rapide que dans les listes.             |
| Comparaisons                                      | Permet de comparer facilement deux collections.        |

Les ensembles sont un excellent choix lorsque vous travaillez avec des données uniques ou avez besoin d'effectuer des opérations d'ensemble. 🎯
