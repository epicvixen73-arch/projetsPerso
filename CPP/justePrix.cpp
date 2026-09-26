#include <iostream>
#include <random>
#include <limits>
#include <cmath>

namespace JustePrix {
    struct GameConfig {
        int min_number{1};
        int max_number{100};
        int max_attempts{10};
    };

    int generateTarget(int min, int max) {
        static std::random_device rd;
        static std::mt19937 gen(rd());
        std::uniform_int_distribution<> distrib(min, max);
        return distrib(gen);
    }

    void play() {
        GameConfig config;
        int target = generateTarget(config.min_number, config.max_number);
        int attempts_left = config.max_attempts;
        bool has_won = false;

        std::cout << R"(
    ___           _        ______     _   
   |_  |         | |       | ___ \   (_)  
     | |_   _ ___| |_ ___  | |_/ / __ ___  __ 
     | | | | / __| __/ _ \ |  __/ '__| \ \/ / 
 /\__/ / |_| \__ \ ||  __/ | |  | |  | |>  <
 \____/ \__,_|___/\__\___| \_|  |_|  |_/_/\_\
)" << '\n';
        
        std::cout << "Vous avez " << attempts_left << " essais pour trouver le nombre.\n";

        while (attempts_left > 0 && !has_won) {
            std::cout << "\nVotre proposition : ";
            int user_guess;
            
            if (!(std::cin >> user_guess)) {
                std::cout << "Entrée invalide. Veuillez saisir un entier.\n";
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                continue;
            }

            if (user_guess == target) {
                std::cout << "Bravo, vous avez trouvé le juste prix !\n";
                has_won = true;
            } else {
                attempts_left--;
                int diff = std::abs(user_guess - target);
                
                if (diff <= 1) {
                    std::cout << "Tu y es presque !\n";
                } else if (diff <= 5) {
                    std::cout << "Tu es proche.\n";
                } else if (user_guess < target) {
                    std::cout << "C'est plus grand.\n";
                } else {
                    std::cout << "C'est plus petit.\n";
                }
                
                if (attempts_left > 0) {
                    std::cout << "Il te reste " << attempts_left << " essai(s).\n";
                }
            }
        }

        if (!has_won) {
            std::cout << "\nPerdu ! Le nombre était : " << target << "\n";
        }
        std::cout << "Fin du jeu. Merci d'avoir joué !\n";
    }
}

int main() {
    JustePrix::play();
    return 0;
}
