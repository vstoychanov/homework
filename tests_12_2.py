import unittest
from runner_and_tournament import Runner, Tournament

def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @skip_if_frozen
    def setUp(self):
        self.usain = Runner('Усейн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)
    @skip_if_frozen
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.assertTrue(str(results[max(results.keys())]) == "Ник")
        self.__class__.all_results["usain_and_nick"] = {k: str(v) for k, v in results.items()}
    @skip_if_frozen
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(str(results[max(results.keys())]) == "Ник")
        self.__class__.all_results["andrey_and_nick"] = {k: str(v) for k, v in results.items()}
    @skip_if_frozen
    def test_all_three_runners(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(str(results[max(results.keys())]) == "Ник")
        self.__class__.all_results["all_three_runners"] = {k: str(v) for k, v in results.items()}

if __name__ == '__main__':
    unittest.main()