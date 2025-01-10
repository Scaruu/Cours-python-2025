# 🛠️ Exercices pratiques sur les fonctions en Python

### Exercice 1 : Création d'une fonction basique

Créez une fonction `dire_bonjour` qui affiche "Bonjour à tous !". Appelez ensuite cette fonction trois fois.

---

### Exercice 2 : Calcul avec des paramètres

Créez une fonction `calculer_somme` qui prend deux paramètres et retourne leur somme. Testez-la avec les valeurs `5` et `10`.

---

### Exercice 3 : Valeur par défaut

Créez une fonction `saluer` qui prend un paramètre `nom` avec une valeur par défaut `"inconnu"`. La fonction doit afficher : "Bonjour, [nom] !".

- **Exemple** :
  - `saluer("Alice")` doit afficher : Bonjour, Alice !
  - `saluer()` doit afficher : Bonjour, inconnu !

---

### Exercice 4 : Fonction avec `*args`

Créez une fonction `moyenne` qui accepte un nombre variable d'arguments (`*args`) et retourne la moyenne des nombres passés.

- **Exemple** :
  - `moyenne(10, 20, 30)` doit retourner `20.0`.

---

### Exercice 5 : Décorateur pour mesurer le temps d'exécution

Créez un décorateur `mesurer_temps` qui mesure le temps d'exécution d'une fonction.

- Appliquez ce décorateur à une fonction `compter` qui affiche les nombres de `1` à `5` avec une pause de `1 seconde` entre chaque nombre (utilisez `time.sleep(1)`).

**Indice** : Importez le module `time` pour mesurer le temps.

---

Ces exercices vous aideront à renforcer vos compétences sur les fonctions en Python en abordant différents concepts comme les paramètres, les valeurs par défaut, les arguments variés, et les décorateurs ! 🚀
