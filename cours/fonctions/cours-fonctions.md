# 📚 Cours complet : Les Fonctions en Python

## Introduction

Les fonctions sont des blocs de code réutilisables qui permettent de structurer et d'organiser un programme. Elles peuvent prendre des **paramètres** en entrée, exécuter des instructions, et renvoyer une **valeur** en sortie.

---

## ✨ Définir une fonction

Une fonction en Python est définie à l'aide du mot-clé `def`, suivi du **nom de la fonction**, des **parenthèses** (avec ou sans paramètres), et d'un bloc d'instructions.

```Python
def saluer():
    print("Bonjour !")

# Appel de la fonction
saluer()  # Affiche : Bonjour !
```

---

## 📥 Paramètres et arguments

Les **paramètres** sont des variables définies dans la fonction, et les **arguments** sont les valeurs passées lors de l'appel.

### Exemple avec un paramètre

```Python
def saluer_utilisateur(nom):
    print(f"Bonjour, {nom} !")

saluer_utilisateur("Mélanie")  # Affiche : Bonjour, Mélanie !
```

---

## 🔄 Valeur de retour avec `return`

Une fonction peut renvoyer une valeur grâce au mot-clé `return`.

```Python
def addition(a, b):
    return a + b

resultat = addition(5, 3)
print(resultat)  # Affiche : 8

```

---

## 🚀 Fonctions avec plusieurs paramètres

Python permet de définir des fonctions avec plusieurs paramètres.

```Python
def soustraction(a, b, c):
    return a - b - c

print(soustraction(10, 3, 2))  # Affiche : 5
```

---

## 🛠️ Paramètres par défaut

Les paramètres peuvent avoir des valeurs par défaut. Si aucun argument n'est passé, la valeur par défaut est utilisée.

```Python
def saluer(nom="inconnu"):
    print(f"Bonjour, {nom} !")

saluer()  # Affiche : Bonjour, inconnu !
saluer("Jean")  # Affiche : Bonjour, Jean !
```

---

## 🌟 Arguments positionnels et nommés

Python permet de passer des arguments **par position** ou **par nom**.

```Python
def afficher_informations(nom, age, ville):
    print(f"Nom : {nom}, Âge : {age}, Ville : {ville}")

# Arguments positionnels
afficher_informations("Mélanie", 25, "Paris")

# Arguments nommés
afficher_informations(age=25, ville="Paris", nom="Mélanie")
```

---

## 🔢 Nombre variable d'arguments

### 1. Arguments positionnels variables (`*args`)

Utilisez `*args` pour accepter un nombre illimité d'arguments positionnels.

```Python
def addition(*nombres):
    return sum(nombres)

print(addition(1, 2, 3))  # Affiche : 6
print(addition(4, 5, 6, 7, 8))  # Affiche : 30
```

### 2. Arguments nommés variables (`**kwargs`)

Utilisez `**kwargs` pour accepter un nombre illimité d'arguments nommés.

```Python
def afficher_infos(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle} : {valeur}")

afficher_infos(nom="Mélanie", age=25, ville="Paris")
```

---

## 🔄 Les fonctions anonymes (lambda)

Les **lambdas** sont des fonctions anonymes, généralement utilisées pour des opérations simples.

```Python
addition = lambda a, b: a + b
print(addition(5, 3))  # Affiche : 8
```

---

## 🔄 Les Callbacks

Un **callback** est une fonction passée en argument à une autre fonction et appelée à l'intérieur de cette fonction.

### Exemple simple

```Python
def effectuer_operation(callback, a, b):
    return callback(a, b)

def addition(x, y):
    return x + y

print(effectuer_operation(addition, 5, 3))  # Affiche : 8
```

---

## 📜 Fonctions imbriquées

Une fonction peut être définie à l'intérieur d'une autre.

```Python
def fonction_principale():
    def fonction_interne():
        print("Fonction interne exécutée")
    fonction_interne()

fonction_principale()
```

---

## 🏭 Fonctions comme objets de première classe

En Python, les fonctions sont des objets. Elles peuvent être assignées à des variables, passées comme arguments, ou retournées par d'autres fonctions.

### Exemple

```Python
def dire_bonjour():
    return "Bonjour !"

message = dire_bonjour
print(message())  # Affiche : Bonjour !
```

---

## 🌟 Portée des variables (scope)

Les variables définies dans une fonction ont une portée locale, sauf si elles sont déclarées globales.

```Python
def afficher_message():
    message = "Ceci est un message local"
    print(message)

afficher_message()
# print(message)  # Erreur : la variable n'existe pas dans la portée globale
```

---

## ⚙️ Utilisation du mot-clé `global`

Pour modifier une variable globale à l'intérieur d'une fonction, utilisez `global`.

```Python
compteur = 0

def incrementer_compteur():
    global compteur
    compteur += 1

incrementer_compteur()
print(compteur)  # Affiche : 1
```

---

## 🔄 Fonctions récursives

Une fonction peut s'appeler elle-même. C'est ce qu'on appelle la **récursivité**.

### Exemple : Factorielle

```Python
def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))  # Affiche : 120
```

---

## 🔢 Déballer les arguments avec `*` et `**`

### Exemple avec `*` (pour des listes/tuples)

```Python
def addition(a, b, c):
    return a + b + c

nombres = (1, 2, 3)
print(addition(*nombres))  # Affiche : 6
```

### Exemple avec `**` (pour des dictionnaires)

```Python
def afficher_infos(nom, age, ville):
    print(f"Nom : {nom}, Âge : {age}, Ville : {ville}")

infos = {"nom": "Mélanie", "age": 25, "ville": "Paris"}
afficher_infos(**infos)
```

---

## 🛠️ Les décorateurs (Decorators)

Un **décorateur** (en anglais, _decorator_) est une fonction spéciale qui permet de **modifier**, **étendre** ou **personnaliser** le comportement d'une autre fonction ou méthode, sans modifier directement son code.

Les décorateurs sont souvent utilisés pour :

1. **Ajouter des fonctionnalités** : Par exemple, enregistrer les appels à une fonction, mesurer son temps d'exécution, ou valider ses entrées.
2. **Réutilisation du code** : Les décorateurs permettent d'appliquer une logique commune à plusieurs fonctions sans duplication de code.
3. **Interopérabilité** : Dans des frameworks comme Django ou Flask, les décorateurs sont utilisés pour associer des routes, valider des requêtes ou gérer l'authentification.
4. **Aspect-Oriented Programming (AOP)** : Ils permettent d’isoler des aspects transversaux (logging, sécurité, etc.) du code métier principal.

### Exemple de base : Ajouter des messages avant et après l’exécution d’une fonction

```Python
def decorateur(fonction):
    def wrapper():
        print("Avant l'exécution")
        fonction()
        print("Après l'exécution")
    return wrapper

@decorateur
def saluer():
    print("Bonjour !")

saluer()

### Résultat
Avant l'exécution
Bonjour !
Après l'exécution
```

---

### Quand utiliser un décorateur ?

- **Mesurer la performance** d'une fonction (temps d'exécution, appels multiples, etc.).
- **Enregistrer des logs** pour suivre les activités d'une fonction.
- **Valider les paramètres** passés à une fonction avant son exécution.
- **Gérer l'accès ou l'authentification** dans des applications Web.
- **Transformer les résultats** renvoyés par une fonction (ex. : convertir une sortie brute en JSON).

---

### Exemple pratique : Mesurer le temps d'exécution

```Python
import time

def mesurer_temps(fonction):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        print(f"Temps d'exécution de {fonction.__name__}: {fin - debut:.4f} secondes")
        return resultat
    return wrapper

@mesurer_temps
def calculer():
    time.sleep(2)  # Simule une opération longue
    print("Calcul terminé !")

calculer()
```

---

### Exemple pratique : Valider les paramètres

```Python
def valider_entrees(fonction):
    def wrapper(*args, **kwargs):
        for valeur in args:
            if not isinstance(valeur, int):
                raise ValueError(f"Tous les paramètres doivent être des entiers ! (Reçu : {valeur})")
        return fonction(*args, **kwargs)
    return wrapper

@valider_entrees
def additionner(a, b):
    return a + b

print(additionner(5, 10))  # Affiche : 15
# print(additionner(5, "10"))  # Erreur : Tous les paramètres doivent être des entiers !
```

---

### Exemple pratique : Ajouter une fonctionnalité de logging

```Python
def logger(fonction):
    def wrapper(*args, **kwargs):
        print(f"Appel de {fonction.__name__} avec les arguments {args} et {kwargs}")
        resultat = fonction(*args, **kwargs)
        print(f"Résultat : {resultat}")
        return resultat
    return wrapper

@logger
def multiplier(a, b):
    return a * b

multiplier(3, 5)
```

---

### Points importants à retenir

1. **Syntaxe simplifiée avec `@`** :  
   Utiliser `@decorateur` avant la définition d'une fonction est une manière concise d'appliquer un décorateur. Cela revient à écrire :

   ```Python
   saluer = decorateur(saluer)
   ```

2. **Flexibilité** :  
   Les décorateurs peuvent être combinés en les empilant :

   ```Python
   @logger
   @mesurer_temps
   def exemple():
       print("Fonction exécutée !")
   ```

3. **Utilisation avec des arguments** :  
    Les décorateurs peuvent eux-mêmes accepter des arguments pour plus de flexibilité. Cela nécessite une **fonction génératrice de décorateurs**.

   Exemple :

   ```Python
   def decorateur_avec_parametre(param):
       def decorateur(fonction):
           def wrapper(*args, **kwargs):
               print(f"Décorateur avec paramètre : {param}")
               return fonction(*args, **kwargs)
           return wrapper
       return decorateur

   @decorateur_avec_parametre("Mon paramètre")
   def exemple():
       print("Fonction décorée")

   exemple()
   ```

   Avec ces exemples, les décorateurs deviennent un outil puissant pour améliorer, personnaliser et organiser votre code Python. 🚀

---

## Résumé des bonnes pratiques des fonctions

1. **Nommez vos fonctions clairement** :

   - Utilisez des noms descriptifs comme `calculer_somme()` au lieu de `cs()`.

2. **Gardez les fonctions courtes** :

   - Une fonction doit idéalement faire une seule chose.

3. **Utilisez des valeurs par défaut** pour les paramètres optionnels :

   - Cela rend vos fonctions plus flexibles.

4. **Documentez vos fonctions** :

   - Ajoutez des commentaires ou des docstrings pour expliquer leur comportement.

5. **Évitez les effets de bord** :
   - Les fonctions ne doivent pas modifier des variables globales sans raison.

Avec ces concepts, vous êtes prêt à écrire des fonctions Python puissantes, réutilisables et élégantes ! 🚀
