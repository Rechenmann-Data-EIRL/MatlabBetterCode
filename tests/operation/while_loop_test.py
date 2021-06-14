import unittest

from core.operation.while_loop import WhileLoop
from core.operation.operation_size import OperationSize


class WhileLoopTestCase(unittest.TestCase):
    def test_creation(self):
        size = OperationSize(start=0, end=15, functional_length=7)
        loop = WhileLoop(condition="a == b", size=size, parent=None)
        self.assertEqual("a == b", loop.condition)
        self.assertEqual(size, loop.size)
        self.assertEqual(None, loop.parent)

    def test_creation_from_line(self):
        line = "while (index < size)"
        loop = WhileLoop.create_from_line(line, parent=None, line_index=0)
        self.assertEqual("(index<size)", loop.condition)
        self.assertEqual(0, len(loop.operations))
        self.assertEqual(None, loop.parent)


if __name__ == '__main__':
    unittest.main()
