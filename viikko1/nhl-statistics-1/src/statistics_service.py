from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists


class StatisticsService:
    def __init__(self, reader):
        self.reader = reader

        self._players = self.reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, criteria=SortBy.POINTS):
        sorting_key=sort_by_points
        if criteria == SortBy.GOALS:
            sorting_key=sort_by_goals
        elif criteria == SortBy.ASSISTS:
            sorting_key=sort_by_assists

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sorting_key
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
