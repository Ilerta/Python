from math import *

running =True

def convert2():
    new_number = int(number) * int(number)
    print("Le carré de", number, "est égal à", new_number)

def convert3():
    new_number = int(number) * int(number) * int(number)
    print("Le cube de", number, "est égal à", new_number)

def convert_rc(): 
    new_number = sqrt(int(number))
    print("La racine carrée de", number, "est égale à", new_number)


while running:
    number = input("Quel nombre voulez-vous convertir ? : ")

    try:
        choice = input("Voulez-vous connaitre le carré de ce nombre : 1\nLe cube de ce nombre : 2\nLa racine carré de ce nombre : 3\nArreter le programme : 'stop'\n\nChoix : ")
        if choice == "stop":
            print("D'accord, merci de votre utilisation")
            running = False
        elif choice == "1":
            convert2()
        elif choice == "2":
            convert3()
        elif choice == "3":
            convert_rc()
        else:
            print("ERREUR : Valeure incorrecte")
    except ValueError:
        print("ERREUR : Entrez un nombre entier supérieur à 0")


