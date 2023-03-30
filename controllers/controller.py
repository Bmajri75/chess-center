import json
import datetime
import re

from dataclasses import dataclass
from json.decoder import JSONDecodeError
from models.model import Tournament
from models.model import Round
from models.model import Player
from models.model import Match


@dataclass
class Validator:
    @staticmethod
    def verif_id(id):
        # Verifie si les ID comporte bien le format => AB12345
        pattern = r'[A-Z]{2}\d{5}'
        match = re.search(pattern, id)
        if match:
            return True
        else:
            return False

    @staticmethod
    def verif_date(date):
        # Verifie si la Date est au format => 01/01/2020
        datetime.datetime.strptime(date, '%d/%m/%Y').date()
        return True

    @staticmethod
    def validator_methode(player):
        # on verifie si les validateurs sont bien True
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
class TournamentController(Validator):
    @staticmethod
    def creat_tournament(
            name,
            location,
            start_date,
            end_date,
            number_of_laps,
            current_lap,
            rounds,
            players,
            description):
        tournament = Tournament(
            name,
            location,
            start_date,
            end_date,
            number_of_laps,
            current_lap,
            rounds,
            players,
            description)
        TournamentController.save_tournament(tournament)

    @staticmethod
    def save_tournament(tournament):
        if Validator.verif_date(tournament.start_date and tournament.end_date):
            try:
                with open('data/tournaments.json') as json_file:
                    data = json.load(json_file)
            except JSONDecodeError:
                data = {}
                data['tournament'] = []
                data['players'] = []

            temp = data['tournament']
            temp.append({
                        'name': tournament.name,
                        'location': tournament.location,
                        'start_date': tournament.start_date,
                        'end_date': tournament.end_date,
                        'number_of_laps': tournament.number_of_laps,
                        'current_lap': tournament.current_lap,
                        'rounds': tournament.rounds,
                        'players': tournament.players,
                        'description': tournament.description,
                        })
            with open('data/tournaments.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)


@dataclass
class RoundController:
    @staticmethod
    def create_round(
        start_date,
        start_time,
        end_date,
        end_time,
        name=1,
        matchs=[]
    ):
        round = Round(
            start_date,
            start_time,
            end_date,
            end_time,
            name,
            matchs
        )
        return round

    # def implement_round(round):
    #     return round.name + 1
    def ajouter_match(joueur1, score1, joueur2, score2):
        match = ([joueur1, score1], [joueur2, score2])
        round.matchs.append(match)

# RoundController.create_round(
#     "10/10/10", "10h", "12/12/12", '13/13/13', ['player1', 'player2'], 3)

# IMPLEMENTER LE Round AVEC LES CHARACTERISTIQUES

# APPELER CETTE CLASS SUR LA VUE POUR IMPLEMENTER LES METHODE ADEQUATE


@dataclass
class PlayerController(Validator):
    # ! cette class reprend les methodes de la class Validator
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


@dataclass
class MatchController():
    def creat_match(players):
        pass

    def points_distributor(self, winner, looser, null):
        # winner = 1
        # looser = 0
        # null = 0.5
        pass
    """cette fonction dois prendre 2 joueurs
       le gagnant 1 pt
       le perdant 0pt
       en cas de nul 0.5 chacun
    """
# class Parent controller
#
