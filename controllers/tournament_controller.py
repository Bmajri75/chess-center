import json

from models.tournament_model import Tournament
from json.decoder import JSONDecodeError


class TournamentController:
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
        try:
            with open('data/tournaments.json') as json_file:
                data = json.load(json_file)
        except JSONDecodeError:
            data = {}
            data['tournament'] = []

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
