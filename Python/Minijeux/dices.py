from random import choice
from time import sleep
def dés():
    faces = [1, 2, 3, 4, 5, 6]
    result = choice(faces)
    print("Roulage des dés...")
    sleep(1.5)
    if result == 1:
        print("() \t() \t()\n() \tX \t()\n() \t() \t()")
    elif result == 2:
        print("() \t() \tX\n() \t() \t()\nX \t() \t()")
    elif result == 3:
        print("() \t() \tX\n() \tX \t()\nX \t() \t()")
    elif result == 4:
        print("X \t() \tX\n() \t() \t()\nX \t() \tX")
    elif result == 5:
        print("X \t() \tX\n() \tX \t()\nX \t() \tX")
    elif result == 6:
        print("X \tX \tX\nX \tX \tX\nX \tX \tX")
def run():
    dés()
    dés()
while True:
    run()
    Quit = input("Avez vous terminé ? 1(oui) / 0(non) : ")
    if Quit == "1":
        break
    print()
