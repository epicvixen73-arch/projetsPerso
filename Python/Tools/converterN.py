def main():
    while True:
        print("\n=== CONVERTISSEUR ===")
        print("1. Decimal -> Bin/Hex")
        print("2. Binaire -> Dec/Hex")
        print("3. Hexadecimal -> Dec/Bin")
        print("0. Quitter")
        
        try:
            choice = input("Choix: ")
            
            if choice == "0":
                print("Fin.")
                break
                
            val = input("Valeur: ").strip().upper()
            
            if choice == "1":
                n = int(val, 10)
            elif choice == "2":
                n = int(val, 2)
            elif choice == "3":
                n = int(val, 16)
            else:
                print("Choix invalide.")
                continue
                
            b = bin(n)[2:]
            h = hex(n)[2:].upper()
            d = str(n)
            
            print("\n--- Resultat ---")
            print("BIN: " + b)
            print("DEC: " + d)
            print("HEX: " + h)
            print("----------------")
            
        except ValueError:
            print("Erreur: Valeur invalide pour la base choisie.")
        except KeyboardInterrupt:
            print("\nFin.")
            break

main()
