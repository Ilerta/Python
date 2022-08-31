bank = 2000
wallet = 100
running = True
bag = []

print("Bienvenue sur notre borne")
print("Entrez 'home' si vous souhaitez retourner à l'accueil quand vous n'y êtes pas\n")

# accueil
def home():
    print("Tappez le chiffre correspondant à l'action de votre choix : ")
    choice = int(input("1 : Recevoir un pret\n2 : Retirer de l'argent\n3 : Acceder à la boutique\n4 : Voir le contenu de mon sac\n5 : Voir mon argent\n6 : Se déconnecter\n\nChoix : "))
    if choice == 1:
        give_money()
    elif choice == 2:
        retirer()
    elif choice == 3:
        shop()
    elif choice == 4:
        bag_elements()
    elif choice == 5:
        money()
    elif choice == 6:
        disconnect()
    else:
        print("\nERREUR : Entrez un nombre valide\n")
        home()

# choix 1
def give_money():
    global bank
    nbr_money = input("Combien voulez-vous emprunter ? (Entre 1 et 5000) : ")
    if nbr_money == "home":
        print("Retour a l'accueil")
        home()
    elif int(nbr_money) <= 5000:
        bank += int(nbr_money)
        print("\nVirement de", str(nbr_money), "€ effectué")
        print("vous avez maintenant " + str(bank) + " € dans votre banque\n")
        home()
    elif int(nbr_money) > 5000:
        print("ERREUR : Cette somme est trop élevée")
        give_money()
    else:
        print("ERREUR : Choisissez une somme entre 1 et 5000")
        give_money()

# choix 2
def retirer():
    global bank, wallet, running
    while running:
        print("Vous avez " + str(bank) + " € dans votre banque et\n" + str(wallet) + " € dans votre porte-monnaie")
        value = input("\nCombien voulez-vous retirer ? : ")
        if value == "home":
            home()
        elif int(value) <= bank:
            bank -= int(value)
            wallet += int(value)
            print("Vous avez bien retirer " + value + " €\nRetour à l'accueil\n")
            home()
        else:
            print("ERREUR : Vous n'avez pas assez d'argent, entrez une somme inférieure\n")
            retirer()

#choix 3
def shop():
    global wallet
    print("\nBienvenue dans notre boutique\n")
    print("Voici les articles disponibles : \n\n"
          "|NOURRITURE|\n> 1 : Panier de fruits | 20€\n> 2 : Panier de légumes | 25€\n> 3 : Viande | 15€\n> 4 : Plateau de fromages | 22€\n> 5 : Lait | 8€\n> 6 : Bouteille d'eau | 3.50€\n\n"
          "|ELECTRO-MENAGER|\n> 7 : Frigo | 220€\n> 8 : Four micro-onde | 125€\n> 9 : Aspirateur | 30€""\n> 10 : Fer à repasser (avec planche) | 32€\n> 11 : Sèche cheveux | 18€\n\n"
          "|APPAREIL INTELLIGENTS|\n> 12 : Smartphone | 565€\n> 13 : Ordinateur de bureau | 2435€\n> 14 : Ordinateur portable | 1300€\n> 15 : Tablette | 255€\n> 16 : Enceinte | 80€\n> 17 : Ecouteurs sans fils | 60€\n\nVous avez", wallet, "€ dans votre porte-monnaie\n")
    while running:
        choice_article = input("Choisissez un article à acheter avec son numéro ou 'home': pour retourner au menu : ")
        if choice_article == "home":
            print("Retour à l'accueil")
            home()
        elif choice_article == str(1):
            if wallet >= 20:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Panier de fruits) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 20
                    bag.append("Panier de fruit")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(2):
            if wallet >= 25:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Panier de légumes) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 25
                    bag.append("Panier de légumes")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(3):
            if wallet >= 15:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Viande) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 15
                    bag.append("Viande")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(4):
            if wallet >= 22:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Plateau de fromages) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 22
                    bag.append("Plateau de fromages")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(5):
            if wallet >= 8:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Lait) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 8
                    bag.append("Lait")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(6):
            if wallet >= 3.50:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Bouteille d'eau) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 3.50
                    bag.append("Bouteille d'eau")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(7):
            if wallet >= 220:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Frigo) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 220
                    bag.append("Frigo")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(8):
            if wallet >= 125:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Four micro-onde) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 125
                    bag.append("Four micro-onde")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(9):
            if wallet >= 30:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Aspirateur) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 30
                    bag.append("Aspirateur")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(10):
            if wallet >= 32:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Fer à repasser (avec planche)) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 32
                    bag.append("Fer à repasser (avec planche)")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(11):
            if wallet >= 18:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Sèche cheveux) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 18
                    bag.append("Sèche cheveux")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(12):
            if wallet >= 565:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Smartphone) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 565
                    bag.append("Smartphone")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(13):
            if wallet >= 2435:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Ordinateur de bureau) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 2435
                    bag.append("Ordinateur de bureau")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(14):
            if wallet >= 1300:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Ordinateur portable) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 1300
                    bag.append("Ordinateur portable")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(15):
            if wallet >= 255:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Tablette) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 255
                    bag.append("Tablette")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(16):
            if wallet >= 80:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Enceinte) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 80
                    bag.append("Enceinte")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        elif choice_article == str(17):
            if wallet >= 20:
                comfirmation = input("Etes vous-sur de votre achat  (oui / non)? (Ecouteurs sans fils) : ")
                if comfirmation == "home":
                    home()
                elif comfirmation == "oui" or "Oui":
                    print("D'accord, merci de votre commande")
                    wallet -= 60
                    bag.append("Ecouteurs sans fils")
                    shop()
                elif comfirmation == "non" or "Non":
                    print("D'accord, achat annulé\n")
                else:
                    print("ERREUR : Vous devez entrer 'oui', 'Oui', 'non', 'Non'")
            else:
                print("Vous n'avez pas d'argent, achat impossible")
        else:
            print("ERREUR : Vous devez entrez un nombre qui correspond à un article")
            shop()

# choix 4
def bag_elements():
    global bag
    if len(bag) != 0:
        print("_________________________________________")
        print("\nVoici le contenu de votre sac : \n")
        for word in bag:
            print(">", word)
        print("_________________________________________\n")
        home()
    else:
        print("_________________________________________\n")
        print("Votre sac est vide")
        print("_________________________________________\n")
        home()

# choix 5
def money():
    print("_________________________________________\n")
    print("Vous avez", bank, "€ dans votre banque\nVous avez", wallet, "€ dans votre porte-monnaie")
    print("_________________________________________\n")
    home()

# choix 6
def disconnect():
    confirmation2 = input("\nVous allez vous déconnecter, en êtes vous sûr ? (oui / non) : ")
    if confirmation2.lower() == "oui":
        print("D'accord, merci d'avoir utiliser nos services")
        quit()
    elif confirmation2.lower() == "non":
        print("Ok, annulation\n")
        home()
    else:
        print("ERREUR : Vous devez entrer 'oui' ou 'non'")
        disconnect()


home()

# test GitHub