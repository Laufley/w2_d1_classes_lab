class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = len([])
    def add_player(self, name):
        self.players.append(name)
    def has_player(self, name):
        for player in self.players:
            if player == name:
                return True
        return False
    def play_game(self, result):
        if result == True:
            self.points += 3
    



    