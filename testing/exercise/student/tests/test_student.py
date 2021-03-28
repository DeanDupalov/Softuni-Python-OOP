import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student('test_name')


    def test_initialize_student(self):
        student = Student('TestStudent')
        self.assertEqual(student.name, 'TestStudent')
        self.assertEqual(student.courses, {})


    def test_enroll__course_not_in_student_courses__should_add_it_and_return_message(self):
        actual = self.student.enroll('OOP', 'test_notes', 'No')
        expected = "Course has been added."

        self.assertEqual(expected, actual)

    def test_enroll__course_not_in_student_courses_and_want_to_add_notes__should_return_message(self):
        actual = self.student.enroll('OOP', 'test_notes', 'Y')
        expected = "Course and course notes have been added."
        actual_notes = self.student.courses['OOP'] 
        expected_notes = 'test_notes'

        self.assertEqual(expected, actual)
        self.assertEqual(expected_notes, actual_notes)

    def test_enroll__course_not_in_student_courses_and_want_to_add_notes_with_empty_string__should_return_message(self):
        actual = self.student.enroll('OOP', 'test_notes', )
        expected = "Course and course notes have been added."
        actual_notes = self.student.courses['OOP']
        expected_notes = 'test_notes'

        self.assertEqual(expected, actual)
        self.assertEqual(expected_notes, actual_notes)

    def test_enroll__course_in_student_courses__should_return_message(self):
        self.student.enroll('Python OOP', ['inheritance', 'Polymorphism'], 'N')

        actual = self.student.enroll('Python OOP', ['inheritance', 'Polymorphism'], 'Y')
        expected = "Course already added. Notes have been updated."

        self.assertEqual(actual, expected)
        self.assertEqual(2, len(self.student.courses['Python OOP']))

    def test_add_notes__when_course_is_found(self):
        self.student.enroll('Python OOP', ['inheritance', 'Polymorphism'], 'Y')
        actual = self.student.add_notes('Python OOP', 'SOLID')
        expected = "Notes have been updated"

        self.assertEqual(expected, actual)
        self.assertEqual(3, len(self.student.courses['Python OOP']))

    def test_add_notes__when_course_is_not_found__should_raise(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('Java', 'SOLID')

        expected = "Cannot add notes. Course not found."

        self.assertEqual(expected, context.exception.args[0])

    def test_leave_course__when_course_is_found__should_remove_and_return_message(self):
        self.student.enroll('Python OOP', ['inheritance', 'Polymorphism'], 'Y')
        actual = self.student.leave_course('Python OOP')
        expected = "Course has been removed"

        self.assertEqual(expected, actual)

    def test_leave_course__when_course_is_not_found__should_raise(self):
        self.student.enroll('Python OOP', ['inheritance', 'Polymorphism'], 'Y')
        with self.assertRaises(Exception) as context:
            self.student.leave_course('Python')
        actual = context.exception.args[0]
        expected = "Cannot remove course. Course not found."

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
