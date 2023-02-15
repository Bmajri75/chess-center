import json
from dataclasses import dataclass
from models.player_model import Player


@dataclass
class PlayerController:
    """ Create a new player, if player is not in the data """
    @staticmethod
    def validator(player):
        """methode qui valide les format des donnee entrer de la views"""
        pass

    @staticmethod
    def create_player(id, first_name, last_name, date_of_birth):
        player = Player(id, first_name, last_name, date_of_birth)
        PlayerController.save_player(player)

    @staticmethod
    def save_player(player):
        data = {}
        data['players'] = []

        # ICI JE DOIS VERIFIER SI LE FICHIER JSON EST VIDE
        # SINON JOBTIEN UNE ERREUR A CORRIGER
        with open('data/tournaments.json') as json_file:
            data = json.load(json_file)
            temp = data['players']
            temp.append({
                'id': player.id,
                'first_name': player.first_name,
                'last_name': player.last_name,
                'date_of_birth': player.date_of_birth
            })

        with open('data/tournaments.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
