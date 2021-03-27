import unittest

from worker.worker_01 import Worker


class WorkerTests(unittest.TestCase):

    def test_initialized_when_with_correct_name_salary_and_energy(self):
        """Test if the worker is initialized with correct name, salary and energy"""
        test_worker = Worker('Test', 5000, 100)
        expected_name = 'Test'
        expected_salary = 5000
        expected_energy = 100

        self.assertEqual(expected_name, test_worker.name)
        self.assertEqual(expected_salary, test_worker.salary)
        self.assertEqual(expected_energy, test_worker.energy)

    def test_rest_when_called_should_increment_energy(self):
        """Test if the worker's energy is incremented after the rest method is called"""
        test_worker = Worker('Test', 5000, 50)
        expected_energy = 51
        test_worker.rest()
        self.assertEqual(expected_energy, test_worker.energy, )

    def test_work__when_energy_is_negative_or_zero__should_raise(self):
        """Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        test_worker = Worker('Test', 5000, 0)

        with self.assertRaises(Exception) as context:
            test_worker.work()

        expected_msg = "Not enough energy."
        self.assertEqual(expected_msg, context.exception.__str__())

    def test_work__should_increase_money_with_salary(self):
        """Test if the worker's money is increased by his salary correctly after the work method is called"""
        test_worker = Worker('Test', 5000, 50)

        test_worker.work()
        test_worker.work()

        self.assertEqual(10000, test_worker.money)

    def test_work_should_decrease_energy(self):
        """Test if the worker's energy is decreased after the work method is called"""
        test_worker = Worker('Test', 5000, 1)

        test_worker.work()
        self.assertEqual(0, test_worker.energy)

    def test_get_info__should_return_right_string(self):
        """Test if the get_info method returns the proper string with correct value"""
        test_worker = Worker('Test_name', 5000, 50)
        test_worker.work()
        test_worker.work()
        message = test_worker.get_info()
        expected_message = 'Test_name has saved 10000 money.'

        self.assertEqual(expected_message, message)


if __name__ == '__main__':
    unittest.main()
