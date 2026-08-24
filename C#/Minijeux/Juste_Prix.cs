using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Random;
namespace Juste_prix
{
    internal class Program
    {

        static void Main(string[] args)
        {
            Random al = new Random();
            int UserGuess;
            int NbGuess = 5;
            string Credit = "Fin du jeu, merci d'y avoir joué ! ";
            int Score = 0; //0 = perdu; 1 = Gagné
            while (NbGuess > 0 && Score ==0)
            {
                if (Saisir("Ton guess: ", out int Guess, al.Next(0, 51)))
                {
                    Score = 1;
                    Console.WriteLine(Credit);
                    continue;
                }
                else if (NbGuess==0 || Score == 1)
                {
                    Console.WriteLine(Credit);
                    break;
                }
                NbGuess -- ;
                Console.WriteLine(NbGuess + " / 5 essai(s) restant(s). ");
            }
        }
        static bool IsInBorne(float UserGuess, float aleatoire)
        {
            if (UserGuess == aleatoire - 1 || UserGuess == aleatoire || UserGuess == aleatoire + 1)
            {
                global::System.Console.WriteLine("Choix valide !");
                return true;
            }
            else
            {
                global::System.Console.WriteLine("Choix invalide !");
                return false;
            }
        }
        static bool Saisir(string message, out int UserGuess, int aleatoire = int.MaxValue)
        {
            Console.Write("\n" + message);
            while (true)
            {
                string saisi = Console.ReadLine();
                if (int.TryParse(saisi, out UserGuess))
                {
                    return IsInBorne(UserGuess, aleatoire);
                }
                else
                {
                    Console.WriteLine("Invalide, reboot... ");
                    return false;
                }
            }
        }
    }
}
