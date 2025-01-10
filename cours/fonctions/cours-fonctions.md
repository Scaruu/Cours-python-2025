# 📚 Cours complet : Les Fonctions en Python

## Sommaire :

1. [Introduction](#introduction)
2. [✨ Définir une fonction](#définir-une-fonction)
3. [📥 Paramètres et arguments](#paramètres-et-arguments)
4. [🛠️ Paramètres par défaut](#️paramètres-par-défaut)
5. [🌟 Arguments positionnels et nommés](#arguments-positionnels-et-nommés)
6. [🔢 Nombre variable d'arguments](#nombre-variable-darguments)
   - [`*args` : Arguments positionnels variables](#args--arguments-positionnels-variables)
   - [`**kwargs` : Arguments nommés variables](#kwargs--arguments-nommés-variables)
7. [🔄 Valeur de retour avec `return`](#valeur-de-retour-avec-return)
8. [🔄 Les fonctions anonymes (lambda)](#les-fonctions-anonymes-lambda)
9. [🔄 Les Callbacks](#les-callbacks)
10. [📜 Fonctions imbriquées](#fonctions-imbriquées)
11. [🛠️ Les décorateurs (Decorators)](#️les-décorateurs-decorators)
    - [Exemple de base](#exemple-de-base)
    - [Exemple : Mesurer le temps d'exécution](#exemple--mesurer-le-temps-dexécution)
12. [🌟 Portée des variables (Scope)](#portée-des-variables-scope)
13. [⚙️ Utilisation du mot-clé `global`](#️-utilisation-du-mot-clé-global)
14. [🔄 Fonctions récursives](#fonctions-récursives)
15. [🔢 Déballer les arguments avec `*` et `**`](#déballer-les-arguments-avec--et-)
    - [Exemple avec `*` pour des listes/tuples](#exemple-avec--pour-des-listestuples)
    - [Exemple avec `**` pour des dictionnaires](#exemple-avec--pour-des-dictionnaires)
16. [Résumé des bonnes pratiques](#résumé-des-bonnes-pratiques)

## Introduction

Les fonctions sont des blocs de code réutilisables qui permettent de structurer et d'organiser un programme. Elles peuvent prendre des **paramètres** en entrée, exécuter des instructions, et renvoyer une **valeur** en sortie. Utiliser des fonctions rend le code plus clair, modulaire et facile à maintenir.

---

## Définir une fonction

Une fonction en Python est définie avec le mot-clé `def`, suivi du **nom de la fonction**, des **parenthèses** (avec ou sans paramètres) et d’un **bloc d'instructions**.

```Python
def saluer():
print("Bonjour !")

# Appel de la fonction

saluer() # Affiche : Bonjour !
```

---

## Paramètres et arguments

Les **paramètres** sont des variables définies dans la fonction, et les **arguments** sont les valeurs passées lors de l'appel.

### Exemple avec un paramètre

```Python
def saluer_utilisateur(nom):
print(f"Bonjour, {nom} !")

saluer_utilisateur("Mélanie") # Affiche : Bonjour, Mélanie !
```

### Exemple avec plusieurs paramètres

```Python
def addition(a, b):
return a + b

print(addition(3, 5)) # Affiche : 8
```

---

## Paramètres par défaut

Vous pouvez définir des valeurs par défaut pour les paramètres. Si aucun argument n'est passé, la valeur par défaut est utilisée.

```Python
def saluer(nom="inconnu"):
print(f"Bonjour, {nom} !")

saluer() # Affiche : Bonjour, inconnu !
saluer("Jean") # Affiche : Bonjour, Jean !
```

---

## Arguments positionnels et nommés

### Arguments positionnels

Les arguments sont passés dans l'ordre défini par les paramètres.

```Python
def afficher_informations(nom, age, ville):
print(f"Nom : {nom}, Âge : {age}, Ville : {ville}")

afficher_informations("Mélanie", 25, "Paris") # Positionnel
```

### Arguments nommés

Les arguments sont spécifiés par leurs noms, ce qui rend l'ordre facultatif.

```Python
afficher_informations(age=25, ville="Paris", nom="Mélanie") # Nommé
```

---

## Nombre variable d'arguments

### `*args` : Arguments positionnels variables

Utilisez `*args` pour accepter un nombre illimité d'arguments positionnels.

```Python
def addition(\*nombres):
return sum(nombres)

print(addition(1, 2, 3)) # Affiche : 6
print(addition(4, 5, 6, 7)) # Affiche : 22
```

### `**kwargs` : Arguments nommés variables

Utilisez `**kwargs` pour accepter un nombre illimité d'arguments nommés.

```Python
def afficher_infos(\*\*kwargs):
for cle, valeur in kwargs.items():
print(f"{cle} : {valeur}")

afficher_infos(nom="Mélanie", age=25, ville="Paris")
```

---

## Valeur de retour avec `return`

Une fonction peut renvoyer une ou plusieurs valeurs grâce à `return`.

### Exemple simple

```Python
def soustraction(a, b):
return a - b

print(soustraction(10, 3)) # Affiche : 7
```

### Retourner plusieurs valeurs

```Python
def calculs(a, b):
return a + b, a - b

somme, difference = calculs(10, 3)
print(somme, difference) # Affiche : 13 7
```

---

## Les fonctions anonymes (lambda)

Les **lambdas** sont des fonctions anonymes utilisées pour des opérations simples.

```Python
addition = lambda x, y: x + y
print(addition(3, 5)) # Affiche : 8
```

---

## Les Callbacks

Un **callback** est une fonction passée en paramètre d'une autre fonction.

```Python
def effectuer_operation(callback, a, b):
return callback(a, b)

def multiplication(x, y):
return x \* y

print(effectuer_operation(multiplication, 3, 5)) # Affiche : 15
```

---

## Fonctions imbriquées

Une fonction peut être définie à l'intérieur d'une autre fonction.

```Python
def exterieur():
def interieur():
print("Fonction interne exécutée")
interieur()

exterieur()
```

---

## Les décorateurs (Decorators)

Un **décorateur** permet de modifier ou étendre le comportement d'une fonction sans en modifier le code.

### Exemple de base

```Python
def decorateur(fonction):
def wrapper():
print("Avant l'exécution")
fonction()
print("Après l'exécution")
return wrapper

@decorateur
def dire_bonjour():
print("Bonjour !")

dire_bonjour()
```

### Exemple : Mesurer le temps d'exécution

```Python
import time

def mesurer_temps(fonction):
def wrapper(*args, \*\*kwargs):
debut = time.time()
resultat = fonction(*args, \*\*kwargs)
fin = time.time()
print(f"Temps d'exécution : {fin - debut:.4f} secondes")
return resultat
return wrapper

@mesurer_temps
def calcul():
time.sleep(2)
print("Opération terminée !")

calcul()
```

---

## Portée des variables (Scope)

Les variables définies dans une fonction sont locales et ne peuvent pas être utilisées en dehors de la fonction.

```Python
def exemple():
var_locale = "Je suis locale"
print(var_locale)

exemple()

# print(var_locale) # Provoque une erreur, car var_locale n'est pas définie dans la portée globale.
```

---

## Utilisation du mot-clé `global`

Pour modifier une variable globale dans une fonction, utilisez le mot-clé `global`.

```Python
compteur = 0

def incrementer():
global compteur
compteur += 1

incrementer()
print(compteur) # Affiche : 1
```

---

## Fonctions récursives

Une fonction peut s'appeler elle-même. C'est ce qu'on appelle la **récursivité**.

```Python
def factorielle(n):
if n == 0:
return 1
return n \* factorielle(n - 1)

print(factorielle(5)) # Affiche : 120
```

---

## Déballer les arguments avec `*` et `**`

### Exemple avec `*` pour des listes/tuples

```Python
def addition(a, b, c):
return a + b + c

nombres = (1, 2, 3)
print(addition(\*nombres)) # Affiche : 6
```

### Exemple avec `**` pour des dictionnaires

```Python
def afficher_infos(nom, age, ville):
print(f"Nom : {nom}, Âge : {age}, Ville : {ville}")

infos = {"nom": "Mélanie", "age": 25, "ville": "Paris"}
afficher_infos(\*\*infos)
```

---

## Résumé des bonnes pratiques

1. **Nommez vos fonctions clairement** :

   - Utilisez des noms explicites comme `calculer_somme()`.

2. **Gardez vos fonctions courtes** :

   - Une fonction doit idéalement effectuer une seule tâche.

3. **Documentez vos fonctions** :

   - Ajoutez des docstrings pour expliquer leur rôle.

4. **Utilisez des paramètres par défaut** :

   - Cela rend vos fonctions plus flexibles.

5. **Évitez les effets de bord** :
   - Minimisez les modifications des variables globales à l'intérieur des fonctions.

Avec ces concepts, vous êtes prêt à écrire des fonctions Python robustes et réutilisables ! 🚀
