class Matchs:
    def __init__(self, player_one, player_two):
        self.joueur_one = player_one
        self.joueur_two = player_two

    def point_counter(self, result):
        match result:
            case "winner":
                pass
            case "looser":
                pass
            case "null":
                pass
