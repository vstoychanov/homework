from Runner import Runner
import unittest


def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):

    is_frozen = False
    @skip_if_frozen
    def test_walk(self):
        runner = Runner('Test')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    @skip_if_frozen
    def test_run(self):
        runner = Runner('test run')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    @skip_if_frozen
    def test_challenge(self):
        runner = Runner('test runner')
        walker = Runner('test walker')
        for i in range(10):
            runner.run()
            walker.walk()
        self.assertNotEqual(walker.distance, runner.distance)
