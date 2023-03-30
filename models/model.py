from dataclasses import dataclass


# ! Les models
# Tournois
# Round
# Matchs
# joueur


@dataclass
class Tournament:
    name: str
    location: str
    start_date: str
    end_date: str
    number_of_laps: int = 4,
    current_lap: int = 0,
    rounds: list = [],
    players: list = [],
    description: str = ""


@dataclass
class Round:
    start_date: str
    start_time: str
    end_date: str
    end_time: str
    name: int
    matchs: list


@dataclass
class Match:
    player_one = str
    player_two = str
    score_player_one = int
    score_player_two = int
    match = ([player_one, score_player_one], [player_two, score_player_two])


@dataclass
class Player:
    id: str
    first_name: str
    last_name: str
    date_of_birth: str
    # points: int
