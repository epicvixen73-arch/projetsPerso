from random import choice
from time import sleep
def decision(a, b, list:list):
    if a == b: 
        print("\nMatch nul; personne ne gagne. ")
    elif a == list[0] and b == list[1] or a == list[1] and b == list[2] or a == list[2] and b == list[0]: 
        print("\nDommage le bot a gagné !")
    elif a == list[1] and b == list[0] or a == list[2] and b == list[1] or a == list[0] and b == list[2]: 
        print("\nBravo vous avez gagné !")
def run():
    choix = ["Rock", "Paper", "Scissors"]
    userChoice = int(input("1: Rock \t2: Paper \t3: Scissors \nChoix: "))
    if userChoice == 1: userChoice = choix[0]
    elif userChoice == 2: userChoice = choix[1]
    elif userChoice == 3: userChoice = choix[2]
    botChoice = choice(choix)
    print("Le bot choisis...")
    sleep(1.5)
    print("Le bot a choisi " + botChoice)
    decision(userChoice, botChoice, choix)
while True:
    run()
    Quit = input("\nAvez vous terminé ? \n1(oui) / 0(non) : ")
    if Quit == "1":
        print("Merci d'avoir joué; à la prochaine fois \nDéconnexion...")
        sleep(1)
        break
    print()
