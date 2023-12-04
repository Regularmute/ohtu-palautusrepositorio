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
        score_string = ""

        if self.game_is_even():
            if self.raw_score1 < 3:
                score_string = self.tennis_scores.get(self.raw_score1) + "-All"
            else:
                score_string = "Deuce"
        elif self.raw_score1 >= 4 or self.raw_score2 >= 4:
            minus_result = self.raw_score1 - self.raw_score2

            if minus_result == 1:
                score_string = "Advantage player1"
            elif minus_result == -1:
                score_string = "Advantage player2"
            elif minus_result >= 2:
                score_string = "Win for player1"
            else:
                score_string = "Win for player2"
        else:
            player1_final_score = self.tennis_scores.get(self.raw_score1)
            player2_final_score = self.tennis_scores.get(self.raw_score2)
            score_string = f"{player1_final_score}-{player2_final_score}"

        return score_string
