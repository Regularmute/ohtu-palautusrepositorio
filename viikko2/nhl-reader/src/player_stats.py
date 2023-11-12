class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self._players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        top_scorers_of_nation = []
        for player in self._players:
            if player.nationality == nationality:
                top_scorers_of_nation.append(player)

        top_scorers_of_nation.sort(
            key=lambda player: player.score, reverse=True)
        
        return top_scorers_of_nation
