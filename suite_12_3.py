from unittest import TestSuite, TestLoader, TextTestRunner

from test_12_2 import TournamentTest
from tests_12_1 import RunnerTest

test_system = TestSuite()
test_system.addTest(TestLoader().loadTestsFromTestCase(RunnerTest))
test_system.addTest(TestLoader().loadTestsFromTestCase(TournamentTest))
runner = TextTestRunner(verbosity=2)
runner.run(test_system)
