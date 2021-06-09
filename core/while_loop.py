import re

from core.operation import Operation
from core.operation_size import OperationSize


class WhileLoop(Operation):
    def __init__(self, condition, size, parent=None):
        super().__init__(size, parent)
        self.condition = condition

    @staticmethod
    def create_from_line(line, parent, line_index):
        patterns_to_remove = r"[\s]|while|\..."
        cleaned_line = re.sub(patterns_to_remove, "", line)
        return WhileLoop(cleaned_line, OperationSize())
