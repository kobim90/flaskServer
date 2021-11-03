import unittest
from Helper.validations_funcs import input_string_check


class TestingStringCheck(unittest.TestCase):

    def test_valid_input(self):
        self.assertIsNone(input_string_check("asda", 'man', "1213"))

    def test_first_name_not_str(self):
        self.assertEqual(input_string_check(12, 'man', '3123'), {'message': 'all values must be of String type'})

    def test_last_name_not_str(self):
        self.assertEqual(input_string_check("asd", 13, '3123'), {'message': 'all values must be of String type'})

    def test_id_number_not_str(self):
        self.assertEqual(input_string_check("asda", 'man', 1213), {'message': 'all values must be of String type'})

    def test_first_name_not_letter(self):
        self.assertEqual(input_string_check("123", 'man', "1213"),
                         {'message': 'first/last name must be characters only'})

    def test_last_name_not_letter(self):
        self.assertEqual(input_string_check("kobi", '1243', "1213"), {'message': 'first/last name must be characters '
                                                                                 'only'})

    def test_id_number_not_digits(self):
        self.assertEqual(input_string_check("asda", 'man', "sd124"), {'message': 'Id number must be numbers only'})

    def test_first_name_long_length(self):
        self.assertEqual(input_string_check("asqwzxqwaszxqwaszxqwa", 'man', "1243124"), {'message': 'first/last name '
                                                                                                    'must be below 20 '
                                                                                                    'characters'})

    def test_last_name_long_length(self):
        self.assertEqual(input_string_check("aas", 'asqwzxqwaszxqwaszxqwa', "1243124"), {'message': 'first/last name '
                                                                                                    'must be below 20 '
                                                                                                    'characters'})

    def test_id_number_invalid_length(self):
        self.assertEqual(input_string_check("aas", 'asqwz', "124312412948"), {'message': 'Id number must be 9 '
                                                                                         'characters or below'})

    def test_first_name_short_length(self):
        self.assertEqual(input_string_check("a", 'man', "1243124"), {'message': 'first/last name must be at least 2 '
                                                                                'characters'})

    def test_last_name_short_length(self):
        self.assertEqual(input_string_check("aas", 'a', "1243124"), {'message': 'first/last name must be at least 2 '
                                                                                'characters'})


# running the tests
if __name__ == '__main__':
    unittest.main()
