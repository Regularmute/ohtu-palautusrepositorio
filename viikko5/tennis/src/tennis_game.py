class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.raw_score1 = 0
        self.raw_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.raw_score1 = self.raw_score1 + 1
        else:
            self.raw_score2 = self.raw_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.raw_score1 == self.raw_score2:
            if self.raw_score1 == 0:
                score = "Love-All"
            elif self.raw_score1 == 1:
                score = "Fifteen-All"
            elif self.raw_score1 == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"
        elif self.raw_score1 >= 4 or self.raw_score2 >= 4:
            minus_result = self.raw_score1 - self. raw_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.raw_score1
                else:
                    score = score + "-"
                    temp_score = self.raw_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
