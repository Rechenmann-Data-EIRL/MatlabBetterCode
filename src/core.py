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