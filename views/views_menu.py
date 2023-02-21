from dataclasses import dataclass
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


@dataclass
class Menu:
    def ask_user(self):
        """ask the user and return his response in menu_response"""
        menu_response = int
        value_menu = [0, 1, 2, 3, 4]
        while menu_response not in value_menu:
            print("""
                    ||Bienvenue dans le Menu Generale
                    ||selectionner une option, Que souhaitez vous faire""")

            menu_response = int(input("""
                      1 . Crée un joueur
                      2 . Crée un tournoi
                      3 . Voir un tournoi
                      4 . Voir les rapports
                      0 . Quit
                      """))
        return menu_response

    def views_player(self):
        print("cree un joueur ")
        id = input("Entre ton ID National>>>")
        first_name = input("Entre ton Nom >>>")
        last_name = input("Entre ton Prénom >>>")
        date_of_birth = input("Entre ta date de naissance >>>")
        PlayerController.create_player(
            id, first_name, last_name, date_of_birth)

    def views_tournament(self):
        print("cree un Tourmois")
        name = input("Entre le nom du tournois >>> ")
        location = input("Où à Lieu le tournois >>> ")
        start_date = input("date de début >>> ")
        end_date = input("date de fin Prévu >>> ")
        number_of_laps = input("nombre de tours. (Par defaut 4 ) >>> ")
        current_lap = 0
        rounds = []
        players = []
        description = input("Entrez votre description >>> ")
        TournamentController.creat_tournament(name,
                                              location,
                                              start_date,
                                              end_date,
                                              number_of_laps,
                                              current_lap,
                                              rounds,
                                              players,
                                              description
                                              )

    def match_response(self):
        """match response from ask user and return the appropriate method """
        match self.ask_user():
            case 1:
                print("reponse 1 ")
                self.views_player()
            case 2:
                print("reponse 2 ")
                self.views_tournament()
            case 3:
                print('reponse 3')
            case 4:
                print('reponse 4')
            case 0:
                print("reponse Q")
