# Calculatrice en C#

Une **calculatrice console interactive** en C# avec architecture orientée objet utilisant les classes abstraites et l'héritage.

The file if you want to test by yourself: [calculatrice.cs]()

## Fonctionnalités

### Opérateurs Arithmétiques
- **Addition** — `a + b`
- **Soustraction** — `a - b`
- **Multiplication** — `a × b`
- **Division** — `a ÷ b`
- **Reste (modulo)** — `a % b`

### Fonctions Mathématiques
- **Carré** — `x²` (utilise `Math.Pow`)
- **Cube** — `x³`
- **Racine Carrée** — `√x`
- **Valeur Absolue** — `|x|`
- **Inverse** — `1/x`

### Puissances
- Calcul de **`a^n`** pour tout exposant entier

## Architecture

```
Program
├── abstract class Operation
│   ├── Addition
│   ├── Soustraction
│   ├── Multiplication
│   ├── Division
│   └── Reste
│
├── abstract class Fonctions
│   ├── Carre
│   ├── Cube
│   ├── Racine
│   ├── Absolue
│   └── Inverse
│
└── Helper Methods
    ├── Saisir(string, out int, int)
    ├── Saisir(string, out float, float)
    └── IsInBorne(float, float)
```

### Points Clés
- **Classes abstraites** — `Operation` et `Fonctions` définissent les contrats
- **Polymorphisme** — Chaque opération/fonction implémente `Calcul()` / `Fonction()`
- **Validation d'entrée** — Méthode surchargée `Saisir()` pour `int` et `float`
- **Gestion des bornes** — Vérification que l'entrée utilisateur est dans la plage valide

## Flux d'Utilisation

```
┌─────────────────────────────────────┐
│  Menu Principal                     │
│  [1] Opérateur [2] Puissances       │
│  [3] Fonctions [4] Quit             │
└─────────────────────────────────────┘
         │
    ┌────┴────┬────────┬──────────┐
    ▼         ▼        ▼          ▼
 Saisir    Entrer   Choisir    Quitter
 opérateur a & b   fonction
    │         │        │
    └─────────┴────────┘
         ▼
    Calcul & Affichage
    du résultat
```

## Variables Principales

| Variable | Type | Description |
|----------|------|-------------|
| `operations` | `List<Operation>` | Liste des 5 opérateurs disponibles |
| `fonctions` | `List<Fonctions>` | Liste des 5 fonctions disponibles |
| `choix` | `int` | Choix du menu principal (1-4) |
| `a_ope`, `b` | `float` | Opérandes pour les calculs |
| `x` | `float` | Argument pour une fonction |

## ⚙️ Méthodes de Validation

### `bool Saisir(string message, out int choix, int borne)`
Récupère un **entier** avec validation dans la plage `[1, borne]`

### `bool Saisir(string message, out float choix, float borne)`
Récupère un **float** avec validation dans la plage `[1, borne]`

### `bool IsInBorne(float choix, float borne)`
Vérifie que le choix respecte les limites

## Utilisation

```bash
# Compiler
csc calculatrice.cs

# Exécuter
./calculatrice.exe

# Exemple d'interaction
#######################
-----[1]: Opérateur----
-----[2]: Puissances---
-----[3]: Fonctions----
-----[4]: Quit---------
Choix: 1

-------Opérateur-------
[1] Addition
[2] Soustraction
[3] Multiplication
[4] Division
[5] Reste
Choix: 1
-----------------------
a: 10
b: 5
Result: 15
```

## Notes Techniques

- **Namespace** — `Calculatrice`
- **Framework** — .NET (Console Application)
- **Type numérique** — `float` pour les calculs (peut être changé en `double` pour plus de précision)
- **Gestion des erreurs** — TryParse avec boucle de retry sur entrée invalide

## Flux de Boucle Principale

1. Affiche le menu principal
2. Récupère le choix utilisateur (validé)
3. En fonction du choix :
   - **Cas 1** : Sélectionne une opération, demande `a` et `b`, affiche le résultat
   - **Cas 2** : Demande `a` et `n`, calcule `a^n`
   - **Cas 3** : Sélectionne une fonction, demande `x`, affiche le résultat
   - **Cas 4** : Quitte la boucle
4. Boucle jusqu'à quitter

## Concepts OOP Utilisés

- **Classes abstraites** — Définissent l'interface commune  
- **Héritage** — Chaque opération/fonction hérite de sa classe abstraite  
- **Polymorphisme** — Même appel `Calcul()` / `Fonction()`, implémentations différentes  
- **Énumération de collection** — Parcours des listes d'opérations/fonctions  
- **Surcharge de méthode** — `Saisir()` existe en 2 versions (`int`, `float`)
