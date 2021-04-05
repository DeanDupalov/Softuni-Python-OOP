import unittest
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.test_room = Room('Dupalovi', 1000, 2)

    def test_init(self):

        for attr in ['family_name', 'budget', 'members_count', 'children', 'expenses']:
            self.assertTrue(hasattr(self.test_room, attr))

        self.assertEqual('Dupalovi', self.test_room.family_name)
        self.assertEqual(1000, self.test_room.budget)
        self.assertEqual(2, self.test_room.members_count)
        self.assertEqual(0, self.test_room.expenses)
        self.assertEqual([], self.test_room.children)

    # def test_expenses_when_valid_value_should_set_expenses(self):
    #     test_room = Room('Dupalovi', 1000, 2)
    #     test_room.expenses = 500
    #     self.assertEqual(test_room.expenses, 500)

    def test_expenses_when_negative_value_should_raise_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.test_room.expenses = -500
        expected = "Expenses cannot be negative"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    # def test_calculate_expenses_with_appliances(self):
    #     test_room = Room('Dupalovi', 1000, 2)
    #     test_room.appliances = [TV(), Laptop(), TV(), Laptop()]  # 1.5, 1
    #     test_room.calculate_expenses(test_room.appliances)
    #     expected = 150
    #     actual = test_room.expenses
    #     self.assertEqual(expected, actual)
    #
    # def test_calculate_expenses_with_children(self):
    #     test_room = Room('Dupalovi', 1000, 2)
    #     test_room.children = [
    #         Child(5, 1, 2, 1),
    #         Child(3, 2),
    #     ]
    #     test_room.calculate_expenses(test_room.children)
    #     expected = 420
    #     actual = test_room.expenses
    #     self.assertEqual(expected, actual)
    #
    # def test_str_method(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
