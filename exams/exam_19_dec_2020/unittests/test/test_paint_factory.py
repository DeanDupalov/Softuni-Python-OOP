import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory('test_name', 2)

    def test_init(self):
        test_factory = PaintFactory('name', 10)
        self.assertEqual(test_factory.name, 'name')
        self.assertEqual(test_factory.capacity, 10)

    def test_add_ingredient_should_increase_quantity(self):
        self.factory.add_ingredient('blue', 1)
        expected_len = 1
        actual_len = len(self.factory.ingredients)

        self.assertEqual(expected_len, actual_len)

        expected_quantity = 1
        actual_quantity = self.factory.ingredients['blue']
        self.assertEqual(expected_quantity, actual_quantity)

    def test_add_ingredient__when_not_valid_ingredient__should_raise(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient('test', 1)

        expected = "Ingredient of type test not allowed in PaintFactory"
        actual = ex.exception.args[0]
        self.assertEqual(expected, actual)

    def test_add_ingredient__when_not_enough_capacity__should_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient('blue', 10)
        expected = "Not enough space in factory"
        actual = ex.exception.args[0]
        self.assertEqual(expected, actual)


    def test_remove_ingredient__should_decrease_quantity(self):
        self.factory.add_ingredient('blue', 2)
        self.factory.remove_ingredient('blue', 1)

        expected_len = 1
        actual_len = self.factory.ingredients['blue']

        self.assertEqual(expected_len, actual_len)

    def test_remove_ingredient__when_missing_in_factory__should_raise(self):
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient('red', 1)
        expected = "No such product in the factory"
        actual = ex.exception.args[0]
        self.assertEqual(expected, actual)

    def test_remove_ingredient__when_given_quantity_bigger_then_current__should_raise(self):
        self.factory.add_ingredient('red', 2)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient('red', 20)
        expected = "Ingredient quantity cannot be less than zero"
        actual = ex.exception.args[0]
        self.assertEqual(expected, actual)

    def test_products_should_return_ingredients_in_factory(self):
        self.factory.add_ingredient('red', 2)
        self.factory.add_ingredient('blue', 2)
        self.assertEqual(self.factory.products, {'blue': 2, 'red': 2})


if __name__ == '__main__':
    unittest.main()
