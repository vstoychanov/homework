import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner(name="walker", speed=-5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            self.fail(f"Тест завершился исключением: {e}")

    def test_run(self):
        try:
            runner = Runner(name="runner", speed=10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            self.fail(f"Тест завершился исключением: {e}")

