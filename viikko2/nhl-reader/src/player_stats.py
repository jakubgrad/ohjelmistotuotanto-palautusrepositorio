class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader
        self.players = self.player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [player for player in self.players if player.nationality == nationality]
        sorted_players = sorted(filtered_players, key=lambda player: player.points, reverse=True)
        return sorted_players
