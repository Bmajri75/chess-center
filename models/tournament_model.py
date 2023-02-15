from dataclasses import dataclass


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
