import datetime
import re
import json

from dataclasses import dataclass
from json.decoder import JSONDecodeError
from models.player_model import Player


@dataclass
class Validator:
    @staticmethod
    def verif_id(id):
        pattern = r'[A-Z]{2}\d{5}'
        match = re.search(pattern, id)
        if match:
            return True
        else:
            return False

    @staticmethod
    def verif_date(date):
        datetime.datetime.strptime(date, '%d/%m/%Y').date()
        return True

    @staticmethod
    def validator_methode(player):
        """methode qui valide les format des donnee entrer de la views"""
        if PlayerController.verif_id(player.id):
            try:
                PlayerController.verif_date(player.date_of_birth)
                return True
            except ValueError:
                # Si la conversion échoue, afficher un message d'erreur
                print("La date n'est pas au format correct"
                      "Format attendu '18/01/1986'")
        else:
            print("Veuillez entrer un ID Valide Format 'AB12345'")
            return False


@dataclass
class PlayerController(Validator):
    """ Create a new player, if player is not in the data """

    @staticmethod
    def create_player(id, first_name, last_name, date_of_birth):
        player = Player(id, first_name, last_name, date_of_birth)
        if Validator.validator_methode(player):
            PlayerController.save_player(player)

    @staticmethod
    def save_player(player):
        try:
            with open('data/tournaments.json') as json_file:
                data = json.load(json_file)
        except JSONDecodeError:
            data = {}
            data['players'] = []
            data['tournament'] = []

        temp = data['players']
        temp.append({
            'id': player.id,
            'first_name': player.first_name,
            'last_name': player.last_name,
            'date_of_birth': player.date_of_birth
        })

        with open('data/tournaments.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)


# class Parent controller
#
