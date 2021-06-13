from core.for_loop import ForLoop
from core.function import Function
from core.while_loop import WhileLoop


class OperationFactory:
    @staticmethod
    def create(line, parent, line_index):
        if ForLoop.is_line_for_loop(line):
            return ForLoop.create_from_line(line, parent, line_index)
        elif WhileLoop.is_line_while_loop(line):
            return WhileLoop.create_from_line(line, parent, line_index)
        elif Function.is_line_function(line):
            return Function.create_from_line(line, parent, line_index)

    @staticmethod
    def is_line_operation(line):
        return ForLoop.is_line_for_loop(line) or WhileLoop.is_line_while_loop(line) or Function.is_line_function(line)
