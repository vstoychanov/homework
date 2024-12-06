import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усейн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.assertTrue(str(results[max(results.keys())]) == "Ник")
        self.__class__.all_results["usain_and_nick"] = {k: str(v) for k, v in results.items()}

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(str(results[max(results.keys())]) == "Ник")
        self.__class__.all_results["andrey_and_nick"] = {k: str(v) for k, v in results.items()}

    def test_all_three_runners(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(str(results[max(results.keys())]) == "Ник")
        self.__class__.all_results["all_three_runners"] = {k: str(v) for k, v in results.items()}

if __name__ == '__main__':
    unittest.main()