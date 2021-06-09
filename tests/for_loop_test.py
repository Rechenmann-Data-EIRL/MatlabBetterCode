import unittest
import core.for_loop
from core.size import OperationSize


class ForLoopTestCase(unittest.TestCase):
    def test_creation(self):
        size = OperationSize(start=0, end=15, length=14, functional_length=7)
        loop = core.for_loop.ForLoop(index_name="index", values="1:max_size", size=size, parent=None)
        self.assertEqual("index", loop.index_name)
        self.assertEqual("1:max_size", loop.values)
        self.assertEqual(size, loop.size)
        self.assertEqual(None, loop.parent)

    def test_creation_from_line(self):
        line = "for index = 1:size"
        loop = core.for_loop.ForLoop.create_from_line(line, parent=None, line_index=0)
        self.assertEqual("index", loop.index_name)
        self.assertEqual("1:size", loop.values)
        self.assertEqual(None, loop.parent)


if __name__ == '__main__':
    unittest.main()
