class Player:
    """La player List est une variable de class"""

    def __init__(self, id, first_name, last_name, date_of_birth):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.player_list = []

    def save_player(self):
        self.player_list.append(self)
        pass


player1 = Player("ae345", "bechir", "Majri", "18/01/1986")

print(player1.save_player())
print(player1.player_list)
