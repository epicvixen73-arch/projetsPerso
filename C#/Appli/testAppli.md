# Test App (Calculatrice + Minigame)

Une **application console intégrée en C#** combinant une calculatrice scientifique et un minigame de devinette, avec menu de navigation central.
Lien du fichier si envie de tester: [TesAppli.cs](https://github.com/epicvixen73-arch/projetsPerso/blob/main/C%23/Appli/testAppli.cs)

## Fonctionnalités Principales

### Module Calculatrice (Option 1)
Identique au projet `Calculatrice.cs` :
- **5 Opérateurs** — Addition, Soustraction, Multiplication, Division, Reste
- **5 Fonctions** — Carré, Cube, Racine Carrée, Valeur Absolue, Inverse
- **Calcul de puissances** — `a^n`
- Architecture orientée objet avec classes abstraites

### Module Minigame (Option 2)
Un **jeu de devinette « Juste Prix »** :
- Devinez un nombre entre **0 et 50**
- **5 tentatives** pour y parvenir
- Feedback : « La valeur est supérieur/inférieur »
- Gagnez si votre guess est à ±1 du nombre secret
- Affichage du nombre de tentatives restantes

## Architecture Globale

```
Program
├── Main() → Menu Principal (3 options)
│
├── [1] Calculatrice
│   ├── abstract class Operation
│   │   ├── Addition, Soustraction, Multiplication, Division, Reste
│   │   └── Calcul(a, b) & GetName()
│   │
│   ├── abstract class Fonctions
│   │   ├── Carre, Cube, Inverse, Racine, Absolue
│   │   └── Fonction(a) & GetName()
│   │
│   └── Logic
│       ├── Menu d'opérateurs/fonctions
│       ├── Saisie des paramètres
│       └── Affichage résultat
│
├── [2] Juste Prix
│   ├── Random.Next(0, 51) → Génère nombre à deviner
│   ├── Loop (5 tentatives)
│   │   ├── Saisir guess utilisateur
│   │   ├── Comparer avec ±1
│   │   └── Feedback + décrémenter tentatives
│   └── Affichage du résultat final
│
└── [3] Quitter
    └── return;
```

## Flux d'Utilisation Principal

```
┌──────────────────────────────────────┐
│      === Test_App ===                │
│  1: Calculatrice                     │
│  2: Juste Prix                       │
│  3: Quitter                          │
│  Choix:                              │
└──────────────────────────────────────┘
         │
    ┌────┼────┬─────────┐
    ▼    ▼    ▼         ▼
   [1]  [2]  [3]      ...
    │    │    │
    ▼    ▼    ▼
  Calc JustePrix Quit
```

## État du Jeu « Juste Prix »

| Variable | Type | Description |
|----------|------|-------------|
| `random` | `Random` | Générateur de nombre aléatoire |
| `valueToGuess` | `int` | Nombre secret (0-50) |
| `guess` | `int` | Entrée utilisateur |
| `nbGuess` | `int` | Tentatives restantes (décrémente) |
| `hasWon` | `bool` | Flag de victoire |

## Logique du Minigame

```csharp
while (nbGuess > 0 && !hasWon) {
    // Demande un guess
    if (Saisir(..., out guess, 51)) {
        
        // Vérification ±1
        if (guess == valueToGuess - 1 ||
            guess == valueToGuess ||
            guess == valueToGuess + 1) {
            hasWon = true;
            Console.WriteLine("Tu as gagné !");
        } else {
            // Feedback directif
            Console.WriteLine(
                valueToGuess > guess ? 
                "La valeur est supérieur" : 
                "La valeur est inférieur"
            );
        }
    }
    nbGuess--;
    Console.WriteLine($"{nbGuess} / 5 essai(s) restant(s).");
}
```

## Flux Calculatrice dans TestAppli

Identique à `Calculatrice.cs` mais encapsulé dans un `case 1` de switch :

1. Initialise `operations` & `fonctions` (listes)
2. Boucle interne avec flag `quitCalc`
3. Menu d'opérateurs/puissances/fonctions
4. Validation des choix avec `Saisir()` surchargé
5. Affichage du résultat
6. Continue ou quitte vers le menu principal

## Méthodes Partagées

### `bool Saisir(string message, out int userChoice, int borne)`
Récupère un **entier** avec validation dans `[1, borne]`

### `bool Saisir(string message, out float userChoice, float borne)`
Récupère un **float** avec validation dans `[1, borne]`

### `bool IsInBorne(float choix, float borne)`
Vérifie les limites : `choix >= 1 && choix <= borne`

## Utilisation

```bash
# Compiler
csc TestAppli.cs

# Exécuter
./TestAppli.exe

# Menu initial
===  Test_App  ===
1: Calculatrice
2: Juste Prix
3: Quitter
Choix: 2

# Minigame
Ton guess: 25
La valeur est inférieur
4 / 5 essai(s) restant(s).
Ton guess: 20
Tu as gagné !
Fin du jeu, merci d'y avoir joué ! La valeur était : 21
```

## Points de Contrôle

### Calculatrice
✅ Validation entrée avec `TryParse`  
✅ Vérification bornes pour sélection menu  
✅ Gestion division par zéro (✓ implicite avec Try-Catch envisageable)  
✅ Boucle infinie jusqu'à quitter (case 4)

### Juste Prix
- Génération aléatoire `Random.Next(0, 51)`  
- Compteur de tentatives (décrémente chaque essai)  
- Feedback directif (supérieur/inférieur)  
- Condition de victoire : `±1` autour du nombre secret  
- Affichage du nombre secret en fin de partie

## Notes Techniques

- **Namespace** — `Test_App`
- **Framework** — .NET Console Application
- **Classe parente** — Tous les opérateurs/fonctions héritent de leurs abstraites
- **Polymorphisme** — Même interface `Calcul()` / `Fonction()`, implémentations multiples
- **Surcharge** — `Saisir()` en 2 versions (`int`, `float`)
- **Gestion d'erreurs** — TryParse + boucle de retry

## Concepts OOP Démontrés

- **Classe abstraite** — `Operation`, `Fonctions`  
- **Héritage** — 5 implémentations de chaque  
- **Polymorphisme** — Appels uniformes, comportements divers  
- **Surcharge de méthode** — `Saisir()` pour `int` et `float`  
- **Énumération de collection** — `foreach` implicite dans les menus  
- **Contrôle de flux** — `while`, `switch`, flags `quitCalc`, `hasWon`

## Améliorations Possibles

- [ ] Gérer division par zéro avec try-catch
- [ ] Ajouter historique des calculs
- [ ] Options de difficulté pour le minigame (nb tentatives, range)
- [ ] Score cumulatif entre sessions
- [ ] Persistance en fichier (JSON/CSV)
