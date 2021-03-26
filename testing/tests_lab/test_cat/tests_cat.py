import unittest

from OOP.testing.lab.cat_02.cat import Cat


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        name = 'Test Cat'
        self.cat = Cat(name)

    def test_CatEat_whenCatIsNotFed_shouldIncreaseSizeBy1(self):
        """
            Cat's size is increased after eating
        """
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_CatEat_whenCatIsNotFed_shouldBeFedAfterEat(self):
        """
            Cat is fed after eating
        """
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_CatEat_whenCatIsFed_shouldRaise(self):
        """
            Cat cannot eat if already fed, raises an error
        """
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()

        self.assertIsNotNone(context.exception)

    def test_CatSleep_whenCatIsNotFed_shouldRaise(self):
        """
            Cat cannot fall asleep if not fed, raises an error
        """
        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertIsNotNone(context.exception)

    def test_CatSleep_shouldNotBeSleepy(self):
        """
            Cat is not sleepy after sleeping
        """
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
