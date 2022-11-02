import unittest
from statistics import Statistics, SortBy
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

class testStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics=Statistics(PlayerReaderStub())

    def test_search_success(self):
        self.assertEqual(str(self.statistics.search("Semenko")),"Semenko EDM 4 + 12 = 16")

    def test_search_failure(self):
        self.assertEqual(str(self.statistics.search("none")),"None")

    def test_top_defaults(self):
        self.assertEqual(str(self.statistics.top(1)[0]),"Gretzky EDM 35 + 89 = 124")

    def test_top_goals(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.GOALS)[0]),"Lemieux PIT 45 + 54 = 99")

    def test_top_assists(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.ASSISTS)[0]),"Gretzky EDM 35 + 89 = 124")

    def test_team(self):
        self.assertEqual(str(self.statistics.team("DET")[0]),"Yzerman DET 42 + 56 = 98")
