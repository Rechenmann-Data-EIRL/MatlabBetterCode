from abc import ABC, abstractmethod


class Operation(ABC):
    def __init__(self, size, operations=[], parent=None):
        self.size = size
        self.parent = parent
        self.operations = operations

    @staticmethod
    @abstractmethod
    def create_from_line(line, parent, line_index):
        pass

    def add_operation(self, operation):
        self.operations.append(operation)
        self.size.end += operation.size.length
        self.size.length += operation.size.length
        self.size.functional_length += operation.size.functional_length