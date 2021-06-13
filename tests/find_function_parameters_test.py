import unittest

from core.operation import Operation
from core.operation_factory import OperationFactory


class FindFileOperationsTestCase(unittest.TestCase):

    def test_number_of_lines_for_function(self):
        with open("tests/resources/simple_empty_function.m", "r") as file:
            operations = Operation.create_from_lines(file.read().split('\n'), None, 0, OperationFactory)
            self.assertEqual(0, operations.size.start, 'Start indexes are not equal')
            self.assertEqual(2, operations.size.end, 'End indexes are not equal')
            self.assertEqual(3, operations.size.length, 'Length are not equal')
            self.assertEqual(2, operations.size.functional_length, 'Functional length are not equal')
            self.assertEqual(0, len(operations.operations), 'Number of operations found are not equal')

    def test_number_of_lines_for_square_function(self):
        with open("tests/resources/simple_square_function.m", "r") as file:
            operations = Operation.create_from_lines(file.read().split('\n'), None, 0, OperationFactory)
            self.assertEqual(0, operations.size.start, 'Start indexes are not equal')
            self.assertEqual(2, operations.size.end, 'End indexes are not equal')
            self.assertEqual(3, operations.size.length, 'Length are not equal')
            self.assertEqual(3, operations.size.functional_length, 'Functional length are not equal')
            self.assertEqual(0, len(operations.operations), 'Number of operations found are not equal')

    def test_number_of_lines_for_function_without_end(self):
        with open("tests/resources/simple_function_without_end.m", "r") as file:
            operations = Operation.create_from_lines(file.read().split('\n'), None, 0, OperationFactory)
            self.assertEqual(0, operations.size.start, 'Start indexes are not equal')
            self.assertEqual(1, operations.size.end, 'End indexes are not equal')
            self.assertEqual(2, operations.size.length, 'Length are not equal')
            self.assertEqual(2, operations.size.functional_length, 'Functional length are not equal')
            self.assertEqual(0, len(operations.operations), 'Number of operations found are not equal')

    def test_number_of_lines_for_nested_functions(self):
        with open("tests/resources/nested_functions.m", "r") as file:
            operations = Operation.create_from_lines(file.read().split('\n'), None, 0, OperationFactory)
            self.assertEqual(0, operations.size.start, 'Start indexes are not equal')
            self.assertEqual(10, operations.size.end, 'End indexes are not equal')
            self.assertEqual(11, operations.size.length, 'Length are not equal')
            self.assertEqual(9, operations.size.functional_length, 'Functional length are not equal')
            self.assertEqual(2, len(operations.operations), 'Number of operations found are not equal')


if __name__ == '__main__':
    unittest.main()
