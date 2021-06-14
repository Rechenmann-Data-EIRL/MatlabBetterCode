import unittest

from core.operation.for_loop import ForLoop
from core.operation.function import Function
from core.operation.operation_factory import OperationFactory
from core.operation.while_loop import WhileLoop


class OperationFactoryTestCase(unittest.TestCase):
    def test_for_loop_creation(self):
        line = "for index = 1:max_size"
        operation = OperationFactory.create(line, None, 2)
        self.assertIsInstance(operation, ForLoop, "given object is not instance of ForLoop")
        self.assertEqual(2, operation.size.start)

    def test_while_loop_creation(self):
        line = "while index > max_size"
        operation = OperationFactory.create(line, None, 2)
        self.assertIsInstance(operation, WhileLoop, "given object is not instance of WhileLoop")
        self.assertEqual(2, operation.size.start)

    def test_function_creation(self):
        line = "function a = testFunction(c,d)"
        operation = OperationFactory.create(line, None, 2)
        self.assertIsInstance(operation, Function, "given object is not instance of Function")
        self.assertEqual(2, operation.size.start)

    def test_none_creation(self):
        line = "a = c + d"
        operation = OperationFactory.create(line, None, 2)
        self.assertIsNone(operation)


if __name__ == '__main__':
    unittest.main()
