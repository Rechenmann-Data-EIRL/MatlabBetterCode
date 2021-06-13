import re
from abc import ABC, abstractmethod


class Operation(ABC):
    def __init__(self, size, parent=None):
        self.size = size
        self.parent = parent
        self.operations = []

    @staticmethod
    @abstractmethod
    def create_from_line(line, parent, line_index):
        pass

    @staticmethod
    def create_from_lines(lines, parent, line_index, operation_factory):
        patterns_to_remove = r"[\s]"
        index = 0
        operation = None
        while index < len(lines):
            cleaned_line = re.sub(patterns_to_remove, "", lines[index])
            is_line_operation = operation_factory.is_line_operation(cleaned_line)
            if is_line_operation and operation is None:
                operation = operation_factory.create(cleaned_line, parent, line_index)
            elif operation is not None and is_line_operation:
                operation.add_operation(operation.create_from_lines(lines[index:-1], operation, index + line_index, operation_factory))
                index += operation.operations[-1].size.length - 1
            elif operation is not None:
                operation.size.length += 1
                if len(cleaned_line) > 0:
                    operation.size.functional_length += 1
                if "end" in cleaned_line or index == len(lines) - 1:
                    operation.size.end = index
                    return operation
            index += 1

    def add_operation(self, operation):
        self.operations.append(operation)
        self.size.end += operation.size.length
        self.size.length += operation.size.length
        self.size.functional_length += operation.size.functional_length
