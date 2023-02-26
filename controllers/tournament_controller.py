import json

from models.tournament_model import Tournament
from controllers.player_controller import Validator
from json.decoder import JSONDecodeError


class TournamentController(Validator):
    @staticmethod
    def creat_tournament(name,
                         location,
                         start_date,
                         end_date,
                         number_of_laps,
                         current_lap,
                         rounds,
                         players,
                         description):
        tournament = Tournament(name,
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
