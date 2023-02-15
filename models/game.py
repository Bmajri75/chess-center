from dataclasses import dataclass


@dataclass
class Game:
    player_one: str
    player_two: str

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
