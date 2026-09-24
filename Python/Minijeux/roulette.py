from random import randint

RED = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)

def get_color(n):
    if n == 0:
        return "VERT"
    return "ROUGE" if n in RED else "NOIR"

def separator():
    print("-" * 30)

def main():
    bank = 100
    separator()
    print("CASINO ROULETTE")
    separator()
    
    while bank > 0:
        print("[SOLDE: " + str(bank) + "$]")
        print("1 - Numero (x36)")
        print("2 - Couleur (x2)")
        print("3 - Pair/Impair (x2)")
        separator()
        
        try:
            choice = int(input("Votre choix: "))
            
            if choice not in [1, 2, 3]:
                print("Choix invalide!")
                continue
            
            bet = int(input("Votre mise: "))
            
            if bet <= 0 or bet > bank:
                print("Mise invalide!")
                continue
            
            # Tirage
            num = randint(0, 36)
            color = get_color(num)
            gain = 0
            
            if choice == 1:
                bet_num = int(input("Votre numero (0-36): "))
                if bet_num == num:
                    gain = bet * 36
                    print("GAGNE: " + str(gain) + "$")
                else:
                    print("PERDU")
                print("\n>>> TIRAGE: " + str(num) + " (" + color + ")")
                    
            elif choice == 2:
                print("R = ROUGE, N = NOIR, V = VERT")
                bet_color = input("Votre couleur: ").upper()
                if bet_color == color:
                    gain = bet * 2
                    print("GAGNE: " + str(gain) + "$")
                else:
                    print("PERDU")
                    
            elif choice == 3:
                if num == 0:
                    print("ZERO - PERDU")
                else:
                    parity = "PAIR" if num % 2 == 0 else "IMPAIR"
                    bet_parity = input("Pair (P) / Impair (I): ").upper()
                    if (bet_parity == "P" and num % 2 == 0) or (bet_parity == "I" and num % 2 == 1):
                        gain = bet * 2
                        print("GAGNE: " + str(gain) + "$")
                    else:
                        print("PERDU")
            
            bank = bank - bet + gain
            print("[NOUVEAU SOLDE: " + str(bank) + "$]")
            separator()
            
            if bank == 0:
                print("GAME OVER - Plus d'argent!")
                
        except ValueError:
            print("Erreur: Entrez un nombre valide")
            separator()
        except KeyboardInterrupt:
            print("\nPartie terminee")
            break

main()
