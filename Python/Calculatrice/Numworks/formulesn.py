from math import sqrt, cos, sin, tan, acos, asin, atan, pi, radians, degrees

def milieu():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    print("coos du milieu: \nx = " + str(mx) + "; y = " + str(my))
    return
def distance():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    distanceResult = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("distance = " + str(distanceResult))
    return
def pythagore():
    choix = input("1: Calculer l'hypotenuse \n2: Verifier un triangle \nChoix: ")
    a = float(input("\na: "))
    b = float(input("b: "))
    if choix == "1":
        c = a ** 2 + b ** 2
        print("Hypo du triangle = " + str(c))
        return
    elif choix == "2":
        c = float(input("c: "))
        if c **2 == a ** 2 + b ** 2:
            print("ABC est rectangle")
            return
        else:
            print("ABC est pas rectangle")
            return
def thales():
    choix = input("AD/AB = AE/AC \n1(AD) 2(AB) 3(AE) 4(AC) \nChercher: ")
    if choix == "1":
        AB = float(input("AB: "))
        AE = float(input("AE: "))
        AC = float(input("AC: "))
        AD = (AB * AE) / AC
        print("AD = " + str(AD))
        return
    elif choix == "2":
        AE = float(input("AE: "))
        AD = float(input("AD: "))
        AC = float(input("AC: "))
        AB = (AD * AC) / AE
        print("AB = " + str(AB))
        return
    elif choix == "3":
        AB = float(input("AB: "))
        AD = float(input("AD: "))
        AC = float(input("AC: "))
        AE = (AD * AC) / AB
        print("AE = " + str(AE))
        return
    elif choix == "4":
        AB = float(input("AB: "))
        AD = float(input("AD: "))
        AE = float(input("AE: "))
        AC = (AB * AE) / AD
        print("AC = " + str(AC))
        return
def chasles():
    choix = input("\n1(AC) 2(AB) 3(BC) \nTrouver: ")
    if choix == "1":
        AB = float(input("AB: "))
        BC = float(input("BC: "))
        AC = AB + BC
        print("AC = " + str(AC))
        return
    elif choix == "2":
        AC = float(input("AC: "))
        BC = float(input("BC: "))
        AB = AC - BC
        print("AB = " + str(AB))
        return
    elif choix == "3":
        AC = float(input("AC: "))
        AB = float(input("AB: "))
        BC = AC - AB
        print("BC = " + str(BC))
        return
def determinant():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    result = x1 * y2 - y1 * x2
    if result == 0:
        print("det = 0 \nVecteurs colineaires")
        return
    else: 
        print("det = " + str(result) + "\nVecteurs non colineraires")
        return
def sommeAngulaire():
    angle1 = float(input("angle1: "))
    angle2 = float(input("angle2: "))
    print("3ieme angle = " + str(180 - (angle1 + angle2)) + "° \n")
    return
def trigo():
    # Partie de trigo normal
    x = float(input("\nTrigo normal (compris dans R) \nx: "))
    print("cos(" + str(x) + ") = " + str(cos(radians(x))))
    print("sin(" + str(x) + ") = " + str(sin(radians(x))))
    print("tan(" + str(x) + ") = " + str(tan(radians(x))))
    # Partie de trigo Arc
    x = float(input("\nArcTrigo (de -1 à 1) 2(skip) \nx: "))
    if x == 2:
        return
    elif -1 < x < 1:
        print("arccos(" + str(x) + ") = " + str(degrees(acos(x))))
        print("arcsin(" + str(x) + ") = " + str(degrees(asin(x))))
        print("arctan(" + str(x) + ") = " + str(degrees(atan(x))))
        return
def taux():
    choix = input("1: taux evo \n2: taux global \nChoix: ")
    if choix == "1":
        a = float(input("Valeur depart: "))
        b = float(input("Valeur arrivee: "))
        if a == 0:
            print("Erreur: \nvaleur depart peut pas etre 0.")
            return
        else:
            taux = (b - a) / a * 100
            print("Taux d'evo: " + str(taux) + " %")
            return
    elif choix == "2":
        a = float(input("Variation 1(%): "))
        b = float(input("Variation 2(%): "))
        var1 = a / 100
        var2 = b / 100
        taux = ((1 + var1) * (1 + var2) - 1) * 100
        print("Taux global: " + str(taux) + " %")
        return
def aireCercle():
    r = float(input("r: "))
    print("Aire cercle de rayon " + str(r) + " = " + str(pi * (r ** 2)) + " cm2")
    return
def aireTriangle():
    base = float(input("base: "))
    hauteur = float(input("hauteur: "))
    print("Aire triangle = " + str((base * hauteur) / 2) + " cm2")
    return
def aireEllipse():
    a = float(input("a: "))
    b = float(input("b: "))
    print("Aire ellipse =  " + str(pi * a * b) + " cm2")
    return
def aireTrapeze():
    grdBase = float(input("Grande base: "))
    pttBase = float(input("Petite base: "))
    hauteur = float(input("Hauteur: "))
    print("Aire trapeze = " + str(((grdBase + pttBase) * hauteur) / 2) + " cm2")
    return
def aireLosange():
    grdDiago = float(input("Grande diagonale: "))
    pttDiago = float(input("Petite diagonale: "))
    print("Aire losange = " + str((grdDiago * pttDiago) / 2) + " cm2")
    return
def aires():
    choix = input("\n1(cercle) 2(triangle) \n3(ellipse) 4(trapeze) \n5(lossange) \nChoix: ")
    if choix == "1":
        aireCercle()
        return
    elif choix == "2":
        aireTriangle()
        return
    elif choix == "3":
        aireEllipse()
        return
    elif choix == "4":
        aireTrapeze()
        return
    elif choix == "5":
        aireLosange()
        return
    else: 
        print("Veuillez saisir une option")
        return
def Vcylindre():
    rayon = float(input("rayon: "))
    hauteur = float(input("hauteur: "))
    print("Volume cylindre = " + str(pi * rayon ** 2 * hauteur) + " cm3")
    return
def Vpyramide():
    base = float(input("base: "))
    hauteur = float(input("hauteur: "))
    print("Volume pyramide = " + str((base * hauteur) / 3) + " cm3")
    return
def Vboule():
    rayon = float(input("rayon: "))
    print("Volume boule = " + str((4 / 3) * pi * rayon ** 3) + " cm3")
    return
def volumes():
    choix = input("1: cylindre 2: pyramide \n3: boule")
    if choix == "1":
        Vcylindre()
        return
    elif choix == "2":
        Vpyramide()
        return
    elif choix == "3":
        Vboule()
        return
def masseVolumique():
    choix = input("1(p) 2(m) 3(V) \nCalculer: ")
    if choix == "1":
        m = float(input("m (kg): "))
        V = float(input("V (m3): "))
        rho = m / V
        print("p = " + str(rho) + " kg/m3")
        return
    elif choix == "2":
        rho = float(input("p (kg/m3): "))
        V = float(input("V (m3): "))
        m = rho * V
        print("m = " + str(m) + " kg")
        return
    elif choix == "3":
        m = float(input("m (kg): "))
        rho = float(input("p (kg/m3): "))
        V = m / rho
        print("V = " + str(V) + " m3")
        return
    else:
        print("Veuillez saisir une option")
        return
def masseAtomes():
    mProton = 1.673e-27
    mNeutron = 1.675e-27
    mElectron = 9.110e-31
    x = int(input("Nb protons: ")) 
    y = int(input("Nb neutrons: "))
    z = int(input("Nb electrons: "))
    m = (x * mProton) + (y * mNeutron) + (z * mElectron)
    print("Masse atome = " + str(m) + " kg")
    return
def mol():
    NA = 6.02e23
    nEntites = float(input("Nombre entitees: "))
    nMoles = nEntites / NA
    print("Nombre mol = " + str(nMoles) + " mol")
    return
def dilution():
    choix = input("\n 1(C2) 2(V2) \nCalculer: ")
    C1 = float(input("C1 (mol/L): "))
    V1 = float(input("V1 (L): "))
    if choix == "1":
        V2 = float(input("V2 (L): "))
        C2 = (C1 * V1) / V2
        print("C2 = " + str(C2) + " mol/L")
        return
    elif choix == "2":
        C2 = float(input("C2 (mol/L): "))
        V2 = (C1 * V1) / C2
        print("V2 = " + str(V2) + " L")
        return
    else:
        print("Veuillez saisir une option")
        return
def loiOhm():
    choix = input("1(U) 2(R) 3(I) \nCalculer: ")
    if choix == "1":
        R = float(input("R (Ω): "))
        I = float(input("I (A): "))
        U = R * I
        print("U = " + str(U) + " V")
        return
    elif choix == "2":
        U = float(input("U (V): "))
        I = float(input("I (A): "))
        R = U / I
        print("R = " + str(R) + " Ω")
        return
    elif choix == "3":
        U = float(input("U (V): "))
        R = float(input("R (Ω): "))
        I = U / R
        print("I = " + str(I) + " A")
        return
def puissanceElec():
    choix = input("1(P = UxI)\n2(P = RxI**2) \n3(P = U**2/R) \nCalculer: ")
    if choix == "1":
        U = float(input("U (V): "))
        I = float(input("I (A): "))
        P = U * I
    elif choix == "2":
        R = float(input("R (Ω): "))
        I = float(input("I (A): "))
        P = R * I ** 2
    elif choix == "3":
        U = float(input("U (V): "))
        R = float(input("R (Ω): "))
        P = U ** 2 / R
    print("\nP = " + str(P) + " W")
    return
def energieElec():
    P = float(input("P (W): "))
    t = float(input("t (s): "))
    E = P * t
    print("E = " + str(E) + " J \nE = " + str(E / 3600) + " Wh")
    return
def Snell_Descartes():
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    i1 = float(input("i1 (°): "))
    sinI2 = n1 * sin(radians(i1)) / n2
    if sinI2 > 1:
        print("Reflexion totale")
        return
    else:
        i2 = degrees(asin(sinI2))
        print("i2 = " + str(i2) + "°")
        return
def indiceRefraction():
    c = 3e8
    choix = input("1(n) 2(v) \nCalculer: ")
    if choix == "1":
        v = float(input("v (m/s): "))
        n = c / v
        print("n = " + str(n))
        return
    elif choix == "2":
        n = float(input("n: "))
        v = c / n
        print("v = " + str(v) + " m/s")
        return
def vitesseMoyenne():
    choix = input("1(v) 2(d) 3(t) \nCalculer: ")
    if choix == "v":
        d = float(input("d (m): "))
        t = float(input("t (s): "))
        v = d / t
        print("v = " + str(v) + " m/s")
        return
    elif choix == "d":
        v = float(input("v (m/s): "))
        t = float(input("t (s): "))
        d = v * t
        print("d = " + str(d) + " m")
        return
    elif choix == "t":
        d = float(input("d (m): "))
        v = float(input("v (m/s): "))
        t = d / v
        print("t = " + str(t) + " s")
        return
def forceDeGravitation():
    G = 6.674e-11
    m1 = float(input("m1 (kg): "))
    m2 = float(input("m2 (kg): "))
    d = float(input("d (m): "))
    F = G * m1 * m2 / d ** 2
    print("F = " + str(F) + " N")
    return
def poids():
    g = 9.81
    m = float(input("m (kg): "))
    P = m * g
    print("P = " + str(P) + " N")
    return
