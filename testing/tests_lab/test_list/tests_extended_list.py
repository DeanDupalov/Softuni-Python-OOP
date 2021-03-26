import unittest

from OOP.testing.lab.list_03.extended_list import IntegerList


class IntegerListTest(unittest.TestCase):
    def test_IntegerListInit_whenOnlyIntegers_shouldStoreThem(self):
        """
            - test init method, should accept only ints and store them
        """
        values = [1, 3, 5, 7, 9]
        new_list = IntegerList(*values)
        self.assertEqual(values, new_list.get_data())

    def test_IntegerListInit_whenOnlyNotIntegers_shouldNotStoreThem(self):
        """
            - test init method, if not only ints will not store them
        """
        values = [1, 3, 5, 'Dean', 7, 9]
        test_list = IntegerList(*values)
        self.assertNotIn('Dean', test_list.get_data())

    def test_IntegerListAdd_whenValueInt_shouldStoreItAndReturnsGetData(self):
        """
            - test 'add' operation, should add an element and returns the list
        """

        test_list = IntegerList()
        test_list.add(1000)
        self.assertListEqual([1000], test_list.get_data())

    def test_IntegerListAdd_whenValueNotInt_shouldRaiseValueError(self):
        """
            - test 'add' operation, if el is not int should return ValueError
        """
        test_list = IntegerList(1, 3, 5)
        with self.assertRaises(ValueError) as context:
            test_list.add('Dean')
        self.assertIsNotNone(context.exception)
        # self.assertEqual('ValueError("Element is not Integer")', context.exception)

    def test_IntegerListRemoveIndex_shouldRemoveTheElementAndReturnsIt(self):
        """
            - test 'remove_index' operation removes the element on that index and returns it
        """
        values = [1, 3, 5, 7, 9]
        test_list = IntegerList(*values)
        el = test_list.remove_index(0)
        self.assertEqual(1, el)
        self.assertEqual([3, 5, 7, 9], test_list.get_data())

    def test_IntegerListRemoveIndex_whenInvalidIndex_shouldRaiseIndexError(self):
        """
            - test 'remove_index' if the index is out of range, an IndexError is thrown
        """
        values = [1, 3, 5, 7, 9]
        test_list = IntegerList(*values)
        test_invalid_id = len(values)
        with self.assertRaises(IndexError) as contest:
            test_list.remove_index(test_invalid_id)

        self.assertIsNotNone(contest.exception)

    def test_IntegerListGet_whenGivenValidIndex_shouldReturnSpecificElement(self):
        """
            - test 'get', should return specific element
        """
        values = [1, 3, 5, 7, 9]
        test_list = IntegerList(*values)

        self.assertEqual(9, test_list.get(-1))

    def test_IntegerListGet_whenInvalidIndex_shouldRaiseIndexError(self):
        """
            - test 'get', if index out of range should return IndexError
        """
        values = [1, 3, 5, 7, 9]
        test_list = IntegerList(*values)
        test_invalid_id = len(values)
        with self.assertRaises(IndexError) as contest:
            test_list.get(test_invalid_id)

        self.assertIsNotNone(contest.exception)

    def test_IntegerListInsert_whenValueIsInteger_shouldInsertAtGivenIdx(self):
        """
            - test 'insert' should insert the element at the given idx
        """
        values = [1, 3, 5, 7, 9]
        test_list = IntegerList(*values)
        test_list.insert(1, 999)
        self.assertListEqual([1, 999, 3, 5, 7, 9], test_list.get_data())

    def test_IntegerListInsert_whenInvalidIdx_shouldRaiseIndexError(self):
        """
            - test 'insert' if the index is out of range, IndexError is thrown
        """
        values = [1, 3, 5, 7, 9]
        test_list = IntegerList(*values)
        test_invalid_id = len(values)
        with self.assertRaises(IndexError) as contest:
            test_list.insert(test_invalid_id, 100)

        self.assertIsNotNone(contest.exception)

    def test_IntegerListInsert_whenValueNotInteger_shouldRaiseValueError(self):
        """
            - test 'insert' if the element is not an integer, ValueError is thrown
        """
        values = [1, 3, 5, 7, 9]
        test_list = IntegerList(*values)

        with self.assertRaises(ValueError) as contest:
            test_list.insert(0, {})

        self.assertIsNotNone(contest.exception)

    def test_IntegerListGetBiggest_shouldReturnsBiggestElement(self):
        """
            - test 'get_biggest' should return the biggest el in collection
        """
        values = [1, 3, 5, 7, 9]
        test_list = IntegerList(*values)

        self.assertEqual(9, test_list.get_biggest())

    def test_IntegerListGetIndex_whenValueIsInteger_shouldReturnsTheIndex(self):
        """
            - test 'get_index' should returns the index of the given element
        """
        values = [1, 3, 5, 7, 9]
        test_list = IntegerList(*values)

        self.assertEqual(0, test_list.get_index(1))


if __name__ == '__main__':
    unittest.main()
