# 🛠️ 9. Exercices Pratiques 🎯

### Exercice 1 : Noms valides

Parmi les noms suivants, lesquels sont valides ?

- `1var`, `_variable`, `nom utilisateur`, `if`, `ma_variable`
<details>
  <summary><b>Solution</b></summary>
  <h2>Exercice 1 : Noms valides ✅</h2>

<p>Parmi les noms suivants, lesquels sont valides ?</p>

<table>
  <thead>
    <tr>
      <th><strong>Nom</strong></th>
      <th><strong>Est valide ?</strong></th>
      <th><strong>Explication</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>1var</code></td>
      <td>❌ Non</td>
      <td>Les noms de variables ne peuvent pas commencer par un chiffre.</td>
    </tr>
    <tr>
      <td><code>_variable</code></td>
      <td>✅ Oui</td>
      <td>Les noms de variables peuvent commencer par un underscore <code>_</code>.</td>
    </tr>
    <tr>
      <td><code>nom utilisateur</code></td>
      <td>❌ Non</td>
      <td>Les espaces ne sont pas autorisés dans les noms de variables.</td>
    </tr>
    <tr>
      <td><code>if</code></td>
      <td>❌ Non</td>
      <td><code>if</code> est un mot-clé réservé en Python et ne peut pas être utilisé comme nom.</td>
    </tr>
    <tr>
      <td><code>ma_variable</code></td>
      <td>✅ Oui</td>
      <td>Ce nom respecte les conventions : lettres, underscores, pas de mots réservés.</td>
    </tr>
  </tbody>
</table>

<h3>Résumé 📋 :</h3>
<ul>
  <li>Un nom de variable doit commencer par une lettre (<code>a-z</code>, <code>A-Z</code>) ou un underscore <code>_</code>.</li>
  <li>Il ne peut pas commencer par un chiffre.</li>
  <li>Les espaces et caractères spéciaux ne sont pas autorisés.</li>
  <li>Les mots-clés réservés de Python (comme <code>if</code>, <code>while</code>, <code>def</code>, etc.) ne peuvent pas être utilisés.</li>
</ul>

</details>

### Exercice 2 : Conversion de types

Convertir les types des variables suivantes :

```Python
age_str = "30"
age_float = 25.5

# À convertir

age = int(age_str) # ?
age_texte = str(age_float) # ?
```

### Exercice 3 : Trouver les erreurs

Parmi les déclarations de variables ci-dessous, identifiez celles qui contiennent des erreurs et corrigez-les.

```Python
1var = 10  # ?
nom utilisateur = "Alice"  # ?
nom-utilisateur = "Bob"  # ?
import = "mot réservé"  # ?
_variable = 42  # ?
```

---

### Exercice 4 : Calcul avec des variables

Créez un programme qui demande à l'utilisateur de saisir deux nombres, les additionne, et affiche le résultat.

**Instructions :**

1. Déclarez deux variables pour stocker les entrées de l'utilisateur.
2. Convertissez ces entrées en nombres entiers ou flottants.
3. Calculez la somme et affichez-la.

Exemple attendu :
Entrez le premier nombre : 10 Entrez le second nombre : 5 La somme est : 15

```Python
# Exemple de solution
nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le second nombre : ")

# Conversion des entrées en nombres
nombre1 = float(nombre1)
nombre2 = float(nombre2)

# Calcul de la somme
somme = nombre1 + nombre2

# Affichage du résultat
print(f"La somme est : {somme}")
```

---

### Exercice 5 : Portée des variables

Analyser et comprendre le comportement des variables locales et globales dans le code suivant.

```Python
compteur = 10

def incrementer_local():
    compteur = 5
    compteur += 1
    print("Valeur locale :", compteur)

def incrementer_global():
    global compteur
    compteur += 1
    print("Valeur globale :", compteur)

incrementer_local()  # ?
incrementer_global()  # ?
print("Valeur finale :", compteur)  # ?
```

---

Ces exercices permettent de travailler sur des concepts essentiels comme :

- Les noms valides des variables (Exercice 3).
- L'interaction avec l'utilisateur et la conversion des types (Exercice 4).
- La portée des variables et leur comportement (Exercice 5). 😊
