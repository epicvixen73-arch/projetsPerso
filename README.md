# Personal Projects Portfolio

> *Building, breaking, and learning through code. A collection of experimental tools, games, and utilities crafted to solve problems and explore software architecture.*

## About This Repository

Welcome to my personal development sandbox. This repository is a living document of my coding journey, where I experiment with different languages, test architectural patterns, and build functional tools from scratch. 

Rather than just showcasing perfect code, this space highlights the *process*: the logic behind a console game, the cross-platform adaptation of a utility, and the iterative refinement of application structure. Each project represents a specific learning milestone, designed to be functional, intuitive, and progressively optimized.

[Python](https://github.com/epicvixen73-arch/projetsPerso/tree/main#-python-logic-utilities--cross-platform-adaptation)

[C++](https://github.com/epicvixen73-arch/projetsPerso/tree/main#%EF%B8%8F-c-algorithmic-foundations)

[C#](https://github.com/epicvixen73-arch/projetsPerso/tree/main#-c-object-oriented-design--refactoring)

---

## 📂 Featured Projects

### 🐍 Python: Logic, Utilities & Cross-Platform Adaptation
Python is my primary environment for rapid prototyping, algorithmic experimentation, and building user-centric tools.

- **Automation Tools** ([Python/Tools/](https://github.com/epicvixen73-arch/projetsPerso/tree/main/Python/Tools))
  - **[converterNumworks.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Tools/converterNumworks.py) & [fullconverter.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Tools/fullconverter.py)**: Custom utilities designed to automate data and format conversions. These scripts eliminate manual, repetitive tasks, demonstrating a focus on practical problem-solving and workflow optimization.
- **Interactive Console Games** ([Python/Minijeux/](https://github.com/epicvixen73-arch/projetsPerso/tree/main/Python/Minijeux))
  - **[roulette.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Minijeux/roulette.py)**: A fully functional terminal-based betting simulation. Users can wager on color, parity, or specific numbers. It implements dynamic state management (tracking player balance in real-time) and robust conditional logic, terminating gracefully when the balance reaches zero.
  - **[dices.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Minijeux/dices.py) & [rockPaperScissors.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Minijeux/rockPaperScissors.py)**: Lightweight, interactive games focusing on clean user input handling, random logic generation, and immediate feedback loops.
- **Modular Calculator Architecture** ([Python/Calculatrice/](https://github.com/epicvixen73-arch/projetsPerso/tree/main/Python/Calculatrice))
  - **PC Version** ([PC/main.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Calculatrice/PC/main.py) + [PC/formules.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Calculatrice/PC/formules.py) + [PC/calcCsharpRefac.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Calculatrice/PC/calcCsharpRefac.py)): A desktop calculator showcasing modular architecture. By separating the core mathematical logic (`formules.py`) from the main execution flow (`main.py`), the code remains clean, testable, and easy to extend.
  - **NumWorks Version** ([Numworks/main_n.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Calculatrice/Numworks/main_n.py) + [Numworks/formulesn.py](https://github.com/epicvixen73-arch/projetsPerso/blob/main/Python/Calculatrice/Numworks/formulesn.py)): A tailored adaptation of the calculator for the NumWorks graphing calculator environment. This highlights my ability to adapt code to strict hardware and OS constraints while maintaining core functionality.

### ⚙️ C++: Algorithmic Foundations
- **Number Guessing Game** ([CPP/justePrix.cpp](https://github.com/epicvixen73-arch/projetsPerso/blob/main/CPP/justePrix.cpp))
  - **What it does**: A classic "Juste Prix" (Guess the Number) game with dynamic feedback loops.
  - **Why it matters**: Built to master fundamental C++ syntax, random number generation, and efficient loop structures without the overhead of high-level frameworks, focusing purely on algorithmic thinking and memory awareness.

### 💻 C#: Object-Oriented Design & Refactoring
- **Application Testbed** ([C#/Appli/testAppli.cs](https://github.com/epicvixen73-arch/projetsPerso/blob/main/C%23/Appli/testAppli.cs))
  - **What it does**: A structured environment for exploring and validating object-oriented principles.
  - **Why it matters**: Recently underwent a major refactor to clean up the code structure, focusing on readability, separation of concerns, and maintainable design patterns.
- **Calculator Logic** ([C#/Calculatrice/calculatrice.cs](https://github.com/epicvixen73-arch/projetsPerso/blob/main/C%23/Calculatrice/calculatrice.cs))
  - **What it does**: A structured implementation of calculation logic, translating mathematical operations into robust, type-safe C# methods.
- **OOP Game Translation** ([C#/Minijeux/Juste_prix.cs](https://github.com/epicvixen73-arch/projetsPerso/blob/main/C%23/Minijeux/Juste_Prix.cs))
  - **What it does**: The object-oriented translation of the classic guessing game, demonstrating how to encapsulate game state and rules within classes for better scalability.

---

## The Learning Journey

Building these projects has been an iterative process of trial, error, and refinement. 

- **The Challenge of State**: In the Python Roulette game, ensuring the balance updated correctly across multiple betting rounds required careful variable scoping and loop control.
- **The Power of Modularity**: Developing the calculator for both PC and NumWorks taught me that separating logic from interface (`main.py` vs `formules.py`) is not just a best practice, but a necessity for cross-platform adaptation.
- **The Value of Refactoring**: The C# application reinforced that writing code is only half the job; restructuring it for clarity and scalability is where true engineering begins.

---

## 🛠️ Tech Stack

| Category | Technologies & Environments |
| :--- | :--- |
| **Languages** | Python, C#, C++ |
| **Environments** | Terminal/Console, NumWorks OS, .NET Framework |
| **Focus Areas** | Algorithmic Logic, State Management, Code Refactoring, Cross-Platform Adaptation, Modular Architecture |
