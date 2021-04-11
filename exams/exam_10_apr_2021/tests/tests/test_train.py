import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self) -> None:
        self.train = Train('test_name', 30)

    def test_train_init_attributes(self):
        for attr in ['name', 'capacity', 'passengers']:
            self.assertTrue(hasattr(self.train, attr))

        self.assertEqual('test_name', self.train.name)
        self.assertEqual(30, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add(self):
        actual = self.train.add('test_person')
        expected = f"Added passenger test_person"

        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual(expected, actual)

    def test_add_when_full_capacity_should_raise(self):
        test_train = Train('test', 1)
        test_train.add('test_person')
        with self.assertRaises(ValueError)as ex:
            test_train.add('test_person_two')

        self.assertEqual("Train is full", str(ex.exception))

    def test_train_when_passenger_on_board_should_raise(self):
        test_train = Train('test', 3)
        test_train.add('test_person')
        with self.assertRaises(ValueError)as ex:
            test_train.add('test_person')

        self.assertEqual("Passenger test_person Exists", str(ex.exception))

    def test_remove(self):
        test_train = Train('test', 3)
        test_train.add('test_person')
        test_train.add('test_person_two')
        expected = "Removed test_person"
        self.assertEqual(2, len(test_train.passengers))
        actual = test_train.remove('test_person')
        self.assertEqual(1, len(test_train.passengers))
        self.assertEqual(expected, actual)

    def test_remove_when_passenger_not_on_board_should_raise(self):
        test_train = Train('test', 3)
        test_train.add('test_person')
        with self.assertRaises(ValueError)as ex:
            test_train.remove('test_person_two')

        self.assertEqual("Passenger Not Found", str(ex.exception))



if __name__ == '__main__':
    unittest.main()