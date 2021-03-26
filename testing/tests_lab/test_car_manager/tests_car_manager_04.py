import unittest

from OOP.testing.lab.car_manager_04.car_manager import Car


class CarManagerTest(unittest.TestCase):
    def setUp(self) -> None:
        make = "Test_car"
        model = "Test_model"
        fuel_consumption = 1
        fuel_capacity = 40
        self.car = Car(make, model, fuel_consumption, fuel_capacity)

    def test_CarInitializing_whenGivenAllParameters(self):
        make = "Test_car"
        model = "Test_model"
        fuel_consumption = 1
        fuel_capacity = 4
        fuel_amount = 0
        test_car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual(make, test_car.make)
        self.assertEqual(model, test_car.model)
        self.assertEqual(fuel_capacity, test_car.fuel_capacity)
        self.assertEqual(fuel_consumption, test_car.fuel_consumption)
        self.assertEqual(fuel_amount, test_car.fuel_amount)

    def test_CarMake_shouldReturnsCarMake(self):
        self.assertEqual('Test_car', self.car.make)

    def test_CarMakeSetter_whenGivenNewMake_shouldSetIt(self):
        self.car.make = 'New_test_car'
        self.assertEqual('New_test_car', self.car.make)

    def test_CarMakeSetter_whenNoMakeGiven_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ''

        self.assertIsNotNone(context.exception)

    def test_CarModel_shouldReturnsCarModel(self):
        self.assertEqual('Test_model', self.car.model)

    def test_CarModelSetter_whenGivenNewModel_shouldSetIt(self):
        self.car.model = 'New_test_model'
        self.assertEqual('New_test_model', self.car.model)

    def test_CarModelSetter_whenNoModelGiven_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ''

        self.assertIsNotNone(context.exception)

    def test_CarFuelConsumption_shouldReturnsFuelConsumption(self):
        self.assertEqual(1, self.car.fuel_consumption)

    def test_CarFuelConsumptionSetter_whenGivenValueGreaterThenZero_shouldChangeIt(self):
        self.car.fuel_consumption = 2

        self.assertEqual(2, self.car.fuel_consumption)

    def test_CarFuelConsumptionSetter_whenGivenValueZero_shouldRaise(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertIsNotNone(context.exception)

    def test_CarFuelConsumptionSetter_whenGivenNegativeValue_shouldRaise(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1
        self.assertIsNotNone(context.exception)

    def test_CarFuelCapacity_shouldReturnsCarsCapacity(self):
        self.assertEqual(40, self.car.fuel_capacity)

    def test_CarFuelCapacitySetter_shouldReturnsCarsCapacity(self):
        self.car.fuel_capacity = 100

        self.assertEqual(100, self.car.fuel_capacity)

    def test_CarFuelCapacitySetter_whenGivenValueZero_shouldRaise(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertIsNotNone(context.exception)

    def test_CarFuelCapacitySetter_whenGivenNegativeValue_shouldRaise(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1
        self.assertIsNotNone(context.exception)

    def test_CarFuelAmount_shouldReturnsCarsFuelAmount(self):
        self.assertEqual(0, self.car.fuel_amount)

    def test_CarFuelAmountSetter_shouldReturnsCarsFuelAmount(self):
        self.car.fuel_amount = 999

        self.assertEqual(999, self.car.fuel_amount)

    def test_CarFuelAmountSetter_whenGivenNegativeValue_shouldRaise(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1
        self.assertIsNotNone(context.exception)

    def test_CarRefuel_whenGivenValidValue_shouldIncreaseFuel(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_CarRefuel_whenGivenValidValueAndExedFuelCapacity_shouldIncreaseFuelAndReachCapacity(self):
        self.car.refuel(100)
        self.assertEqual(40, self.car.fuel_amount)

    def test_CarRefuel_whenGivenNegativeValue_shouldRaise(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-10)

        self.assertIsNotNone(context.exception)

    def test_CarRefuel_whenGivenZero_shouldRaise(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)

        self.assertIsNotNone(context.exception)

    def test_CarDrive_whenHaveNeededFuel_shouldDecreaseFuel(self):
        self.car.refuel(self.car.fuel_capacity)
        distance = 10
        self.car.drive(distance)

        expected = self.car.fuel_capacity - (distance / 100 * self.car.fuel_consumption)
        actual = self.car.fuel_amount

        self.assertEqual(expected, actual)

    def test_CarDrive_whenFuelNotEnough_shouldRaise(self):
        with self.assertRaises(Exception) as context:
            distance = 10
            self.car.drive(distance)

        self.assertIsNotNone(context.exception)

if __name__ == '__main__':
    unittest.main()
