# Les Variables en Python 🐍

Les variables sont des éléments essentiels en programmation, permettant de stocker, manipuler et réutiliser des données. En Python, elles sont dynamiques, faciles à utiliser et flexibles.

---

## 🛠️ 1. Introduction aux Variables

### Qu'est-ce qu'une variable ?

Une variable est un conteneur permettant de stocker des données. Elle agit comme un alias associé à une valeur dans la mémoire de l'ordinateur.

- **Exemple simple** :

  ```Python
  x = 5 # Stocke la valeur 5 dans la variable x
  nom = "Alice" # Stocke la chaîne de caractères "Alice" dans la variable nom
  ```

### Caractéristiques des variables en Python

1. **Dynamique** : Aucune déclaration de type n'est nécessaire. Le type est déterminé automatiquement.

   ```Python
   x = 42 # Entier
   x = "Python" # Devient une chaîne
   ```

2. **Sensible à la casse** : `maVariable` et `mavariable` sont deux variables distinctes.
3. **Flexible** : Les variables peuvent stocker n'importe quel type de données.

---

## 🛠️ 2. Déclaration et Affectation

### Syntaxe de base

```Python
nom_variable = valeur
```

### Affectation multiple

- Déclaration de plusieurs variables sur une seule ligne :

  ```Python
  a, b, c = 1, 2, 3
  ```

- Attribuer une même valeur à plusieurs variables :

  ```Python
  x = y = z = 0
  ```

### Type dynamique

Les variables peuvent changer de type en cours d'exécution :

```Python
variable = 10 # Entier
variable = "texte" # Devient une chaîne
```

---

## 🛠️ 3. Types de Données

### Types de base

- **`int`** : Entiers
- **`float`** : Nombres décimaux
- **`str`** : Chaînes de caractères
- **`bool`** : Booléens (`True` ou `False`)

```Python
age = 25 # int
taille = 1.75 # float
nom = "Alice" # str
est_actif = True # bool
```

### Collections

- **`list`** : Listes (mutables)
- **`tuple`** : Tuples (immuables)
- **`set`** : Ensembles (uniques et non ordonnés)
- **`dict`** : Dictionnaires (paires clé-valeur)

### Type spécial : `None`

Utilisé pour représenter l'absence de valeur.

```Python
x = None # Variable sans valeur
```

---

## 🛠️ 4. Conversion de Types

Les types de données peuvent être convertis à l'aide de fonctions prédéfinies.

- **Exemple :**

  ```Python
  age_str = "25"
  age = int(age_str) # Convertit en entier

  pi = 3.14
  pi_str = str(pi) # Convertit en chaîne
  ```

---

## 🛠️ 5. Nommage des Variables : Règles et Bonnes Pratiques

### Règles syntaxiques

1. Commencer par une lettre ou un underscore (`_`).
2. Ne pas utiliser de caractères spéciaux ni d'espaces.
3. Ne pas utiliser des mots-clés Python réservés (comme `if`, `while`, `for`).

### Bonnes pratiques

- **Utiliser des noms explicites** :

  ```Python

  # Mauvais

  x = 25

  # Bon

  age_utilisateur = 25
  ```

- **Respecter le style snake_case** :

  ```Python
  nombre_utilisateurs = 100
  ```

- **Variables constantes** : Utiliser des majuscules.

  ```Python
  PI = 3.14
  ```

---

## 🛠️ 6. Portée des Variables (Scope)

### Variables locales

Accessible uniquement dans la fonction où elle est définie.

```Python
def afficher_message():
message = "Bonjour" # Variable locale
print(message)

afficher_message()

# print(message) # Erreur : message n'existe pas en dehors de la fonction
```

### Variables globales

Accessible partout dans le programme.

```Python
message_global = "Bonjour"

def afficher_message():
print(message_global) # Variable globale accessible ici

afficher_message()
```

### Le mot-clé `global`

Permet de modifier une variable globale depuis une fonction.

```Python
compteur = 0

def incrementer():
global compteur
compteur += 1

incrementer()
print(compteur) # Affiche : 1
```

---

## 🛠️ 7. Variables Mutables vs Immuables

### Types immuables

Les données ne peuvent pas être modifiées après leur création.
Exemples : `int`, `float`, `str`, `tuple`.

```Python
nom = "Alice"

# nom[0] = "a" # Erreur
```

### Types mutables

Les données peuvent être modifiées.
Exemples : `list`, `dict`, `set`.

```Python
liste = [1, 2, 3]
liste[0] = 10 # Modification possible
```

---

## 🛠️ 8. Références et Mémoire

En Python, les variables stockent des **références** vers des objets, pas directement les valeurs.

### Exemple

```Python
a = [1, 2, 3]
b = a # 'b' pointe vers la même liste que 'a'
b[0] = 10
print(a) # Affiche : [10, 2, 3]
```

### Copier des objets

Pour éviter de partager la même référence :

- **Copie superficielle** :

  ```Python
  import copy
  a = [1, 2, 3]
  b = copy.copy(a)
  ```

- **Copie profonde** :

  ```Python
  b = copy.deepcopy(a)
  ```
