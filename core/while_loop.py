import re

from core.operation import Operation
from core.size import OperationSize


class WhileLoop(Operation):
    def __init__(self, condition, size, operations=[], parent=None):
        super().__init__(size, operations, parent)
        self.condition = condition
        self.operations = operations
        self.parent = parent

    @staticmethod
    def create_from_line(line, parent, line_index):
        patterns_to_remove = r"[\s]|while|\..."
        cleaned_line = re.sub(patterns_to_remove, "", line)
        return WhileLoop(cleaned_line, OperationSize())
