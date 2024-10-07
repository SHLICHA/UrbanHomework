import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for results in cls.all_results:
            print(results)

    def testUsainAndNik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1][2] == self.runner3)

    def testAndreyAndNik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        self.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1][2] == self.runner3)

    def testUsainAndreyAndNik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1][3] == self.runner3)
