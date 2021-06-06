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
    lines = string.split('\n')
    start_function = 0
    end_function = 0
    function_found = False
    index = 0
    for line in lines:
        patterns_to_remove = r"[\s]"
        cleaned_line = re.sub(patterns_to_remove, "", line)
        if is_line_function(line):
            start_function = index
            function_found = True
        if function_found:
            if "end" in cleaned_line or index == len(lines)-1:
                end_function = index
        if len(cleaned_line) > 0:
            index += 1
    return end_function - start_function + 1