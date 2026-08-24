from math import exp, factorial
from formulesn import *
from time import sleep
def run():
    choix = input("1: Maths \t2: Physique \nChoix: ")
    if choix == "1":
        choix = input("\n1(Fonctions) 2(Coordos) \n3(Theoremes) 4(Vecteurs) \n5(Triangles) 6(Taux) \n7(Geometrie) \nChoix: ")
        if choix == "1":
            x = int(input("x: "))
            print("\n" + str(x) + "**2 = " + str(x ** 2))
            print(str(x) + "**3 = " + str(x ** 3))
            if x == 0:
                print("Division par 0")
                pass
            else:
                print("1 / " + str(x) + " = " + str(1 / x))
                print("sqrt(" + str(x) + ") = " + str(sqrt(x)))
            print("| " + str(x) + " | = " + str(abs(x)))
            print("facto de " + str(x) + " = " + str(factorial(x)))
            print("expo de " + str(x) + " = " + str(exp(x)))
        elif choix == "2":
            choix = input("\n1(Milieu) 2(Distance) \nChoix: ")
            if choix == "1":
                milieu()
                return
            elif choix == "2":
                distance()
                return
            else:
                print("Veuillez choisir une option valide")
                return
        elif choix == "3":
            choix = input("\n1(Pythagore) 2(Thales) \nChoix: ")
            if choix == "1":
                pythagore()
                return
            elif choix == "2":
                thales()
                return
            else:
                print("Veuillez choisir une option valide")
                return
        elif choix == "4":
            choix = input("\n1(Relation de Chasles) \n2(Determinant) \nChoix: ")
            if choix == "1":
                chasles()
                return
            elif choix == "2":
                determinant()
                return
            else:
                print("Veuillez choisir une option valide")
                return
        elif choix == "5":
            choix = input("\n1(Somme angulaire) \n2(Trigonometrie) \nChoix: ")
            if choix == "1":
                sommeAngulaire()
                return
            elif choix == "2":
                trigo()
                return
            else:
                print("Veuillez choisir une option valide")
                return
        elif choix == "6":
            taux()
            return
        elif choix == "7":
            choix = input("\n1: Aires 2: Volumes \nChoix: ")
            if choix == "1":
                aires()
                return
            elif choix == "2":
                volumes()
                return
            else:
                print("Veuillez choisir une option valide")
                return
        else:
            print("Veuillez choisir une option valide")
            return
    elif choix == "2":
        choix = input("1(Matiere) 2(Elec) \n3(Optique) 4(Vit Moyenne) \n5(Forces) \nChoix: ")
        if choix == "1":
            choix = input("1(mVolumique) 2(mAtome) \n3(Mol) 4(Dilution) \nChoix: ")
            if choix == "1":
                masseVolumique()
                return
            elif choix == "2":
                masseAtomes()
                return
            elif choix == "3":
                mol()
                return
            elif choix == "4":
                dilution()
                return
            else:
                print("Veuillez choisir une option valide")
                return
        elif choix == "2":
            choix = input("1(Loi d'Ohm) \n2(Puissance Electrique) \n3(Energie Electrique) \nChoix: ")
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
        elif choix == "3":
            choix = input("1(Snell Descartes) \n2(Indice refrac) \nChoix: ")
            if choix == "1":
                Snell_Descartes()
                return
            elif choix == "2":
                indiceRefraction()
                return
        elif choix == "4":
            vitesseMoyenne()
            return
        elif choix == "5":
            choix = input("1(Force de grav) 2(Poids) \nChoix: ")
            if choix == "1":
                forceDeGravitation()
                return
            elif choix == "2":
                poids()
                return
            else: 
                print("Option valide svp")
        else: 
            print("Ooption valide svp")
while True:
    run()
    continuer = input("\nAvez vous termine ? \n1(oui) / 0(non): ")
    if continuer == "1":
        print("Deconnexion...")
        sleep(2)
        print("Au revoir")
        break
