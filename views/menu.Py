
def ask_user():
    reponse = int
    print("  =====================================")
    print("")
    print("||Bienvenue dans le Menu Generale      ||")
    print("||selectionner une option, VOUS ÉTES : ||")
    print("")
    print("  =====================================")

    while reponse != 1 and reponse != 2:
        reponse = int(input("1 Joueur\n2 Organisateur >>"))
        if reponse == 1:
            print(f"Tu est donc un joueur\n ==========================")
            print("Tu veux faire quoi \n ========================= ")
            player_section_choice = int(input(
                "1 Crée un joueur\n 0 Retour au Menu >> "))
            if player_section_choice == 1:
                print("cree un joueur ")
            elif player_section_choice == 0:
                print("retour au menu principal")
                reponse = int(player_section_choice)
                print(reponse)
        elif reponse == 2:
            print(f"Tu est donc un Organisateur\n =========================")
            print("Tu veux faire quoi \n =========================")
            player_section_choice = int(input(
                "1 Crée un tournois\n2- Voir la liste des tournois\n3- Voir la liste des joueurs\n4- Selectionner un tournois existant\n0- Retour au menu precedent >>"))
            if player_section_choice == 1:
                print("Tu veux : Crée un tournois")
            elif player_section_choice == 2:
                print("Tu veux : Voir la liste des tournois")
            elif player_section_choice == 3:
                print("Tu veux : Voir la liste des Joueurs")
            elif player_section_choice == 4:
                print("Tu veux :Sélectionner un tournois existant")
            elif player_section_choice == 0:
                print("Tu veux : Retour au menu principal")
                reponse = int(player_section_choice)


ask_user()
