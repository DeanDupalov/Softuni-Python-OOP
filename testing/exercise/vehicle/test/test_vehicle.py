import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(50, 100)

    # def test_initialized_when_given_correct_fuel_horse_power(self):
    #     test_car = Vehicle(60, 70)
    #     self.assertEqual(1.25, test_car.DEFAULT_FUEL_CONSUMPTION)
    #     self.assertEqual(60, test_car.fuel)
    #     self.assertEqual(60, test_car.capacity)
    #     self.assertEqual(70, test_car.horse_power)

    def test_drive_when_fuel_is_enough__should_decrease_fuel(self):
        self.car.drive(10)
        expected = 37.5
        actual = self.car.fuel

        self.assertEqual(actual, expected)

    def test_drive__when_fuel_not_enough__should_raise(self):
        expected = "Not enough fuel"
        with self.assertRaises(Exception) as context:
            self.car.drive(200)

        self.assertIsNotNone(context.exception)
        self.assertEqual(expected, context.exception.args[0])

    def test_drive_when_given_invalid_parameters(self):
        pass

    def test_refuel__when_given_valid_fuel_amount__should_increase_fuel(self):
        self.car.drive(10)
        self.car.refuel(12.5)

        expected = 50
        self.assertEqual(expected, self.car.fuel)

    def test_refuel__when_given_valid_fuel_reach_capacity__should_raise(self):
        self.car.drive(10)

        with self.assertRaises(Exception) as context:
            self.car.refuel(20)

        expected = "Too much fuel"

        self.assertEqual(expected, context.exception.args[0])

    def test_str_should_return_right_message(self):
        self.car.drive(10)

        expected = f"The vehicle has 100 " \
                   f"horse power with 37.5 " \
                   f"fuel left and 1.25 fuel consumption"

        actual = self.car.__str__()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
