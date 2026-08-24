from math import exp, factorial
from formules import*
from time import sleep
def run():
    choix=input("1: Maths \t2: Physique \nChoix: ")
    # Maths
    if choix == "1": # Maths
        choix = input("\n1: Fonctions \t5: Triangles \n2: Coordonnées \t6: Taux \n3: Théorèmes \t7: Géométrie \n4: Vecteurs \nChoix: ")
        match choix:
            case "1": #Fonctions
                x = int(input("\nx: "))
                print(f"\n{x} ^ 2 = {x ** 2}")
                print(f"{x} ^ 3 = {x ** 3}") 
                if x == 0:
                    pass
                else: 
                    print(f"1 / {x} = {1 / x}")
                    print(f"sqrt({x}) = {sqrt(x)}")
                print(f"|{x}| = {abs(x)}")
                print(f"factorielle de {x} = {factorial(x)}")
                print(f"exponentielle de {x} = {exp(x)}")
            case "2": # Coordonnées
                choix = input("\nm: Milieu \td: Distance \nChoix: ")
                if choix == "m": # milieu
                    milieu()
                    return
                elif choix == "d": # distance
                    distance()
                    return
                else: 
                    print("Veuillez choisir une option valide")
                    return
            case "3": # Théorèmes
                choix = input("\np: Pythagore \tt: Thalès \nChoix: ")
                if choix == "p":
                    pythagore()
                    return
                elif choix == "t":
                    thales()
                    return
                else: 
                    print("Veuillez choisir une option valide")
                    return
            case "4": # Vecteurs
                choix = input("\nc: Relation de Chasles \nd: Déterminant \nChoix: ")
                if choix == "c":
                    chasles()
                    return
                elif choix == "d":
                    determinant()
                    return
                else: 
                    print("Veuillez choisir une option valide")
                    return
            case "5": # Triangle
                choix = input("\ns: Somme angulaire \nt: Trigonométrie \nChoix: ")
                if choix == "s": 
                    sommeAngulaire()
                    return
                elif choix == "t":
                    trigo()
                    return
                else: 
                    print("Veuillez choisir une option valide")
                    return
            case "6": # Taux
                taux()
                return
            case "7":
                choix = input("\n1: Aires \t2: Volumes \nChoix: ")
                if choix == "1":
                    aires()
                    return
                elif choix == "2":
                    volumes()
                    return
                else:
                    print("Veuillez choisir une option valide.")
                    return
            case _: # Default
                print("Veuillez choisir une option valide")
                return
    elif choix == "2": # Physique
        choix = input("1: Matière \t2: Electricité \n3: Optique \t4: Vitesse Moyenne \n5: Forces \nChoix: ")
        match choix:
            case "1": # Matière
                choix = input("v: Masse Volumique \ta: Masse Atome \nm: Mol \td: Dilution \nChoix: ")
                match choix:
                    case "v":
                        masseVolumique()
                        return
                    case "a":
                        masseAtomes()
                        return
                    case "m":
                        mol()
                        return
                    case "d":
                        dilution()
                        return
                    case _: 
                        print("Veuillez choisir une option valide")
            case "2": # Électricité
                choix = input("1: Loi d'Ohm \t2: Puissance Electrique \n3: Energie Electrique \nChoix: ")
                if choix == "1":
                    loiOhm()
                    return
                elif choix == "2":
                    puissanceElec()
                    return
                elif choix == "3":
                    energieElec()
                    return
                else: 
                    print("Veuillez choisir une option valide")
            case "3": # Optique
                choix = input("1: Loi de Snell Descartes \n2: Indice de réfraction \nChoix: ")
                if choix == "1":
                    Snell_Descartes()
                    return
                elif choix == "2":
                    indiceRefraction()
                    return
            case "4": # Vitesse Moyenne
                vitesseMoyenne()
                return
            case "5": # Forces
                choix = input("1: Force de gravitation \n2: Poids \nChoix: ")
                if choix == "1":
                    forceDeGravitation()
                    return
                elif choix == "2":
                    poids()
                    return
                else: 
                    print("Veuillez choisir une option valide")
            case _:
                print("Veuillez choisir une option valide")

while True:
    run()
    continuer = input("\nAvez vous terminé ? \n1(oui) / 0(non): ")
    if continuer=="1":
        print("Deconnexion...")
        sleep(2)
        print("Au revoir")
        break
    print()
