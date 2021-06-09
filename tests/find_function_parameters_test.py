import unittest

import core.core


class FindFunctionParametersTest(unittest.TestCase):


    def test_number_of_lines_for_function(self):
        with open("tests/resources/simple_empty_function.m", "r") as file:
            function_params = core.core.find_number_of_lines_for_operation(file.read().split('\n'))
            self.assertEqual("function", function_params["type"], 'Types are not equal')
            self.assertEqual(0, function_params["start"], 'Start indexes are not equal')
            self.assertEqual(2, function_params["end"], 'End indexes are not equal')
            self.assertEqual(3, function_params["length"], 'Length are not equal')
            self.assertEqual(0, len(function_params["operations"]), 'Number of operations found are not equal')
            self.assertEqual(2, function_params["functional_length"], 'Functional length are not equal')

    def test_number_of_lines_for_square_function(self):
        with open("tests/resources/simple_square_function.m", "r") as file:
            function_params = core.core.find_number_of_lines_for_operation(file.read().split('\n'))
            self.assertEqual("function", function_params["type"], 'Types are not equal')
            self.assertEqual(0, function_params["start"], 'Start indexes are not equal')
            self.assertEqual(2, function_params["end"], 'End indexes are not equal')
            self.assertEqual(3, function_params["length"], 'Length are not equal')
            self.assertEqual(0, len(function_params["operations"]), 'Number of operations found are not equal')
            self.assertEqual(3, function_params["functional_length"], 'Functional length are not equal')

    def test_number_of_lines_for_function_without_end(self):
        with open("tests/resources/simple_function_without_end.m", "r") as file:
            function_params = core.core.find_number_of_lines_for_operation(file.read().split('\n'))
            self.assertEqual("function", function_params["type"], 'Types are not equal')
            self.assertEqual(0, function_params["start"], 'Start indexes are not equal')
            self.assertEqual(1, function_params["end"], 'End indexes are not equal')
            self.assertEqual(2, function_params["length"], 'Length are not equal')
            self.assertEqual(0, len(function_params["operations"]), 'Number of operations found are not equal')
            self.assertEqual(2, function_params["functional_length"], 'Functional length are not equal')

    def test_number_of_lines_for_nested_functions(self):
        with open("tests/resources/nested_functions.m", "r") as file:
            function_params = core.core.find_number_of_lines_for_operation(file.read().split('\n'))
            self.assertEqual("function", function_params["type"], 'Types are not equal')
            self.assertEqual(0, function_params["start"], 'Start indexes are not equal')
            self.assertEqual(10, function_params["end"], 'End indexes are not equal')
            self.assertEqual(11, function_params["length"], 'Length are not equal')
            self.assertEqual(2, len(function_params["operations"]), 'Number of operations found are not equal')
            self.assertEqual(9, function_params["functional_length"], 'Functional length are not equal')


if __name__ == '__main__':
    unittest.main()
