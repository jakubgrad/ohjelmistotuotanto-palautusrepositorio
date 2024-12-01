score_labels = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score 
    
    def increment_score(self):
        self.score = self.score + 1

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.player1.score = 0
        self.player2.score = 0

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.score = self.player1.score + 1
        else:
            self.player2.score = self.player2.score + 1

    def _get_even_score(self):
        if self.player1.score <= 2:
            return score_labels[self.player1.score] + "-All"
        return "Deuce"

    def _get_late_game_score(self):
        leader = max([self.player1,self.player2], key=lambda player: player.score)
        if abs(self.player1.score - self.player2.score)>=2:
            return f"Win for {leader.name}" 
        return f"Advantage {leader.name}"

    def get_score(self):
        if self.player1.score == self.player2.score:
            return self._get_even_score()
        if self.player1.score >= 4 or self.player2.score >= 4:
            return self._get_late_game_score()        
        return score_labels[self.player1.score] + "-" + score_labels[self.player2.score]
            
