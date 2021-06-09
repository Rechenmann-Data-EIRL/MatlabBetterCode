import unittest
import core.function
from core.size import OperationSize


class FunctionTestCase(unittest.TestCase):
    def test_creation(self):
        size = OperationSize(start=0, end=15, length=14, functional_length=7)
        function = core.function.Function(size, name="functionName", arguments=["arg1", "arg2"], outputs=[],
                                          operations=[], parent=None)
        self.assertEqual("functionName", function.name)
        self.assertEqual(["arg1", "arg2"], function.arguments)
        self.assertEqual([], function.outputs)
        self.assertEqual(0, function.size.start)
        self.assertEqual(15, function.size.end)
        self.assertEqual(14, function.size.length)
        self.assertEqual(7, function.size.functional_length)
        self.assertEqual(0, len(function.operations))
        self.assertEqual(None, function.parent)

    def test_creation_from_line(self):
        line = "function ...\r\n\t[output1, ...\n\toutput2  ] = ...\n\ttestFunction  (argument1,...\n\targument2)"
        function = core.function.Function.create_from_line(line, parent=None, line_index=0)
        self.assertEqual("testFunction", function.name)
        self.assertEqual(["argument1", "argument2"], function.arguments)
        self.assertEqual(["output1", "output2"], function.outputs)
        self.assertEqual(0, function.size.start)
        self.assertEqual(0, function.size.end)
        self.assertEqual(1, function.size.length)
        self.assertEqual(1, function.size.functional_length)
        self.assertEqual(0, len(function.operations))
        self.assertEqual(None, function.parent)

    def test_add_operation(self):
        size1 = OperationSize(start=0, end=0, length=1, functional_length=1)
        size2 = OperationSize(start=1, end=14, length=14, functional_length=7)
        function = core.function.Function(size1, name="functionName", operations=[], parent=None)
        operation = core.function.Function(size2, name="nestedFunction", operations=[], parent=function)
        function.add_operation(operation)
        self.assertEqual("functionName", function.name)
        self.assertEqual(0, function.size.start)
        self.assertEqual(14, function.size.end)
        self.assertEqual(15, function.size.length)
        self.assertEqual(8, function.size.functional_length)
        self.assertEqual(1, len(function.operations))
        self.assertEqual(None, function.parent)
        self.assertEqual(function, operation.parent)

    def test_finding_function_parameters_no_arguments_no_output_no_space(self):
        parameters = core.function.find_function_parameters_from_line("function testFunction()")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(None, parameters["arguments"])
        self.assertEqual(None, parameters["outputs"])

    def test_finding_function_name_no_arguments_with_space(self):
        parameters = core.function.find_function_parameters_from_line("function  testFunction  ()")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(None, parameters["arguments"])
        self.assertEqual(None, parameters["outputs"])

    def test_finding_function_name_arguments_and_spaces(self):
        parameters = core.function.find_function_parameters_from_line("function  testFunction  (argument1, argument2)")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(['argument1', 'argument2'], parameters["arguments"])
        self.assertEqual(None, parameters["outputs"])

    def test_finding_function_arguments_with_arguments_and_spaces(self):
        parameters = core.function.find_function_parameters_from_line("function  testFunction  (argument1, argument2)")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(['argument1', 'argument2'], parameters["arguments"])
        self.assertEqual(None, parameters["outputs"])

    def test_finding_function_output_with_arguments_and_spaces(self):
        parameters = core.function.find_function_parameters_from_line(
            "function output1 = testFunction  (argument1, argument2)")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(["argument1", "argument2"], parameters["arguments"])
        self.assertEqual(["output1"], parameters["outputs"])

    def test_finding_function_multiple_outputs_with_arguments_and_spaces(self):
        string = "function [output1, output2  ] = testFunction  (argument1, argument2)"
        parameters = core.function.find_function_parameters_from_line(string)
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(["argument1", "argument2"], parameters["arguments"])
        self.assertEqual(["output1", "output2"], parameters["outputs"])

    def test_finding_function_multiple_outputs_with_arguments_and_spaces_and_jump_line(self):
        string = "function ...\r\n\t[output1, ...\n\toutput2  ] = ...\n\ttestFunction  (argument1,...\n\targument2)"
        parameters = core.function.find_function_parameters_from_line(string)
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(["argument1", "argument2"], parameters["arguments"])
        self.assertEqual(["output1", "output2"], parameters["outputs"])

    def test_if_line_is_function(self):
        string = "function [output1, output2  ] = testFunction  (argument1, argument2)"
        self.assertEqual(True, core.function.Function.is_line_function(string))

    def test_if_line_is_not_a_function(self):
        string = "[output1, output2  ] = testFunction  (argument1, argument2)"
        self.assertEqual(False, core.function.Function.is_line_function(string))


if __name__ == '__main__':
    unittest.main()
