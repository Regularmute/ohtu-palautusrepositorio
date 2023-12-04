class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.raw_score1 = 0
        self.raw_score2 = 0
        self.tennis_scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.raw_score1 = self.raw_score1 + 1
        else:
            self.raw_score2 = self.raw_score2 + 1

    def game_is_even(self):
        return self.raw_score1 == self.raw_score2

    def game_is_over(self):
        return max(self.raw_score1, self.raw_score2) > 3\
            and self.score_difference() > 1

    def is_game_point(self):
        return max(self.raw_score1, self.raw_score2) > 3\
            and self.score_difference() == 1

    def score_difference(self):
        return abs(self.raw_score1 - self.raw_score2)

    def get_score(self):
        if self.game_is_over():
            if self.raw_score1 > self.raw_score2:
                winning_player = "player1"
            else:
                winning_player = "player2"
            return f"Win for {winning_player}"

        elif self.is_game_point():
            if self.raw_score1 > self.raw_score2:
                leading_player = "player1"
            else:
                leading_player = "player2"
            return f"Advantage {leading_player}"

        elif self.game_is_even():
            if self.raw_score1 < 3:
                return self.tennis_scores.get(self.raw_score1) + "-All"
            else:
                return "Deuce"

        player1_final_score = self.tennis_scores.get(self.raw_score1)
        player2_final_score = self.tennis_scores.get(self.raw_score2)
        return f"{player1_final_score}-{player2_final_score}"

