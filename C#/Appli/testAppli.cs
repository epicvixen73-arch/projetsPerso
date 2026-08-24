using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Math = System.Math;
using System.Globalization;
namespace Test_App
{
    internal class Program
    {
        abstract class Operation
        {
            public abstract float Calcul(float a, float b);
            public abstract string GetName();
        }
        class Addition : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a + b;
            }

            public override string GetName()
            {
                return "Addition";
            }
        }
        class Soustraction : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a - b;
            }

            public override string GetName()
            {
                return "Soustraction";
            }
        }
        class Multiplication : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a * b;
            }

            public override string GetName()
            {
                return "Multiplication";
            }
        }
        class Division : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a / b;
            }

            public override string GetName()
            {
                return "Division";
            }
        }
        class Reste : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a % b;
            }

            public override string GetName()
            {
                return "Reste";
            }
        }
        abstract class Fonctions
        {
            public abstract float Fonction(float a);
            public abstract string GetName();
        }
        class Carre : Fonctions
        {
            public override float Fonction(float a)
            {
                return (float)Math.Pow(a, 2);
            }

            public override string GetName()
            {
                return "Carre";
            }
        }
        class Cube : Fonctions
        {
            public override float Fonction(float a)
            {
                return (float)Math.Pow(a, 3);
            }

            public override string GetName()
            {
                return "Cube";
            }
        }
        class Inverse : Fonctions
        {
            public override float Fonction(float a)
            {
                return 1 / a;
            }

            public override string GetName()
            {
                return "Inverse";
            }
        }
        class Racine : Fonctions
        {
            public override float Fonction(float a)
            {
                if (a < 0)
                    return float.NaN;
                return (float)Math.Sqrt(a);
            }
            public override string GetName()
            {
                return "Racine Carrée";
            }
        }
        class Absolue : Fonctions
        {
            public override float Fonction(float a)
            {
                return (float)Math.Abs(a);
            }

            public override string GetName()
            {
                return "Valeur Absolue";
            }
        }
        static void Main(string[] args)
        {
            string message = "\nAppuyez sur une touche pour revenir au menu principal...";
            string asciiApp = @"
  /$$$$$$                      /$$ /$$                       /$$     /$$                    
 /$$__  $$                    | $$|__/                      | $$    |__/                    
| $$  \ $$  /$$$$$$   /$$$$$$ | $$ /$$  /$$$$$$$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$__  $$ /$$__  $$| $$| $$ /$$_____/ |____  $$|_  $$_/  | $$ /$$__  $$| $$__  $$
| $$__  $$| $$  \ $$| $$  \ $$| $$| $$| $$        /$$$$$$$  | $$    | $$| $$  \ $$| $$  \ $$
| $$  | $$| $$  | $$| $$  | $$| $$| $$| $$       /$$__  $$  | $$ /$$| $$| $$  | $$| $$  | $$
| $$  | $$| $$$$$$$/| $$$$$$$/| $$| $$|  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
|__/  |__/| $$____/ | $$____/ |__/|__/ \_______/ \_______/   \___/  |__/ \______/ |__/  |__/
          | $$      | $$                                                                    
          | $$      | $$                                                                    
          |__/      |__/                                                                    ";
            string asciiCalc = @"
  /$$$$$$            /$$                     /$$             /$$               /$$                              
 /$$__  $$          | $$                    | $$            | $$              |__/                              
| $$  \__/  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$  /$$$$$$    /$$$$$$  /$$  /$$$$$$$  /$$$$$$$  /$$$$$$ 
| $$       |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$|_  $$_/   /$$__  $$| $$ /$$_____/ /$$_____/ /$$__  $$
| $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$  | $$    | $$  \__/| $$| $$      | $$      | $$$$$$$$
| $$    $$ /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$  | $$ /$$| $$      | $$| $$      | $$      | $$_____/
|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$  |  $$$$/| $$      | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$
 \______/  \_______/|__/ \_______/ \______/ |__/ \_______/   \___/  |__/      |__/ \_______/ \_______/ \_______/
                                                                                                                
                                                                                                                
                                                                                                                ";
            string asciiJeu = @"
    /$$$$$                       /$$                       /$$$$$$$           /$$          
   |__  $$                      | $$                      | $$__  $$         |__/          
      | $$ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$         | $$  \ $$ /$$$$$$  /$$ /$$   /$$
      | $$| $$  | $$ /$$_____/|_  $$_/   /$$__  $$ /$$$$$$| $$$$$$$//$$__  $$| $$|  $$ /$$/
 /$$  | $$| $$  | $$|  $$$$$$   | $$    | $$$$$$$$|______/| $$____/| $$  \__/| $$ \  $$$$/ 
| $$  | $$| $$  | $$ \____  $$  | $$ /$$| $$_____/        | $$     | $$      | $$  >$$  $$ 
|  $$$$$$/|  $$$$$$/ /$$$$$$$/  |  $$$$/|  $$$$$$$        | $$     | $$      | $$ /$$/\  $$
 \______/  \______/ |_______/    \___/   \_______/        |__/     |__/      |__/|__/  \__/
                                                                                           
";
            string asciiMeteo = @"
 /$$      /$$             /$$                        
| $$$    /$$$            | $$                        
| $$$$  /$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$  $$$| $$| $$$$$$$$  | $$    | $$$$$$$$| $$  \ $$
| $$\  $ | $$| $$_____/  | $$ /$$| $$_____/| $$  | $$
| $$ \/  | $$|  $$$$$$$  |  $$$$/|  $$$$$$$|  $$$$$$/
|__/     |__/ \_______/   \___/   \_______/ \______/ 
                                                     
";
            string asciiExit = @"
 /$$$$$$$$           /$$   /$$    
| $$_____/          |__/  | $$    
| $$       /$$   /$$ /$$ /$$$$$$  
| $$$$$   |  $$ /$$/| $$|_  $$_/  
| $$__/    \  $$$$/ | $$  | $$    
| $$        >$$  $$ | $$  | $$ /$$
| $$$$$$$$ /$$/\  $$| $$  |  $$$$/
|________/|__/  \__/|__/   \___/  
                                  
";
            string asciiHist = @"
$$\   $$\ $$\             $$\                         $$\                               
$$ |  $$ |\__|            $$ |                        \__|                              
$$ |  $$ |$$\  $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$\  $$$$$$\  $$\   $$\  $$$$$$\  
$$$$$$$$ |$$ |$$  _____|\_$$  _|  $$  __$$\ $$  __$$\ $$ |$$  __$$\ $$ |  $$ |$$  __$$\ 
$$  __$$ |$$ |\$$$$$$\    $$ |    $$ /  $$ |$$ |  \__|$$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |
$$ |  $$ |$$ | \____$$\   $$ |$$\ $$ |  $$ |$$ |      $$ |$$ |  $$ |$$ |  $$ |$$   ____|
$$ |  $$ |$$ |$$$$$$$  |  \$$$$  |\$$$$$$  |$$ |      $$ |\$$$$$$$ |\$$$$$$  |\$$$$$$$\ 
\__|  \__|\__|\_______/    \____/  \______/ \__|      \__| \____$$ | \______/  \_______|
                                                                $$ |                    
                                                                $$ |                    
                                                                \__|                    
";
            while (true)
            {
                Console.Clear();
                PrintBanner(asciiApp, ConsoleColor.Red);
                if (!Saisir("===  Test_App  === \n1: Calculatrice \n2: Juste Prix \n3: Convertisseur °C/°F\n4: Quitter \nChoix: " , out int ActionChoice, 4))
                    continue;
                switch (ActionChoice)
                {
                    case 1:
                        //Calculatrice
                        PrintBanner(asciiCalc, ConsoleColor.Cyan);
                        bool quitCalc = false;
                        List<Operation> operations = new List<Operation>
                        {
                            new Addition(),
                            new Soustraction(),
                            new Multiplication(),
                            new Division(),
                            new Reste()
                        };


                        List<Fonctions> fonctions = new List<Fonctions>
                        {
                            new Carre(),
                            new Cube(),
                            new Inverse(),
                            new Racine(),
                            new Absolue()
                        };


                        while (!quitCalc)
                        {
                            global::System.Console.WriteLine("#######################");
                            global::System.Console.WriteLine();
                            message = "-----[1]: Opérateur---- \n-----[2]: Puissances--- \n-----[3]: Fonctions---- \n-----[4]: Quit--------- \nChoix: ";
                            if (!Saisir(message, out int choix, 4))
                                continue;
                            switch (choix)
                            {
                                case 1:
                                    message = "-------Opérateur-------";
                                    for (int i = 0; i < operations.Count; i++)
                                    {
                                        Operation op = operations[i];
                                        message += "\n[" + (i + 1) + "] " + op.GetName();
                                    }
                                    message += "\nChoix: ";
                                    if (!Saisir(message, out int choix_operateur, operations.Count))
                                        continue;
                                    Console.WriteLine("-----------------------");
                                    if (!SaisirAnyFloat("a: ", out float a_ope))
                                        continue;
                                    if (!SaisirAnyFloat("b: ", out float b))
                                        continue;
                                    Console.WriteLine();
                                    float resultatOp = operations[choix_operateur - 1].Calcul(a_ope, b);
                                    Console.WriteLine("Result: " + resultatOp);
                                    historique.Add($"Calculatrice [{operations[choix_operateur - 1].GetName()}] : {a_ope} , {b} = {resultatOp}");
                                    break;
                                case 2:
                                    Console.WriteLine("-------Puissances------");
                                    if (!Saisir("a: ", out int a))
                                        continue;
                                    if (!Saisir("n: ", out int n))
                                        continue;
                                    Console.WriteLine();
                                    float resultatPow = (float)Math.Pow(a, n);
                                    Console.WriteLine($"Result de {a}^{n}: {resultatPow}");
                                    historique.Add($"Puissance : {a}^{n} = {resultatPow}");
                                    break;
                                case 3:
                                    message = "-------Fonctions-------";
                                    for (int i = 0; i < fonctions.Count; i++)
                                    {
                                        Fonctions op = fonctions[i];
                                        message += "\n[" + (i + 1) + "] " + op.GetName();
                                    }
                                    message += "\nChoix: ";
                                    if (!Saisir(message, out int choix_fonctions, fonctions.Count))
                                        continue;
                                    Console.WriteLine("-----------------------");
                                    if (!Saisir("x: ", out float x))
                                        continue;
                                    Console.WriteLine(); 
                                    float resultatFn = fonctions[choix_fonctions - 1].Fonction(x);
                                    Console.WriteLine("Result: " + resultatFn);
                                    historique.Add($"Fonction [{fonctions[choix_fonctions - 1].GetName()}] de {x} = {resultatFn}");
                                    break;
                                case 4:
                                    Console.WriteLine("Au revoir !");
                                    quitCalc = true;
                                    break;
                            }
                        }
                        PauseDuUser("\nAppuyez sur une touche pour revenir au menu principal...");
                        break;
                    case 2:
                        //Juste Prix
                        PrintBanner(asciiJeu, ConsoleColor.Magenta);
                        Random random = new Random();
                        int nbGuess = 5;
                        int randomMax = 51;
                        bool hasWon = false;

                        int valueToGuess = random.Next(0, randomMax);
                        Console.WriteLine($"Nombre à trouver entre 0 et {randomMax - 1}");
                        while (nbGuess > 0 && !hasWon)
                        {
                            if (Saisir("Ton guess: ", out int guess, randomMax))
                            {
                                int ecart = Math.Abs(valueToGuess - guess);
                                if (ecart <= 1)
                                {
                                    hasWon = true;
                                    Console.ForegroundColor = ConsoleColor.Green;
                                    Console.WriteLine("Tu as gagné !");
                                    Console.ResetColor();
                                }
                                else
                                {
                                    string chaleur = ecart < 2 ? "BRÛLANT !" : ecart < 5 ? "Chaud" : ecart < 10 ? "Tiède" : "Froid";
                                    ConsoleColor couleur = ecart < 2 ? ConsoleColor.Red : ecart < 5 ? ConsoleColor.Yellow : ecart < 10 ? ConsoleColor.DarkYellow : ConsoleColor.Blue;
                                    string direction = valueToGuess > guess ? "supérieure" : "inférieure";
                                    Console.ForegroundColor = couleur;
                                    Console.WriteLine($"{chaleur} - La valeur est {direction}");
                                    Console.ResetColor();
                                }
                            }
                            else
                            {
                                continue;
                            }

                            nbGuess--;
                            Console.WriteLine(nbGuess + " / 5 essai(s) restant(s). ");
                        }

                        if (hasWon)
                        {
                            Console.ForegroundColor = ConsoleColor.Green;
                            Console.WriteLine("Fin du jeu, merci d'y avoir joué ! Vous avez gagné ! La valeur était : " + valueToGuess);
                            Console.ResetColor();
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("Fin du jeu, merci d'y avoir joué ! Vous avez perdu. La valeur était : " + valueToGuess);
                            Console.ResetColor();
                        }
                        historique.Add(hasWon ? $"Juste Prix : gagné en {5 - nbGuess} essai(s) (valeur = {valueToGuess})" : $"Juste Prix : perdu (valeur = {valueToGuess})");
                        PauseDuUser("\nAppuyez sur une touche pour revenir au menu principal...");
                        break;
                    case 3:
                        // Convertisseur °C <-> °F
                        PrintBanner(asciiMeteo, ConsoleColor.Green);
                        Console.WriteLine("1: °C -> °F");
                        Console.WriteLine("2: °F -> °C");
                        if (!Saisir("Choix: ", out int convChoice, 2))
                            break;

                        if (!SaisirAnyFloat("Température: ", out float tempVal))
                            break;

                        if (convChoice == 1)
                        {
                            float resultF = tempVal * 9f / 5f + 32f;
                            Console.WriteLine($"{tempVal} °C = {resultF} °F");
                            historique.Add($"Conversion : {tempVal}°C = {resultF}°F");
                        }
                        else
                        {
                            float resultC = (tempVal - 32f) * 5f / 9f;
                            Console.WriteLine($"{tempVal} °F = {resultC} °C");
                            historique.Add($"Conversion : {tempVal}°F = {resultC}°C");
                        }
                        PauseDuUser("\nAppuyez sur une touche pour revenir au menu principal...");
                        break;
                    case 4:
                        //Quit

                        //Rajouter le print de l'historique entier après ce commentaire mais au dessus du clear.
                        Console.Clear();
                        PrintBanner(asciiHist, ConsoleColor.Yellow);
                        ShowHist();
                        Console.Clear();
                        PrintBanner(asciiExit, ConsoleColor.DarkGray);
                        return;
                }
            }
        }
        static bool Saisir(string message, out int userChoice, int borne = int.MaxValue)
        {
            Console.Write("\n" + message);

            string saisi = Console.ReadLine();
            if (int.TryParse(saisi, out userChoice))
            {
                return IsInBorne(userChoice, borne);
            }
            else
            {
                Console.WriteLine("Invalide, reboot... ");
                return false;
            }
        }
        static bool Saisir(string message, out float userChoice, float borne = float.MaxValue)
        {
            Console.Write("\n" + message);
            string saisi = Console.ReadLine();
            if (float.TryParse(saisi, out userChoice))
            {
                return IsInBorne(userChoice, borne);
            }
            else
            {
                Console.WriteLine("Invalide, reboot... ");
                return false;
            }
        }
        static bool SaisirAnyFloat(string message, out float userChoice)
        {
            Console.Write("\n" + message);
            string saisi = Console.ReadLine()?.Trim().Replace(',', '.');
            if (float.TryParse(saisi, NumberStyles.Float, CultureInfo.InvariantCulture, out userChoice))
            {
                return true;
            }
            Console.WriteLine("Invalide, reboot...");
            userChoice = 0f;
            return false;
        }
        static bool IsInBorne(float choix, float borne)
        {
            if (choix < 1 || choix > borne) 
            {
                Console.WriteLine("Choix invalide !");
                return false;
            }
            return true;
        }
        static void PrintBanner(string banner, ConsoleColor color = ConsoleColor.Cyan)
        {
            Console.Clear();
            Console.ForegroundColor = color;
            Console.WriteLine(banner);
            Console.ResetColor();
        }
        static void PauseDuUser(string message)
        {
            Console.WriteLine(message);
            Console.ReadKey(true);
        }
        static readonly List<string> historique = new List<string>();
        static void ShowHist()
        {
            if (historique.Count == 0)
            {
                Console.WriteLine("Aucune action enregistrée.");
            }
            else
            {
                for (int i = 0; i < historique.Count; i++)
                    Console.WriteLine($"{i + 1}. {historique[i]}");
            }
            PauseDuUser("\nAppuyez sur une touche pour fermer...");
        }
    }
}
