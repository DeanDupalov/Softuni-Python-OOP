import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.test_mammal = Mammal('test_name', 'cat', 'bow bow')

    def test_initialized_when_with_correct_name_type_sound(self):
        mammal = Mammal('Suzi', 'dog', 'bow bow')
        self.assertEqual('Suzi', mammal.name)
        self.assertEqual('dog', mammal.type)
        self.assertEqual('bow bow', mammal.sound)
        actual_kingdom = mammal.get_kingdom()
        self.assertEqual('animals', actual_kingdom )


    def test_make_sound_should_return_message(self):
        actual = self.test_mammal.make_sound()
        expected = "test_name makes bow bow"
        self.assertEqual(actual, expected)

    def test_get_kingdom(self):
        actual = self.test_mammal.get_kingdom()
        expected = "animals"
        self.assertEqual(actual, expected)

    def test_info(self):
        actual = self.test_mammal.info()
        expected = "test_name is of type cat"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
