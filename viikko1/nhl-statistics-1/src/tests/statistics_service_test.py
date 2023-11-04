import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_get_players_returns_correct_amount_of_players(self):
        player_list = self.stats._players

        self.assertEqual(len(player_list), 5)

    def test_search_returns_first_player_with_search_term_in_name(self):
        search_result = self.stats.search("ur")

        self.assertEqual(search_result, self.stats._players[2])

    def test_search_returns_none_if_no_player_name_fits_search_term(self):
        search_result = self.stats.search("lol")

        self.assertEqual(search_result, None)

    def test_team_returns_players_of_team_correctly(self):
        players_of_team = self.stats.team("EDM")

        self.assertEqual(len(players_of_team), 3)
        self.assertEqual(players_of_team[0], self.stats._players[0])
        self.assertEqual(players_of_team[1], self.stats._players[2])
        self.assertEqual(players_of_team[2], self.stats._players[4])

    def test_top_returns_correct_amount_of_players_with_most_points_in_order(self):
        top_players = self.stats.top(1, SortBy.POINTS)

        self.assertEqual(len(top_players), 2)
        self.assertEqual(top_players[0], self.stats._players[4])
        self.assertEqual(top_players[1], self.stats._players[1])

    def test_top_sorts_by_points_without_if_no_criteria_as_parameter(self):
        top_players = self.stats.top(1)

        self.assertEqual(len(top_players), 2)
        self.assertEqual(top_players[0], self.stats._players[4])
        self.assertEqual(top_players[1], self.stats._players[1])

    def test_top_returns_correct_amount_of_players_with_most_goals_order(self):
        top_players = self.stats.top(1, SortBy.GOALS)

        self.assertEqual(len(top_players), 2)
        self.assertEqual(top_players[0], self.stats._players[1])
        self.assertEqual(top_players[1], self.stats._players[3])

    def test_top_returns_correct_amount_of_players_with_most_assists_in_order(self):
        top_players = self.stats.top(1, SortBy.ASSISTS)

        self.assertEqual(len(top_players), 2)
        self.assertEqual(top_players[0], self.stats._players[4])
        self.assertEqual(top_players[1], self.stats._players[3])
