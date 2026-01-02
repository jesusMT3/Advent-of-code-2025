import math

def parse_input(filename: str):
    output = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = list(line[:-1].replace(" ", "0"))
            output.append(line)
    output = list(map(list, zip(*output)))
    return output                   

def convert_to_number(digits: list):
    number = 0
    i = 0
    for digit in reversed(digits):
        if digit != "0":
            number += int(digit) * 10 ** i
            i += 1
    return number


if __name__ == "__main__":
    input = parse_input("day_6/input_6.txt")
    solution = 0
    operation_array = []
    current_character = ""
    for line in input:
        number = convert_to_number(line[:-1])
        character = line[-1]
        if number == 0:
            pass
        else:
            if character == "0":
                operation_array.append(number)
            else:
                if current_character == "":
                    current_character = character
                    operation_array.append(number)
                elif current_character == "+":
                    solution += sum(operation_array)
                    operation_array.clear()
                    operation_array.append(number)
                    current_character = character
                elif current_character == "*":
                    solution += math.prod(operation_array)
                    operation_array.clear()
                    operation_array.append(number)
                    current_character = character
    if current_character == "+":
        solution += sum(operation_array)
        operation_array.clear()
        operation_array.append(number)
        current_character = character
    elif current_character == "*":
        solution += math.prod(operation_array)
        operation_array.clear()
        operation_array.append(number)
        current_character = character
    print(solution)