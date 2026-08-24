from math import*
from random import randint
quitApp = True
firstWrite = True
kmToMl = 0.62137119
mlToKm = 1.609344
def saisir1(message, userChoice=None): # Pour les int
    while True:
        try:
            choix=int(input(message + "\nChoix: "))
            if userChoice is None or choix in userChoice:
                return choix
            else:
                print(f"Invalide. \nnombre nécessaire entre {userChoice}")
        except ValueError:
            print("Merci d'entrer un nombre valide. ")
def saisir2(message, valeurs_valide=None): # Pour les float
    while True:
        try:
            choix=float(input(message))
            if valeurs_valide is None or choix in valeurs_valide:
                return choix
            else:
                print(f"Invalide. \nnombre nécessaire entre {valeurs_valide}")
        except ValueError:
            print("Merci d'entrer un nombre valide. ")
def Actions(action: int, a: float, b: float):
    match action: 
        case 1: # Opérateurs
            print(f"\nAddition : {a} + {b} = {a + b}")
        case 2: 
            print(f"\nSoustraction : {a} - {b} = {a - b}")
        case 3:
            print(f"\nMultiplication : {a} x {b} = {a * b}")
        case 4: 
            print(f"\nDivision : {a} / {b} = {a / b}")
        case 5: 
            print(f"\nReste : {a} % {b} = {a % b}")
        case 6: 
            print(f"\nQuotient : {a} // {b} = {a // b}")
        case 7: # Fonctions
            print(f"\nCarre : {a}**2 = {a ** 2}")
        case 8: 
            print(f"\nCube : {a}**3 = {a ** 3}")
        case 9: 
            print(f"\nInverse : {a: int} / 1 = {a / 1}")
        case 10: 
            print(f"\nRacine : {a: int} = {a ** 0.5}")
        case 11: 
            print(f"\nAbsolue : {a} = {abs(a)}")

def Calculatrice():
    quitCalc = False
    while (quitCalc!=True):
        message = "\n-----[1]: Opérateur---- \n-----[2]: Puissances--- \n-----[3]: Fonctions---- \n-----[4]: Quit--------- \nChoix: "
        choix = saisir1(message, [1,2,3,4])
        if choix not in [1,2,3,4]:
            return
        match choix:
            case 1: #Operateurs
                message = "\n1: Addition \n2: Soustraction \n3: Multiplication \n4: Division \n5: Reste \n6: Quotient \nChoix: "
                choix = saisir1(message, [1,2,3,4,5,6])
                if choix not in [1,2,3,4,5,6]:
                    return
                a: float = saisir2("a: ")
                b: float = saisir2("b: ")
                Actions(choix, a, b)
            case 2: # Puissance
                print("⚠: Nombre eniter uniquement")
                a:int = saisir1("a: ")
                n:int = saisir1("n: ")
                print(f"{a} ^ {n} = {a**n}")
            case 3: # Fonctions
                message: str = "\n1: Carre \n2: Cube \n3: Inverse \n4: Racine \n5: Absolue \nChoix: "
                choix = saisir1(message, [1,2,3,4,5])
                if choix not in [1,2,5]:
                    a = saisir2("a: ")
                    Actions(choix + 6, a)
                    return
                elif choix not in [3,4]: 
                    a = saisir1("a: ")
                    Actions()
                    return
            case 4: 
                quitCalc = True
                return
def JeuPrix():
    hasWon: bool = False
    randomMax: int = 51
    nbGuess: int = 5
    valueToGuess: int = randint(0, randomMax)
    print(f"Nombre à trouvé entre 0 et {randomMax}")
    while (nbGuess > 0 and hasWon != True):
        guess = saisir1("Ton guess: ", )
        if (guess):
            ecart: int = abs(valueToGuess - guess)
            if (ecart <=1):
                hasWon = True
                print("Bravo tu as gagné !!")
            else: 
                chaleur: str = None
                match ecart:
                    case < 2:
                        chaleur = "BRÛLANT !!"
                    case < 5:
                        chaleur = "Chaud"
                    case < 10:
                        chaleur = "Tiède"
                    default:
                        chaleur = "Froid"
                direction: str = "supérieure" if valueToGuess > guess else "inférieure"
                print(f"{chaleur} - La valeur est {direction}")
        else:
            continue
        nbGuess += -1
        print(f"{nbGuess} / 5 essai(s) restant(s)")
        if (hasWon):
            print(f"Fin du jeu, merci d'y avoir joué ! Vous avez gagné ! La valeur était {valueToGuess}")
        else:
            print(f"Fin du jeu, merci d'y avoir joué ! Vous avez perdu. La valeur était {valueToGuesss}")
        continue
def Météo():
    print("1: °C ->°F; 2: °F -> °C")
    choix:int = saisir1("Choix: ")
    if (choix):
        return
    température = saisir2("Température: ")
    if (température):
        return
    result:str = None
    if choix == 1:
        resultF:float = température * 9 / 5 + 32
        print(f"{température} °C = {resultF} °F")
    else: 
        resultC: float = (temppérature - 32) * 5 + 32
        print(f"{température} °F = {resultC} °C")
    return
def VitesseConv():
    print("1: km/h -> mph; 2: mph -> km/h")
    choix:int = saisir1("Choix: ")
    if (choix):
        return
    vitesse: float = saisir2("Vitesse: ")
    if (vitesse):
        return
    if choix == 1:
        resultMPH: float = vitesse * kmToMl
        print(f"{vitesse} km/h = {resultMPH} mph")
    else:
        resultKm:float = vitesse * mlToKM
        print(f"{vitesse} mph = {resultKM} km/h")
    return
while quitApp != True:
    choix:int = saisir1("TEST_APP \n1: Calculatrice \n2: Juste_Prix \n3: Météo \n4: Vitesse \n5: Quit \nChoix: ")
    if (choix):
        return
    match choix:
        case 1: 
            Calculatrice()
            break
        case 2:
            JeuPrix()
            break
        case 3: 
            Météo()
            break
        case 4: 
            VitesseConv()
            break
        case 5:
            print("Au revoir et à bientôt !")
            quitApp = True
            break
