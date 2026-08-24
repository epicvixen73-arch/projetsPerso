using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Math = System.Math;
namespace Calculatrice
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
                return a / 1;
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
            List<Operation> operations = new List<Operation>();
            operations.Add(new Addition());
            operations.Add(new Soustraction());
            operations.Add(new Multiplication());
            operations.Add(new Division());
            operations.Add(new Reste());


            List<Fonctions> fonctions = new List<Fonctions>();
            fonctions.Add(new Carre());
            fonctions.Add(new Cube());
            fonctions.Add(new Inverse());
            fonctions.Add(new Racine());
            fonctions.Add(new Absolue());


            while (true)
            {
                global::System.Console.WriteLine("#######################");
                global::System.Console.WriteLine();
                string message = "-----[1]: Opérateur---- " +
                    "\n-----[2]: Puissances--- " +
                    "\n-----[3]: Fonctions---- " +
                    "\n-----[4]: Quit--------- " +
                    "\nChoix: ";
                if (!Saisir(message, out int choix, 4)) 
                    continue;
                switch (choix)
                {
                    case 1:
                        message = "-------Opérateur-------";
                        for (int i = 0; i < operations.Count; i++)
                        {
                            Operation op = operations[i];
                            message += "\n[" + (i+1) + "] " + op.GetName();
                        }
                        message += "\nChoix: ";
                        if (!Saisir(message, out int choix_operateur, operations.Count)) 
                            continue;
                        Console.WriteLine("-----------------------");
                        Console.Write("a: ");
                        float a_ope = Convert.ToSingle(Console.ReadLine());
                        Console.Write("b: ");
                        float b = Convert.ToSingle(Console.ReadLine());
                        Console.WriteLine();
                        Console.WriteLine("Result: " + operations[choix_operateur-1].Calcul(a_ope,b ));
                        break;
                    case 2:
                        Console.WriteLine("-------Puissances------");
                        if (!Saisir("a: ", out int a)) 
                            continue;
                        if (!Saisir("n: ", out int n)) 
                            continue;
                        Console.WriteLine();
                        Console.WriteLine("Result de " + a +"^"+ n + " : " + (float)Math.Pow(a, n));
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
                        Console.WriteLine("Result: " + fonctions[choix_fonctions - 1].Fonction(x));
                        break;
                    case 4:
                        Console.WriteLine("Au revoir !");
                        return;

                }
            }
        }
        //fonction pour verif typo

        static bool IsInBorne(float choix, float borne)
        {
            if (choix< 1 || choix> borne) global::System.Console.WriteLine("Choix invalide !") 
                return false;
            else 
                return true;
        }

        //Saisir en int
        static bool Saisir(string message, out int choix, int borne = int.MaxValue)
        {
            Console.Write("\n" + message);
            while (true)
            {
                string saisi = Console.ReadLine();
                if (int.TryParse(saisi, out choix)) 
                    return IsInBorne(choix, borne);
                else Console.WriteLine("Invalide, reboot... ") 
                        return false;
            }
        }


        //Saisir en float
        static bool Saisir(string message, out float choix, float borne = float.MaxValue)
        {
            Console.Write("\n" + message);
            while (true)
            {
                string saisi = Console.ReadLine();
                if (float.TryParse(saisi, out choix)) 
                    return IsInBorne(choix, borne);
                else Console.WriteLine("Invalide, reboot... ") 
                    return false;
            }
        }
        //fonction pour reset ligne pour du dynamique*

    }
}
