import random


print("Bienvenue dans le jeu du Shifumi")


points_of_bot = 0
points_of_player = 0


while points_of_player < 3 and points_of_bot < 3:

    print("Entrez un élément entre : Pierre / Papier / Ciseaux en respectant les majuscules et les minuscules : ")
    hasard = random.choice(["Pierre", "Papier", "Ciseaux"])
    choice_p = input()
    if choice_p == hasard:
        print("Vous :", choice_p, "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Egalité")
    elif choice_p == "Pierre" and hasard == "Ciseaux":
        print("Vous :", choice_p, "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Bravo, vous gagnez 1 point")
        points_of_player += 1
        print("\n", "Vous :", points_of_player, "points\n", "Bot :", points_of_bot, "points")
    elif choice_p == "Papier" and hasard == "Pierre":
        print("Vous :", choice_p, "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Bravo, vous gagnez 1 point")
        points_of_player += 1
        print("\n", "Vous :", points_of_player, "points\n", "Bot :", points_of_bot, "points")
    elif choice_p == "Ciseaux" and hasard == "Papier":
        print("Vous :", choice_p, "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Bravo, vous gagnez 1 point")
        points_of_player += 1
        print("\n", "Vous :", points_of_player, "points\n", "Bot :", points_of_bot, "points")
    elif choice_p == "Ciseaux" and hasard == "Pierre":
        print("Vous :", choice_p, "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Aïe, le bot gagne 1 point")
        points_of_bot += 1
        print("\n", "Vous :", points_of_player, "points\n", "Bot :", points_of_bot, "points")
    elif choice_p == "Pierre" and hasard == "Papier":
        print("Vous :", choice_p, "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Aïe, le bot gagne 1 point")
        points_of_bot += 1
        print("\n", "Vous :", points_of_player, "points\n", "Bot :", points_of_bot, "points")
    elif choice_p == "Papier" and hasard == "Ciseaux":
        print("Vous :", choice_p, "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Aïe, le bot gagne 1 point")
        points_of_bot += 1
        print("\n", "Vous :", points_of_player, "points\n", "Bot :", points_of_bot, "points")


if points_of_player == 3:
    print("\nFélicitation, vous avez gagné")
else:
    print("\nLe bot a gagné")
