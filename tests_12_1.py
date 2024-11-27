from Runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Test')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('test run')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner('test runner')
        walker = Runner('test walker')
        for i in range(10):
            runner.run()
            walker.walk()
        self.assertNotEqual(walker.distance, runner.distance)
