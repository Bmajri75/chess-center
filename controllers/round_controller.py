from dataclasses import dataclass
from models.round_model import Round


@dataclass
class Round_controller:
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

# Round_controller.create_round(
#     "10/10/10", "10h", "12/12/12", '13/13/13', ['player1', 'player2'], 3)

# IMPLEMENTER LE Round AVEC LES CHARACTERISTIQUES

# APPELER CETTE CLASS SUR LA VUE POUR IMPLEMENTER LES METHODE ADEQUATE
