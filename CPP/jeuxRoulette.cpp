#include <iostream>
#include <random>
#include <string>
#include <unordered_set>
#include <limits>

using std::unordered_set;

//générateur de l'aléatoire
std::mt19937 gen(std::random_device {}());
static std::uniform_int_distribution<int> distr(0, 36);

static std::string getColor(int number) {
    if (number == 0) return "VERT";
    static const std::unordered_set<int> nombresRouge = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36};
    return nombresRouge.contains(number) ? "ROUGE" : "NOIR";
}
static void separator() {
        std::cout << "-------------------------\n";
}
static bool readInt(int& out, const std::string& prompt) {
    std::cout << prompt;
    if (!(std::cin >> out)) {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return false;
    }
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    return true;
}
int main()
{
    int bank = 1000;
    separator();
    std::cout << "CASINO ROULETTE\n";
    separator();
    while (bank > 0) {
        std::cout << "[SOLDE: " << bank << "$]\n";
        std::cout << "1 - Numéro (x36)\n";
        std::cout << "2 - Couleur (x2)\n";
        std::cout << "3  - Pair / Impair (x2)\n";
        std::string choix;
        std::cout << "Choix: ";
        std::cin >> choix;
        if (choix == "0") {
            std::cout << "Fin de la partie. Solde final: " << bank << " $\n";
            break;
        }
        if (choix != "1" && choix != "2" && choix != "3") {
            std::cout << "Choix invalide ! \n";
            continue;
        }
        int bet = 0;
        std::cout << "Mise: " << std::endl;
        if (!readInt(bet, "Mise: ") || bet <= 0 || bet > bank) {
            std::cout << "Erreur : vous devez entrer un nombre entier !\n";
            continue;
        }
        bank -= bet;
        int num = distr(gen);
        std::string color = getColor(num);
        bool won = false;
        int gain = 0;
        //filtre pour un parie sur un nombre
        if (choix == "1") {
            int bet_num = -1;
            if (!readInt(bet_num, "Numéro de 0 à 36: ") || bet_num < 0 || bet_num > 36) {
                std::cout << "Erreur : saisie invalide. Mise perdue.\n";
            }
            else if (bet_num == num) {
                gain = bet * 36;
                won = true;
            }
        }
        //filtre pour un parie sur une couleur
        else if (choix == "2") {
            int bet_color = 0;
            if (!readInt(bet_color, "1 = Rouge, 2 = Noir, 3 = Vert\nCouleur: ") || bet_color < 1 || bet_color > 3) {
                std::cout << "Erreur : saisie invalide. Mise perdue.\n";
            }
            else {
                std::string targetColor = (bet_color == 1) ? "ROUGE" : (bet_color == 2) ? "NOIR" : "VERT";
                if (color == targetColor) {
                    gain = (bet_color == 3) ? bet * 36 : bet * 2;
                    won = true;
                }
            }
        }
        //filtre pour un parie sur la parité
        else if (choix == "3") {
            char bet_parity = ' ';

            std::cout << "Pair (P) / Impair (I): ";
            std::cin >> bet_parity;
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

            bet_parity = std::toupper(bet_parity);

            if (bet_parity != 'P' && bet_parity != 'I') {
                std::cout << "Erreur : saisie invalide. Mise perdue.\n";
            }
            else if (num == 0) {
                std::cout << "ZERO : Les paris de parité sont perdants.\n";
            }
            else {
                bool is_even = (num % 2 == 0);
                bool bet_is_even = (bet_parity == 'P');
                if (is_even == bet_is_even) {
                    gain = bet * 2;
                    won = true;
                }
            }
        }
        std::string parity_str = (num == 0) ? "ZERO" : (num % 2 == 0) ? "PAIR" : "IMPAIR";
        std::cout << "\nTirage: " << num << " (" << color << ", " << parity_str << ") \n";
        if (won) {
            bank += gain;
            std::cout << "GAGNE: +" << (gain - bet) << " $ (profit)\n";
        }
        else {
            std::cout << "Perdu...\n";
        }
        std::cout << "[SOLDE: " << bank << " $]";
        separator();
    }
    if (bank <= 0) {
        std::cout << "GAME OVER\n";
    }
    return 0;
}
