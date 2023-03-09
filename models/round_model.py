from dataclasses import dataclass


@dataclass
class Round:
    start_date: str
    start_time: str
    end_date: str
    end_time: str
    name: int
