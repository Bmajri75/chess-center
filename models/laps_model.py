from dataclasses import dataclass


@dataclass
class Laps:
    name: int
    start_date: int
    start_time: int
    end_date: int
    end_time: int
    games: str = []

    def create_laps(self):
        pass
