import logging
import unittest

from rt_with_exceptions import Runner

logging.basicConfig(
        level=logging.INFO,
        filemode='w',
        filename='runner_tests.log',
        encoding='UTF-8',
        format='%(asctime)s, %(levelname)s, %(message)s, %(funcName)s, %(lineno)s'
    )


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            walker = Runner('Павел', -1)
            for i in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = Runner(5, 5)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walker = Runner('Павел')
        runner = Runner('Павел')
        for i in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)
