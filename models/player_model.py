from dataclasses import dataclass


@dataclass
class Player:
    id: str
    first_name: str
    last_name: str
    date_of_birth: str
