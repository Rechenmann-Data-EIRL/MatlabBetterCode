import re

from core.operation import Operation
from core.size import OperationSize


class ForLoop(Operation):
    def __init__(self, index_name, values, size, parent=None):
        super().__init__(size, parent)
        self.index_name = index_name
        self.values = values

    @staticmethod
    def create_from_line(line, parent, line_index):
        patterns_to_remove = r"[\s\[\]\)]|for|\..."
        cleaned_line = re.sub(patterns_to_remove, "", line)
        split_line = cleaned_line.split("=")
        return ForLoop(split_line[0], split_line[1], OperationSize())
