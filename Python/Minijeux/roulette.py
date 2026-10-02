import random

RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
GREEN_NUMBERS = {0}

COLOR_MAP = {
    "R": "ROUGE",
    "N": "NOIR",
    "V": "VERT"
}

def get_color(number):
    if number in GREEN_NUMBERS:
        return "VERT"
    if number in RED_NUMBERS:
        return "ROUGE"
    if number in BLACK_NUMBERS:
        return "NOIR"
    return "INCONNU"

def separator():
    print("-" * 25)

def main():
    bank = 100
    separator()
    print("CASINO ROULETTE")
    separator()

    while bank > 0:
        print("\n[SOLDE: {} $]".format(bank))
        print("1 - Numero (x36)")
        print("2 - Couleur (x2)")
        print("3 - Pair/Impair (x2)")
        print("0 - Quitter")
        separator()

        try:
            choice = input("Choix: ").strip()
            if choice == "0":
                print("Fin de partie.")
                break
            if choice not in ("1", "2", "3"):
                print("Choix invalide !")
                continue

            bet = int(input("Mise: ").strip())
            if bet <= 0 or bet > bank:
                print("Mise invalide !")
                continue

            num = random.randint(0, 36)
            color = get_color(num)
            gain = 0
            won = False

            if choice == "1":
                bet_num = int(input("Num (0-36): ").strip())
                if not (0 <= bet_num <= 36):
                    print("Num invalide !")
                    continue
                if bet_num == num:
                    gain = bet * 36
                    won = True

            elif choice == "2":
                print("R=Rouge, N=Noir, V=Vert")
                bet_color = input("Couleur: ").strip().upper()
                if bet_color not in COLOR_MAP:
                    print("Couleur invalide !")
                    continue
                if COLOR_MAP[bet_color] == color:
                    gain = bet * 2
                    won = True

            elif choice == "3":
                if num == 0:
                    print("ZERO - PERDU")
                else:
                    bet_parity = input("Pair(P)/Impair(I): ").strip().upper()
                    if bet_parity not in ("P", "I"):
                        print("Choix invalide !")
                        continue
                    
                    is_even = (num % 2 == 0)
                    if (bet_parity == "P" and is_even) or (bet_parity == "I" and not is_even):
                        gain = bet * 2
                        won = True

            parity_str = "PAIR" if num % 2 == 0 else "IMPAIR" if num != 0 else "ZERO"
            print("\nTIRAGE: {} ({}, {})".format(num, color, parity_str))
            
            bank -= bet
            if won:
                bank += gain
                net_profit = gain - bet
                print("GAGNE: +{} $ (profit)".format(net_profit))
            else:
                print("PERDU")

            print("[SOLDE: {} $]".format(bank))
            separator()

        except ValueError:
            print("Erreur: Nombre invalide")
            separator()
        except KeyboardInterrupt:
            print("\nArret.")
            break

    if bank <= 0:
        print("GAME OVER !")

main()
