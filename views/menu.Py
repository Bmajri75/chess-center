
class Menu:
    def __init__(self):
        pass

    def ask_Player(self):
        print("Tu est donc un joueur\n ==========================")
        print("Tu veux faire quoi \n =========================")
        player_section_response = int(input(
            "-1 Crée un joueur\n-0 Retour au Menu >> "))
        match player_section_response:
            case 1:
                joueur = []
                print("cree un joueur ")
                id = input("Entre ton ID National>>>")
                first_name = input("Entre ton Nom >>>")
                last_name = input("Entre ton Prénom >>>")
                date_of_birth = input("Entre ta date de naissance >>>")
                joueur.append(id)
                joueur.append(first_name)
                joueur.append(last_name)
                joueur.append(date_of_birth)
                return joueur

            case 0:
                return 0

    def ask_Admin(self):
        print("Tu est donc un Organisateur\n =========================")
        print("Tu veux faire quoi \n =========================")
        organisation_section_choice = int(input(
            "1 Crée un tournois\n2- Voir la liste des tournois\n3- Voir la liste des joueurs\n4- Selectionner un tournois existant\n0- Retour au menu precedent >>"))
        match organisation_section_choice:
            case 1:
                tournament = []
                print("Tu veux : Crée un tournois")
                tournament_name = input("Entre le nom du tournois >>>")
                place = input("Entre le lieu >>>")
                start_date = input("Date de debut >>>")
                end_date = input("Date de fin >>>")
                curent_laps = input("Tours en cours >>>")
                laps_liste = input("Liste de tours >>>")
                list_players = input("Liste de joueurs >>>")
                description = input("Description >>>")
                total_laps = input("Total de tours >>>")
                tournament.append(tournament_name)
                tournament.append(place)
                tournament.append(start_date)
                tournament.append(end_date)
                tournament.append(curent_laps)
                tournament.append(laps_liste)
                tournament.append(list_players)
                tournament.append(description)
                tournament.append(total_laps)
                print(tournament)
                return tournament
            case 2:
                print("Tu veux : Voir la liste des tournois")
                return 1
            case 3:
                print("Tu veux : Voir la liste des Joueurs")
                return 1
            case 4:
                print("Tu veux :Sélectionner un tournois existant")
                return 1
            case 0:
                return 0

    def menu(self):
        response = int(0)
        while response != 1 and response != 2:
            print("  =====================================")
            print("")
            print("||Bienvenue dans le Menu Generale      ||")
            print("||selectionner une option, VOUS ÉTES : ||")
            print("")
            print("  =====================================")
            response = int(input("1 Joueur\n2 Organisateur\n0 Quit >>"))
            if response == 1:
                self.ask_Player()

            elif response == 2:
                self.ask_Admin()

            elif response == 0:
                break


menu_1 = Menu()

menu_1.menu()
