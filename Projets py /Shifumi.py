import random

print("Bienvenue dans le jeu du Shifumi")

points_of_bot = 0
points_of_player = 0


while points_of_player < 3 and points_of_bot < 3:

    print("Entrez un élément entre : Pierre / Papier / Ciseaux : ")
    hasard = random.choice(["pierre", "papier", "ciseaux"])
    choice_p = input()
    if choice_p == hasard:
        print("Vous :", choice_p.lower(), "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Egalité")
    elif choice_p.lower() == "pierre" and hasard == "ciseaux":
        print("Vous :", choice_p.lower(), "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Bravo, vous gagnez 1 point")
        points_of_player += 1
        print("\n" + "Vous : " + str(points_of_player) + " points\n" + "Bot : " + str(points_of_bot) + " points")
    elif choice_p.lower() == "papier" and hasard == "pierre":
        print("Vous :", choice_p.lower(), "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Bravo, vous gagnez 1 point")
        points_of_player += 1
        print("\n" + "Vous : " + str(points_of_player) + " points\n" + "Bot : " + str(points_of_bot) + " points")
    elif choice_p.lower() == "ciseaux" and hasard == "papier":
        print("Vous :", choice_p.lower(), "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Bravo, vous gagnez 1 point")
        points_of_player += 1
        print("\n" + "Vous : " + str(points_of_player) + " points\n" + "Bot : " + str(points_of_bot) + " points")
    elif choice_p.lower() == "ciseaux" and hasard == "pierre":
        print("Vous :", choice_p.lower(), "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Aïe, le bot gagne 1 point")
        points_of_bot += 1
        print("\n" + "Vous : " + str(points_of_player) + " points\n" + "Bot : " + str(points_of_bot) + " points")
    elif choice_p.lower() == "pierre" and hasard == "papier":
        print("Vous :", choice_p.lower(), "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Aïe, le bot gagne 1 point")
        points_of_bot += 1
        print("\n" + "Vous : " + str(points_of_player) + " points\n" + "Bot : " + str(points_of_bot) + " points")
    elif choice_p.lower() == "papier" and hasard == "ciseaux":
        print("Vous :", choice_p.lower(), "\nBot :", hasard, "\n")
        print(choice_p, "VS", hasard, ":")
        print("Aïe, le bot gagne 1 point")
        points_of_bot += 1
        print("\n" + "Vous : " + str(points_of_player) + " points\n" + "Bot : " + str(points_of_bot) + " points")


if points_of_player == 3:
    print("\nFélicitation, vous avez gagné")
else:
    print("\nLe bot a gagné")
