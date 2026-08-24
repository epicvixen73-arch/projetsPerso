# Minigame « Juste Prix » en C#

Un **jeu de devinette simple mais efficace** écrit en C# avec validation d'entrée et feedback interactif.

Le lien si vous voulez testez: [Minigame_Juste-Prix.cs](https://github.com/epicvixen73-arch/Projects/blob/main/CSharp/Minigame/Minigame%20%22Juste_ptrix%22.cs)

## Règles du Jeu

| Aspect | Détail |
|--------|--------|
| **Objectif** | Devinez un nombre secret entre **0 et 50** |
| **Tentatives** | Vous avez **5 essais** |
| **Condition de victoire** | Votre guess est exact **ou à ±1** du nombre |
| **Feedback** | Le jeu vous indique si le secret est supérieur/inférieur |
| **Fin de partie** | Affichage du nombre secret après 5 tentatives ou victoire |

## Architecture

```
Program
├── Main()
│   ├── Initialisation
│   │   ├── Random al = new Random()
│   │   ├── int NbGuess = 5
│   │   ├── int valueToGuess = al.Next(0, 51)
│   │   └── int Score = 0 (0=perdu, 1=gagné)
│   │
│   └── Boucle de jeu
│       ├── while (NbGuess > 0 && Score == 0)
│       │   ├── Appel Saisir(..., valueToGuess)
│       │   ├── Si valide → IsInBorne()
│       │   ├── Si victoire → Score = 1
│       │   ├── Sinon → Feedback
│       │   └── Décrémenter NbGuess
│       │
│       └── Fin du jeu → Affichage résultat
│
├── bool Saisir(string, out int, int)
│   └── Validation d'entrée utilisateur
│
└── bool IsInBorne(float, float)
    └── Vérification ±1 du nombre secret
```

## Logique de Victoire

Pour **gagner**, votre guess doit satisfaire l'une de ces conditions :
```csharp
guess == aleatoire - 1   // Un en dessous
|| guess == aleatoire    // Exact !
|| guess == aleatoire + 1 // Un au-dessus
```

Cette mécanique rend le jeu **plus accessible** sans être trivial.

## Variables Clés

| Variable | Type | Valeur/Rôle |
|----------|------|------------|
| `al` | `Random` | Générateur pseudo-aléatoire |
| `valueToGuess` | `int` | Nombre secret (0-50) |
| `UserGuess` | `int` | Entrée utilisateur |
| `NbGuess` | `int` | Compteur (5 → 0) |
| `Score` | `int` | 0=En cours, 1=Victoire |
| `Credit` | `string` | Message de fin |

## Flux d'Exécution

```
┌─────────────────────────────────┐
│ Initialiser Random & Nombre     │
│ aleatoire ∈ [0, 51[             │
│ NbGuess = 5                     │
│ Score = 0                       │
└──────────────┬──────────────────┘
               │
        ┌──────▼───────────────┐
        │ while (NbGuess>0 &&  │
        │        Score==0)     │
        └──────┬───────────────┘
               │
        ┌──────▼──────────────┐
        │ Demander guess      │
        │ utilisateur         │
        └──────┬──────────────┘
               │
        ┌──────▼──────────────┐
        │ Valider entrée      │
        │ IsInBorne()         │
        └──────┬──────────────┘
               │
        ┌──┬───▼────┬──┐
        ▼  ▼        ▼  ▼
      Perdu  Exact ±1  ...
        │     │     │
        ▼     ▼     ▼
      Feedback Victoire
        │             │
        └──────┬──────┘
               │
        NbGuess--
        │
        └─────► (retour à la boucle)
```

## Utilisation

```bash
# Compiler
csc "Minigame Juste_ptrix.cs"

# Exécuter
./"Minigame Juste_ptrix.exe"

# Exemple de session
Ton guess: 25
Choix valide !
Choix invalide !    [Le nombre était ≠ 25±1]
4 / 5 essai(s) restant(s).

Ton guess: 30
Choix valide !
0 / 5 essai(s) restant(s).

Fin du jeu, merci d'y avoir joué !
```

## Méthodes

### `bool Saisir(string message, out int UserGuess, int aleatoire)`

**Rôle** — Récupère l'entrée utilisateur et la valide  
**Paramètres** :
- `message` : Texte à afficher à l'utilisateur
- `UserGuess` : La valeur saisie (sortie)
- `aleatoire` : Le nombre à deviner (pour IsInBorne)

**Logique** :
1. Affiche le message
2. Boucle infinie :
   - Lit une ligne
   - Essaie de parser en `int`
   - Si succès → appelle `IsInBorne()` et retourne le résultat
   - Si échec → affiche « Invalide, reboot... » et retourne `false`

### `bool IsInBorne(float UserGuess, float aleatoire)`

**Rôle** — Vérifie si le guess est dans la zone de victoire  
**Logique** :
```csharp
if (UserGuess == aleatoire - 1 || 
    UserGuess == aleatoire || 
    UserGuess == aleatoire + 1) {
    Console.WriteLine("Choix valide !");
    return true;
} else {
    Console.WriteLine("Choix invalide !");
    return false;
}
```

## Notes Techniques

- **Namespace** — `Juste_prix`
- **Framework** — .NET Console Application
- **Génération aléatoire** — `Random.Next(0, 51)` → entiers de 0 à 50 (51 exclu)
- **Validation** — `int.TryParse()` avec boucle de retry
- **Affichage** — Console.Write / Console.WriteLine

## Points de Conception

- **Gestion d'erreurs** — Entrée invalide → redemande avec retry  
- **Feedback clair** — Indique si le guess est supérieur/inférieur  
- **Compteur visuel** — Affiche tentatives restantes après chaque essai  
- **Condition de victoire généreuse** — Accepte ±1 pour plus de fun  
- **Boucle simple** — Contrôle par flags `NbGuess` et `Score`

## Exemple d'État de Jeu

| Étape | `aleatoire` | `guess` | `NbGuess` | `Score` | Résultat |
|-------|------------|---------|-----------|---------|----------|
| Initial | 25 | - | 5 | 0 | En cours |
| Essai 1 | 25 | 20 | 5 | 0 | Invalide (< 24) |
| Essai 2 | 25 | 26 | 4 | 0 | Valide ! ±1 ✓ |
| Final | 25 | 26 | 4 | 1 | **Victoire** |

## Améliorations Possibles

- [ ] **Score par difficulté** — Moins de tentatives = plus de points
- [ ] **Modes de jeu** — Facile (0-20), Normal (0-50), Difficile (0-100)
- [ ] **Leaderboard** — Persistance des meilleurs temps
- [ ] **Feedback plus riche** — « Tu es chaud ! » vs « Froid »
- [ ] **Son/Vibration** — Feedback auditif sur victoire
- [ ] **Menu de rejouer** — Option pour relancer une partie sans redémarrer

## Expérience Utilisateur

**Positifs** :
- Mécanique simple et accessible
- Feedback immédiat (supérieur/inférieur)
- Compteur de tentatives motivant
- Affichage du nombre secret à la fin

**À améliorer** :
- Pas de score cumulatif
- Pas de difficulté progressive
- Message de fin un peu abrupt
- Pas d'option « rejouer »

## Concepts C# Utilisés

- **Classe `Random`** — Génération de nombres aléatoires  
- **Surcharge de méthode** — Pas multiple `Saisir()` (une seule)  
- **Validation avec TryParse** — Gestion d'erreur de parsing  
- **Boucles (`while`)** — Retry sur erreur, jeu principal  
- **Conditions (`if`/`else`)** — Feedback directif  
- **Flags (`NbGuess`, `Score`)** — Contrôle de flux
