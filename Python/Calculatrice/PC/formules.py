from math import sqrt, cos, sin, tan, acos, asin, atan, pi, degrees, radians

def milieu():
    """
    Demande quatre variables pour les coordonnées de deux points.
    Puis affiche les coordonnées du points qui est le milieu des deux premiers.
    Puis la fonction se termine proprement avec 'return'.
    """
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    print(f"coordonnées du milieu: x = {mx}; y = {my}")
    return

def distance():
    """
    Demande quatre variables pour les coordonnées de deux points.
    Puis affiche la distance entre ces deux points avec la forule dans la variable 'distance_result'.
    Puis la fonction se termiine proprement avec 'return'.
    """
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    distance_result = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"distance = {distance_result}")
    return

def pythagore():
    """
    Propose deux options au user:
        c pour calculer l'hypoténuse
        v pour vérifier un triangle
    
    Selon l'option choisie, plusieurs variables sont demandées pour sois calculer ou vérifier un calcul.
    Puis, on affiche la valeur de l'hyponétuse si il veut le calculer; 
    si second choix, on affiche si le triangle est rectangle ou non.
    """
    choix = input("c: Calculer l'hypoténuse \nv: Vérifier un triangle \nChoix: ")
    print()
    a = float(input("a: "))
    b = float(input("b: "))
    if choix == "c":
        c = a ** 2 + b ** 2
        print(f"L'hypothénuse du triangle vaut {c}")
        return
    elif choix == "v":
        c = float(input("c: "))
        if c ** 2 == a ** 2 + b ** 2:
            print("Le triangle a b c est rectangle")
            return
        else:
            print("Le triangle a b c n'est pas rectangle")
            return

def thales():
    """
    AE pour chercher AE
    AC pour chercher AC
    AD pour chercher AD
    AB pour chercher AB
    """
    choix = input("AD/AB = AE/AC\nAE: Chercher AE \tAC: Chercher AC\nAD: Chercher AD \tAB: Chercher AB \nChoix: ")
    match choix:
        case "AE":
            AB = float(input("AB: "))
            AD = float(input("AD: "))
            AC = float(input("AC: "))
            AE = (AD * AC) / AB
            print(f"AE = {AE}")
            return
        case "AC":
            AB = float(input("AB: "))
            AD = float(input("AD: "))
            AE = float(input("AE: "))
            AC = (AB * AE) / AD
            print(f"AC = {AC}")
            return
        case "AD":
            AB = float(input("AB: "))
            AE = float(input("AE: "))
            AC = float(input("AC: "))
            AD = (AB * AE) / AC
            print(f"AD = {AD}")
            return
        case "AB":
            AE = float(input("AE: "))
            AD = float(input("AD: "))
            AC = float(input("AC: "))
            AB = (AD * AC) / AE
            print(f"AB = {AB}")
            return

def chasles():
    """
    1 pour calculer AC
    2 pour calculer AB
    3 pour calculer BC
    """
    print("")
    choix = input("\n1: Calculer AC \t2: Calculer AB \t3: Calculer BC \nChoix: ")
    match choix:
        case "1":
            AB = float(input("AB: "))
            BC = float(input("BC: "))
            AC = AB + BC
            print(f"AC = {AC}")
            return
        case "2":
            AC = float(input("AC: "))
            BC = float(input("BC: "))
            AB = AC - BC
            print(f"AB = {AB}")
            return
        case "3":
            AC = float(input("AC: "))
            AB = float(input("AB: "))
            BC = AC - AB
            print(f"BC = {BC}")
            return

def determinant():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    result = x1 * y2 - y1 * x2
    if result == 0:
        print(f"déterminant = {result} \nLes deux vecteurs sont colinéaires")
        return
    else: 
        print(f"déterminant = {result} \nLes deux vecteurs ne sont pas colinéaires")
        return

def sommeAngulaire():
    angle1 = float(input("angle1: "))
    angle2 = float(input("angle2: "))
    print(f"troisième angle = {180 - (angle1 + angle2)}° \n")
    return

def trigo():
    # Partie de trigo normal
    x = float(input("Pour trigo normal (compris dans R) \nx: "))
    print(f"cos({x}) = {cos(radians(x))}")      #cosinus
    print(f"sin({x}) = {sin(radians(x))}")      #sinus
    print(f"tan({x}) = {tan(radians(x))}")      #tangente
    # Partie de trigo Arc
    x = float(input("Pour ArcTrigo (de -1 à 1) \nx: "))
    print(f"arcos({x}) = {degrees(acos(x))}")   #arccosinus
    print(f"arcsin({x}) = {degrees(asin(x))}")  #arcsinus
    print(f"arctan({x}) = {degrees(atan(x))}")  #arctangente
    return

def taux():
    choix = input("e: \ttaux d'évolution \ng: \ttaux global \nChoix: ")
    if choix == "e":
        a = float(input("Valeur de départ: "))
        b = float(input("Valeur d'arrivée: "))
        if a == 0:
            print("Erreur: valeur de départ ne peut pas être 0.")
            return
        else:
            taux = (b - a) / a * 100
            print(f"Taux d'évolution: {taux:.2f} %")
            return
    elif choix == "g":
        a = float(input("Variation 1(%): "))
        b = float(input("Variation 2(%): "))
        var1 = a / 100
        var2 = b / 100
        taux = ((1 + var1) * (1 + var2) - 1) * 100
        print(f"Taux global: {taux:.2f} %")
        return

def aireCercle():
    r = float(input("r: "))
    print(f"Le cercle de rayon {r} a une aire de {pi * (r ** 2)} cm²")
    return

def aireTriangle():
    base = float(input("base: "))
    hauteur = float(input("hauteur: "))
    print(f"Le triangle a une aire de {(base * hauteur) / 2} cm²")
    return

def aireEllipse():
    a = float(input("a: "))
    b = float(input("b: "))
    print(f"L'Ellipse a une aire de {pi * a * b} cm²")
    return

def aireTrapeze():
    grdBase = float(input("Grande base: "))
    pttBase = float(input("Petite base: "))
    hauteur = float(input("Hauteur: "))
    print(f"Le trapèze vaut {((grdBase + pttBase) * hauteur) / 2} cm²")
    return

def aireLosange():
    grdDiago = float(input("Grande diagonale: "))
    pttDiago = float(input("Petite diagonale: "))
    print(f"Le losange vaut {(grdDiago * pttDiago) / 2} cm²")
    return

def aires():
    """
    aires de 
        1- cercle (fonction à part)
        2- triangle (fonction à part)
        3- ellipse (fonction à part)
        4- trapèse (fonction à part)
        5- losange (fonction à part)
    """
    choix = input("1: cercle \t2: triangle \n3: ellipse \t4: trapèze \n5: lossange \nChoix: ")
    match choix: 
        case "1":
            aireCercle()
            return
        case "2":
            aireTriangle()
            return
        case "3":
            aireEllipse()
            return
        case "4":
            aireTrapeze()
            return
        case "5":
            aireLosange()
            return
    return

def Vcylindre():
    rayon = float(input("rayon: "))
    hauteur = float(input("hauteur: "))
    print(f"Volume du cylindre vaut {pi * rayon ** 2 * hauteur} cm³")
    return

def Vpyramide():
    base = float(input("base (cm2) : "))
    hauteur = float(input("hauteur: "))
    print(f"Le volume de la pyramide vaut {(base * hauteur) / 3} cm³")
    return

def Vboule():
    rayon = float(input("rayon: "))
    print(f"Le volume de la boule vaut {(4 / 3) * pi * rayon ** 3} cm³")
    return

def volumes():
    """
    1- cylindre
    2- pyramide
    3- boule
    """
    choix = input("1: cylindre \t2: pyramide \n3: boule")
    match choix:
        case "1":
            Vcylindre()
            return
        case "2":
            Vpyramide()
            return
        case "3":
            Vboule()
            return

def masseVolumique():
    """
    p pour calculer p
    m pour calculer m
    v pour calculer V
    """
    choix = input("p: Calculer p\nm: Calculer m\nv: Calculer V \nChoix: ")
    match choix:
        case "p":
            m = float(input("m (kg): "))
            V = float(input("V (m³): "))
            rho = m / V
            print(f"p = {rho} kg/m³")
            return
        case "m":
            rho = float(input("p (kg/m³): "))
            V = float(input("V (m³): "))
            m = rho * V
            print(f"m = {m} kg")
            return
        case "v":
            m = float(input("m (kg): "))
            rho = float(input("p (kg/m³): "))
            V = m / rho
            print(f"V = {V} m³")
            return
        case _:
            print("Veuillez saisir une option")
            return

def masseAtomes():
    mProton = 1.673e-27
    mNeutron = 1.675e-27
    mElectron = 9.110e-31
    x = int(input("Nb de protons: ")) 
    y = int(input("Nb de neutrons: "))
    z = int(input("Nb d'électrons: "))
    m = (x * mProton) + (y * mNeutron) + (z * mElectron)
    print(f"Masse de l'atome: {m:.3e} kg")
    return

def mol():
    NA = 6.02e23
    n_entites = float(input("Nombre d'entitées: "))
    n_moles = n_entites / NA
    print(f"Nombre de moles: {n_moles:.4e} mol")
    return

def dilution():
    """
    c pour calculer C2
    v pour calculer V2
    """
    choix = input("c: Calculer C2\nv: Calculer V2 \nChoix: ")
    C1 = float(input("C1 (mol/L): "))
    V1 = float(input("V1 (L): "))
    match choix:
        case "c":
            V2 = float(input("V2 (L): "))
            C2 = (C1*V1)/V2
            print(f"C2 = {C2} mol/L")
            return
        case "v":
            C2 = float(input("C2 (mol/L): "))
            V2 = (C1*V1)/C2
            print(f"V2 = {V2} L")
            return
        case _:
            print("Veuillez saisir une option")
            return

def loiOhm():
    choix = input("Calculer: \nu: U \nr=R \ni=I \nChoix: ")
    match choix:    
        case "u":
            R = float(input("R (Ω): "))
            I = float(input("I (A): "))
            U = R * I
            print(f"U = {U} V")
            return
        case "r":
            U = float(input("U (V): "))
            I = float(input("I (A): "))
            R = U / I
            print(f"R = {R} Ω")
            return
        case "i":
            U = float(input("U (V): "))
            R = float(input("R (Ω): "))
            I = U / R
            print(f"I = {I} A")
            return

def puissanceElec():
    choix = input("1: P = UxI\n2: P = RxI²\n3: P = U²/R \nChoix: ")
    match choix:
        case 1:
            U = float(input("U (V): "))
            I = float(input("I (A): "))
            P = U * I
        case 2:
            R = float(input("R (Ω): "))
            I = float(input("I (A): "))
            P = R * I ** 2
        case 3:
            U = float(input("U (V): "))
            R = float(input("R (Ω): "))
            P = U ** 2 / R
    print(f"P = {P} W")
    return

def energieElec():
    P = float(input("P (W): "))
    t = float(input("t (s): "))
    E = P * t
    print(f"E = {E} J  |  E = {E / 3600:.2f} Wh")
    return

def Snell_Descartes():
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    i1 = float(input("i1 (°): "))
    sin_i2 = n1 * sin(radians(i1)) / n2
    if sin_i2 > 1:
        print("Réflexion totale")
        return
    else:
        i2 = degrees(asin(sin_i2))
        print(f"i2 = {i2}°")
        return

def indiceRefraction():
    c = 3e8
    choix = input("Calculer: \n\tn: \tn  \n\tv: \tv \nChoix: ")
    if choix == "n":
        v = float(input("v (m/s): "))
        n = c / v
        print(f"n = {n}")
        return
    elif choix == "v":
        n = float(input("n: "))
        v = c / n
        print(f"v = {v:.2e} m/s")
        return

def vitesseMoyenne():
    choix = input("Calculer: \n\tv: \tv  \n\td: \td  \n\tt: \tt \nChoix: ")
    if choix == "v":
        d = float(input("d (m): "))
        t = float(input("t (s): "))
        v = d / t
        print(f"v = {v} m/s")
        return
    elif choix == "d":
        v = float(input("v (m/s): "))
        t = float(input("t (s): "))
        d = v * t
        print(f"d = {d} m")
        return
    elif choix == "t":
        d = float(input("d (m): "))
        v = float(input("v (m/s): "))
        t = d / v
        print(f"t = {t} s")
        return

def forceDeGravitation():
    G = 6.674e-11
    m1 = float(input("m1 (kg): "))
    m2 = float(input("m2 (kg): "))
    d = float(input("d (m): "))
    F = G * m1 * m2 / d ** 2
    print(f"F = {F:.2e} N")
    return

def poids():
    g = 9.81
    m = float(input("m (kg): "))
    P = m * g
    print(f"P = {P} N")
    return
