import unittest
from OOP.testing.lab.worker.worker_01 import Worker


class WorkerTests(unittest.TestCase):
    def test_workerInit_whenCorrectNameSalaryEnergy_shouldBeInitialized(self):
        """
            Test if the worker is initialized with correct name, salary and energy
        """
        name = 'Test Worker'
        salary = 500
        energy = 5
        money = 0
        worker = Worker(name, salary, energy)

        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)
        self.assertEqual(money, worker.money)

    def test_workerRest_checkIfEnergyIsIncremented(self):
        """
            Test if the worker's energy is incremented after the rest method is called
        """
        name = 'Test Worker'
        salary = 500
        energy = 5
        worker = Worker(name, salary, energy)

        worker.rest()
        self.assertEqual(6, worker.energy)

    def test_workerWork_whenEnergyIsZero_shouldRaise(self):
        """
            Test if an error is raised if the worker tries to work with negative energy or equal to 0
        """
        name = 'Test Worker'
        salary = 500
        energy = 0
        worker = Worker(name, salary, energy)

        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertIsNotNone(context.exception)

    def test_workerWork_whenEnergyAboveZero_shouldIncreasedMoneyWithHisSalary(self):
        """
            Test if the worker's money is increased by his salary correctly after the work method is called
        """
        name = 'Test Worker'
        salary = 500
        energy = 5
        worker = Worker(name, salary, energy)
        worker.work()

        self.assertEqual(salary, worker.money)

    def test_workerWork_whenEnergyAboveZero_shouldDecreasedEnergyByOne(self):
        """
            Test if the worker's energy is decreased after the work method is called
        """
        name = 'Test Worker'
        salary = 500
        energy = 5
        worker = Worker(name, salary, energy)

        worker.work()
        self.assertEqual(energy - 1, worker.energy)

    def test_workerGetInfo_shouldReturnsRightString(self):
        """
            Test if the get_info method returns the proper string with correct values
        """
        name = 'Test Worker'
        salary = 500
        energy = 5
        worker = Worker(name, salary, energy)
        money = 0
        expected_string = f'{name} has saved {money} money.'
        result = worker.get_info()

        self.assertEqual(expected_string, result)



if __name__ == '__main__':
    unittest.main()
