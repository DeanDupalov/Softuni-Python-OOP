import unittest

from cat_02.cat import Cat


class TestCat(unittest.TestCase):

    def setUp(self) -> None:
        self.cat = Cat('test_name')

    def test_eat__should_increase_size(self):
        """Cat's size is increased after eating"""

        self.cat.eat()

        expected_size = 1
        self.assertEqual(expected_size, self.cat.size)

    def test_eat__should_be_fed_true(self):
        """Cat is fed after eating"""
        self.cat.eat()
        expected_fed = True
        self.assertEqual(expected_fed, self.cat.fed)

    def test_eat__when_is_fed_can_not_eat__should_raise(self):
        """Cat cannot eat if already fed, raises an error"""
        self.cat.eat()

        with self.assertRaises(Exception) as context:
            self.cat.eat()

        expected_exception = 'Already fed.'
        self.assertEqual(expected_exception, context.exception.args[0])

    def test_sleep__when_not_fed__should_raise(self):
        """Cat cannot fall asleep if not fed, raises an error"""
        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertIsNotNone(context.exception)

    def test_sleepy__after_sleep_can_not_be_sleepy(self):
        """Cat is not sleepy after sleeping"""
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
