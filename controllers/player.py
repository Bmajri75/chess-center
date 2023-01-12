import json


class Player:
    list_players = []

    def __init__(self, id, first_name, last_name, date_of_birth):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def save_player(self):
        Player.list_players.append(Player())

    def to_python(self):
        pass


class Tournament:
    def __init__(self, tournament_name, place, start_date, end_date, curent_laps, laps_liste, list_players, description, total_laps=4):
        self.tournament_name = tournament_name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.curent_laps = curent_laps
        self.laps_liste = laps_liste
        self.liste_players = list_players
        self.description = description
        self.total_laps = total_laps

    def creat_tournament(self):
        pass

    def to_python(self):
        pass
