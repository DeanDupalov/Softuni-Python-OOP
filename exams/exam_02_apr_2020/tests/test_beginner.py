import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):

    def setUp(self) -> None:
        self.beginner = Beginner('test_name')

    def test_init_attributes(self):
        for attr in ['username', 'health', 'card_repository', 'is_dead']:
            self.assertTrue(hasattr(self.beginner, attr))

    def test_health_should_be_50(self):
        self.assertEqual(50, self.beginner.health)


    def test_take_damage_with_valid_value_should_decrease_health(self):
        self.beginner.take_damage(49)
        self.assertEqual(1, self.beginner.health)

    def test_take_damage_with_invalid_value_should_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.beginner.take_damage(-50)

        expected = "Damage points cannot be less than zero."
        self.assertEqual(expected, str(ex.exception))



if __name__ == '__main__':
    unittest.main()
