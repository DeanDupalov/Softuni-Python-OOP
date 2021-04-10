import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):

    def setUp(self) -> None:
        self.advanced_test = Advanced('test_name')

    def test_init_attributes(self):
        for attr in ['username', 'health', 'card_repository', 'is_dead']:
            self.assertTrue(hasattr(self.advanced_test, attr))

    def test_health_should_be_250(self):
        self.assertEqual(250, self.advanced_test.health)

    def test_take_damage_with_valid_value_should_decrease_health(self):
        self.advanced_test.take_damage(50)
        self.assertEqual(200, self.advanced_test.health)

    def test_take_damage_with_invalid_value_should_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced_test.take_damage(-50)

        expected = "Damage points cannot be less than zero."
        self.assertEqual(expected, str(ex.exception))



if __name__ == '__main__':
    unittest.main()
