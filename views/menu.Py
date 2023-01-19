
def ask_user():
    response = int(0)
    while response != 1 and response != 2:
        print("  =====================================")
        print("")
        print("||Bienvenue dans le Menu Generale      ||")
        print("||selectionner une option, VOUS ÉTES : ||")
        print("")
        print("  =====================================")
        response = int(input("1 Joueur\n2 Organisateur\n0 Quit >>"))
        match response:
            case 1:
                print("Tu est donc un joueur\n ==========================")
                print("Tu veux faire quoi \n =========================")
                player_section_response = int(input(
                    "-1 Crée un joueur\n-0 Retour au Menu >> "))
                match player_section_response:
                    case 1:
                        print("cree un joueur ")
                    case 0:
                        response = str(0)
            case 2:
                print("Tu est donc un Organisateur\n =========================")
                print("Tu veux faire quoi \n =========================")
                organisation_section_choice = int(input(
                    "1 Crée un tournois\n2- Voir la liste des tournois\n3- Voir la liste des joueurs\n4- Selectionner un tournois existant\n0- Retour au menu precedent >>"))
                match organisation_section_choice:
                    case 1:
                        print("Tu veux : Crée un tournois")
                    case 2:
                        print("Tu veux : Voir la liste des tournois")
                    case 3:
                        print("Tu veux : Voir la liste des Joueurs")
                    case 4:
                        print("Tu veux :Sélectionner un tournois existant")
                    case 0:
                        response = str(0)
            case _:
                break


ask_user()
