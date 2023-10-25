"""
    Unit tests for employee.py
"""

import unittest
from unittest.mock import patch  # for mockinh
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('in setUpClass ...\n')

    @classmethod
    def tearDownClass(cls):
        print('in tearDownClass ...')

    def setUp(self):
        """ Code that runs before every single test """
        print('in setUp() ...')
        self.emp_1 = Employee("John", "Smith", 100000)
        self.emp_2 = Employee("Jack", "Jones", 120000)

    def tearDown(self):
        """ code that runs after every single test """
        print('in tearDown() ...\n')

    def test_email(self):
        print('in test_email() ...')
        self.assertEqual(self.emp_1.email, "John.Smith@email.com")
        self.assertEqual(self.emp_2.email, "Jack.Jones@email.com")

        self.emp_1.first = "Bill"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "Bill.Smith@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Jones@email.com")

    def test_fullname(self):
        print('in test_fullname() ...')
        self.assertEqual(self.emp_1.fullname, "John Smith")
        self.assertEqual(self.emp_2.fullname, "Jack Jones")

        self.emp_1.first = "Bill"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "Bill Smith")
        self.assertEqual(self.emp_2.fullname, "Jane Jones")

    def test_apply_raise(self):
        print('in test_apply_raise() ...')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 105000)
        self.assertEqual(self.emp_2.pay, 126000)

    def test_monthly_schedule(self):
        print('in test_monthly_schedule() ...')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Smith/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Jones/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()