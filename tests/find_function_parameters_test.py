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

if __name__ == '__main__':
    unittest.main()
