import unittest
from Helper.validations_funcs import input_non_empty


class TestingEmptyVal(unittest.TestCase):

    def test_first_name_empty(self):
        self.assertEqual(input_non_empty('', 'man', '3123'), {'message': 'Input must contain value'})

    def test_last_name_empty(self):
        self.assertEqual(input_non_empty('man', '', '3123'), {'message': 'Input must contain value'})

    def test_id_number_empty(self):
        self.assertEqual(input_non_empty('man', 'asd', ''), {'message': 'Input must contain value'})

    def test_none_empty(self):
        self.assertIsNone(input_non_empty('man', 'asd', '12323'))

    def test_first_last_empty(self):
        self.assertEqual(input_non_empty('', '', '12323'), {'message': 'Input must contain value'})

    def test_first_id_empty(self):
        self.assertEqual(input_non_empty('', 'mna', ''), {'message': 'Input must contain value'})

    def test_last_id_empty(self):
        self.assertEqual(input_non_empty('kobi', '', ''), {'message': 'Input must contain value'})

    def test_first_last_id_empty(self):
        self.assertEqual(input_non_empty('', '', ''), {'message': 'Input must contain value'})


# running the tests
if __name__ == '__main__':
    unittest.main()
