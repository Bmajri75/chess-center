from dataclasses import dataclass


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

    def creat_player(self):
        joueur = []
        print("cree un joueur ")
        id = input("Entre ton ID National>>>")
        first_name = input("Entre ton Nom >>>")
        last_name = input("Entre ton Prénom >>>")
        date_of_birth = input("Entre ta date de naissance >>>")
        joueur.append(id)
        joueur.append(first_name, )
        joueur.append(last_name, )
        joueur.append(date_of_birth)
        return joueur

    def match_response(self):
        """match response from ask user and return the appropriate method """
        match self.ask_user():
            case 1:
                print("reponse 1 ")
                self.creat_player()
            case 2:
                print("reponse 2 ")
            case 3:
                print('reponse 3')
            case 4:
                print('reponse 4')
            case 0:
                print("reponse Q")


menu = Menu()
menu.match_response()
