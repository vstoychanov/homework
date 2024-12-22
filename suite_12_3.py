import unittest
import tests_12_1
import tests_12_2

tour_test = unittest.TestSuite()
tour_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
tour_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tour_test)
