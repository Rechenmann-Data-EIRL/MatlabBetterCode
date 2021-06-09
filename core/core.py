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


def is_line_condition(line):
    return "if" in line


def is_line_for_loop(line):
    return "for" in line


def is_line_while_loop(line):
    return "while" in line


def is_line_switch(line):
    return "switch" in line


def is_line_operation(line):
    return is_line_function(line) or is_line_condition(line) or is_line_for_loop(line) or is_line_while_loop(line) \
           or is_line_switch(line)


def get_operation_type(line):
    if "function" in line:
        return "function"
    elif "if" in line:
        return "if"
    elif "for" in line:
        return "for"
    elif "while" in line:
        return "while"
    elif "switch" in line:
        return "switch"


def find_number_of_lines_for_operation(lines):
    patterns_to_remove = r"[\s]"
    operation_params = None
    index = 0
    while index < len(lines):
        cleaned_line = re.sub(patterns_to_remove, "", lines[index])
        if is_line_operation(lines[index]) and operation_params is None:
            operation_params = {"start": index, "end": index, "length": 1, "functional_length": 1, "operations": [],
                                "type": get_operation_type(lines[index])}
        elif operation_params is not None and is_line_operation(lines[index]):
            operation_params["operations"].append(find_number_of_lines_for_operation(lines[index:-1]))
            operation_params["length"] += operation_params["operations"][-1]["length"]
            operation_params["functional_length"] += operation_params["operations"][-1]["functional_length"]
            operation_params["end"] += operation_params["operations"][-1]["length"]
            index += operation_params["operations"][-1]["length"] - 1
        elif operation_params is not None:
            operation_params["length"] += 1
            if len(cleaned_line) > 0:
                operation_params["functional_length"] += 1
            if "end" in cleaned_line or index == len(lines)-1:
                operation_params["end"] = index
                return operation_params
        index += 1
