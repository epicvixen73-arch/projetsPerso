#include <iostream>
#include <random>
#include <string>
#include <unordered_map>
#include <map>
#include <algorithm>
#include <unordered_set>

using std::unordered_set;

//générateur de l'aléatoire
std::random_device rd;
std::mt19937 gen(rd());
std::uniform_int_distribution<> distr(0, 36);

unordered_set<int> nombresRouge = { 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 };
unordered_set<int> nombresNoir = { 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35 };
int nombreVert = 0;

std::map<int, std::string> COLOR_MAP = {
        {1, "ROUGE"},
        {2, "NOIR"},
        {3, "VERT"}
};

static std::string getColor(int number) {
        if (number == 0) {
            return "VERT";
        }
        if (nombresRouge.contains(number)) {
            return "ROUGE";
        }
        if (nombresNoir.contains(number)) {
            return "NOIR";
        }
        else {
            return "INVALIDE";
        }
}

static void separator() {
        std::cout << "-------------------------" << std::endl;
}

int main()
{
    std::string choix;
    std::string color;
    std::string parity_str;
    char bet_parity;
    bool is_even;
    int bank = 1000;
    int net_profit;
    int bet_color;
    int bet_num;
    int bet;
    int num;
    int gain = 0; 

    separator();
    std::cout << "CASINO ROULETTE" << std::endl;
    separator();

    while (bank > 0) {
        //Début UI Utilisateur
        std::cout << "[SOLDE: " << bank << "$]" << std::endl;
        std::cout << "1 - Numéro (x36)" << std::endl;
        std::cout << "2 - Couleur (x2)" << std::endl;
        std::cout << "3  - Pair / Impair (x2)" << std::endl;
        //Fin UI Utilisateur
        std::cout << "Choix: " << std::endl;
        std::cin >> choix;
        if (choix == "0") {
            std::cout << "Fin de la partie. " << std::endl;
            break;
        }

        if (choix != "1" && choix != "2" && choix != "3") {
            std::cout << "Choix invalide !" << std::endl;
            continue;
        }

        std::cout << "Mise: " << std::endl;
        if (!(std::cin >> bet)) {
            std::cout << "Erreur : vous devez entrer un nombre entier !" << std::endl;
            std::cin.clear();
            std::cin.ignore(1000, '\n');
            continue;
        }
        if (bet <= 0 || bet > bank) {
            std::cout << "Mise invalide (trop élevée ou négative) !" << std::endl;
            continue;
        }

        num = distr(gen);
        color = getColor(num);
        bool won = false;
        gain = 0;

        //filtre pour un parie sur un nombre
        if (choix == "1") {
            std::cout << "Numéro de 0 à 36: " << std::endl;
            if (!(std::cin >> bet_num)) {
                std::cin.clear();
                std::cin.ignore(10000, '\n');
                std::cout << "Erreur : saisie invalide.\n";
                continue;
            }
            if (bet_num == num) {
                gain = bet * 35 + bet;
                bank -= bet;
                won = true;
            }
        }
        //filtre pour un parie sur une couleur
        else if (choix == "2") {
            std::cout << "1 = Rouge \n2 = Noir \n3 = Vert \nCouleur: " << std::endl;

            if (!(std::cin >> bet_color)) {
                std::cin.clear();
                std::cin.ignore(10000, '\n');
                std::cout << "Erreur : saisie invalide.\n";
                continue;
            }
            if (!COLOR_MAP.contains(bet_color)) {
                std::cout << "Couleur Invalide !" << std::endl;
                continue;
            }
            if (COLOR_MAP.at(bet_color) == color) {
                gain = (bet_color == 3) ? bet * 35 + bet : bet * 2;
                bank -= bet;
                won = true;
            }
        }
        //filtre pour un parie sur la parité
        else if (choix == "3") {
            if (num == 0) {
                std::cout << "ZERO - PERDU" << std::endl;
            }
            else {
                std::cout << "Pair (P) / Impair (I): " << std::endl;
                if (!(std::cin >> bet_parity)) {
                    std::cin.clear();
                    std::cin.ignore(10000, '\n');
                    std::cout << "Erreur : saisie invalide.\n";
                    continue;
                }
                if (bet_parity != 'P' && bet_parity != 'I') {
                    std::cout << "Choix invalide !" << std::endl;
                    continue;
                }
                is_even = (num % 2 == 0);
                if ((bet_parity == 'P' && is_even) || (bet_parity == 'I' && !is_even)) {
                    gain = bet * 2;
                    bank -= bet;
                    won = true;
                }
            }
        }
        parity_str = (num == 0) ? "ZERO" : (num % 2 == 0) ? "PAIR" : "IMPAIR";
        std::cout << "\nTirage: " << num << " (" << color << ", " << parity_str << ") " << std::endl;
        if (won) {
            bank += gain; 
            net_profit = gain - bet;
            std::cout << "GAGNE: +" << net_profit << " $ (profit)" << std::endl;
        }
        else {
            std::cout << "Perdu..." << std::endl;
        }
        std::cout << "[SOLDE: " << bank << " $]" << std::endl;
        separator();
        if (bank <= 0) {
            std::cout << "GAME OVER" << std::endl;
            break;
        }
    }
}
