import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_a_player_from_the_PlayerReader(self):

        self.assertAlmostEqual(self.stats.search("Semenko").name, "Semenko")

    def test_search_returns_none_for_nonexisting_player(self):

        self.assertAlmostEqual(self.stats.search("Gal"), None)

    def test_team_returns_players_of_the_same_team(self):

        self.assertAlmostEqual(len(self.stats.team("EDM")), 3)

    def test_top_returns_sorted_players(self):

        self.assertEqual(self.stats.top(2)[1].name, "Lemieux")