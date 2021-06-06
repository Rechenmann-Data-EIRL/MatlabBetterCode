import unittest

import core.core


class FindFunctionParametersTest(unittest.TestCase):
    def test_finding_function_parameters_no_arguments_no_output_no_space(self):
        parameters = core.core.find_function_parameters_from_line("function testFunction()")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(None, parameters["arguments"])
        self.assertEqual(None, parameters["outputs"])

    def test_finding_function_name_no_arguments_with_space(self):
        parameters = core.core.find_function_parameters_from_line("function  testFunction  ()")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(None, parameters["arguments"])
        self.assertEqual(None, parameters["outputs"])

    def test_finding_function_name_arguments_and_spaces(self):
        parameters = core.core.find_function_parameters_from_line("function  testFunction  (argument1, argument2)")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(['argument1', 'argument2'], parameters["arguments"])
        self.assertEqual(None, parameters["outputs"])

    def test_finding_function_arguments_with_arguments_and_spaces(self):
        parameters = core.core.find_function_parameters_from_line("function  testFunction  (argument1, argument2)")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(['argument1', 'argument2'], parameters["arguments"])
        self.assertEqual(None, parameters["outputs"])

    def test_finding_function_output_with_arguments_and_spaces(self):
        parameters = core.core.find_function_parameters_from_line("function output1 = testFunction  (argument1, argument2)")
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(["argument1", "argument2"], parameters["arguments"])
        self.assertEqual(["output1"], parameters["outputs"])

    def test_finding_function_multiple_outputs_with_arguments_and_spaces(self):
        string = "function [output1, output2  ] = testFunction  (argument1, argument2)"
        parameters = core.core.find_function_parameters_from_line(string)
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(["argument1", "argument2"], parameters["arguments"])
        self.assertEqual(["output1", "output2"], parameters["outputs"])

    def test_finding_function_multiple_outputs_with_arguments_and_spaces_and_jump_line(self):
        string = "function ...\r\n\t[output1, ...\n\toutput2  ] = ...\n\ttestFunction  (argument1,...\n\targument2)"
        parameters = core.core.find_function_parameters_from_line(string)
        self.assertEqual("testFunction", parameters["name"])
        self.assertEqual(["argument1", "argument2"], parameters["arguments"])
        self.assertEqual(["output1", "output2"], parameters["outputs"])

    def test_if_line_is_function(self):
        string = "function [output1, output2  ] = testFunction  (argument1, argument2)"
        self.assertEqual(True, core.core.is_line_function(string))

    def test_if_line_is_not_a_function(self):
        string = "[output1, output2  ] = testFunction  (argument1, argument2)"
        self.assertEqual(False, core.core.is_line_function(string))

    def test_number_of_lines_for_function(self):
        with open("tests/resources/simple_empty_function.m", "r") as file:
            nb_lines = core.core.find_number_of_lines_for_function(file.read())
            self.assertEqual(2, nb_lines)

    def test_number_of_lines_for_square_function(self):
        with open("tests/resources/simple_square_function.m", "r") as file:
            nb_lines = core.core.find_number_of_lines_for_function(file.read())
            self.assertEqual(3, nb_lines)

    def test_number_of_lines_for_function_without_end(self):
        with open("tests/resources/simple_function_without_end.m", "r") as file:
            nb_lines = core.core.find_number_of_lines_for_function(file.read())
            self.assertEqual(2, nb_lines)


if __name__ == '__main__':
    unittest.main()
