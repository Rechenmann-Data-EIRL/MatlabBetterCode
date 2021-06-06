import re


def find_function_parameters_from_line(line):
    patterns_to_remove = r"[\s\[\]\)]|function|\..."
    cleaned_line = re.sub(patterns_to_remove, "", line)
    split_line = cleaned_line.split("(")
    name = split_line[0]
    argument_string = split_line[1]
    arguments = argument_string.split(",") if len(argument_string) > 0 else None
    outputs = None
    if '=' in split_line[0]:
        output_string = split_line[0].split("=")
        outputs = output_string[0].split(',')
        name = output_string[1]
    return {"name": name, "arguments": arguments, "outputs": outputs}


def is_line_function(line):
    return "function" in line


def find_number_of_lines_for_function(string):
    patterns_to_remove = r"[\s]"
    lines = string.split('\n')
    current_function_params = None
    for index in range(len(lines)):
        cleaned_line = re.sub(patterns_to_remove, "", lines[index])
        if is_line_function(lines[index]):
            current_function_params = {"start": index, "end": 0, "length": 0, "functional_length": 0}
        if current_function_params is not None:
            current_function_params["length"] += 1
            if len(cleaned_line) > 0:
                current_function_params["functional_length"] += 1
            if "end" in cleaned_line or index == len(lines)-1:
                current_function_params["end"] = index
                return current_function_params

