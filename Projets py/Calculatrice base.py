running = True

while running:

    print("Bienvenue dans ma calculatrice")
    a = input("Choisie le premier nombre ou 'stop' pour arreter le programme : ")

    if a == "stop":
        print("Arret du programme !")
        break

    choice = input("Veux-tu l'additionner : +, le soustraire : -, le multiplier : * ou le diviser : / ? Ou 'stop' pour arreter le programme : ")

    if choice == "stop":
        print("Arret du programme !")
        break

    b = input("Choisie le second nombre ou 'stop' pour arreter le programme : ")

    if b == "stop":
        print("Arret du programme !")
        break

    plus = int(a) + int(b)
    moins = int(a) - int(b)
    multiplier = int(a) * int(b)
    diviser = int(a) / int(b)


    if choice == "+":
        print(str(a) + " + " + str(b) + " = " + str(plus))
    elif choice == "-":
        print(str(a) + " - " + str(b) + " = " + str(moins))
    elif choice == "*":
        print(str(a) + " x " + str(b) + " = " + str(multiplier))
    elif choice == "/":
        print(str(a) + " / " + str(b) + " = " + str(diviser))
    else:
        print("Une erreur est survenue, veillez réessayer")
