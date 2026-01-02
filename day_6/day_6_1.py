import math

def parse_into_columns(filename: str)-> list[list[int]]:
    # get each row
    with open(filename, "r") as f:
        output = []
        for line in f.readlines():
           output.append(line.strip().split())
    
    # transpose list
    output = list(map(list, zip(*output)))
    return output
    
if __name__ == "__main__":
    solution = 0
    input = parse_into_columns("day_6/input_6.txt")
    for line in input:
        numbers = [int(i) for i in line[:-1]]
        symbol = line[-1]
        if symbol == "+":
            solution += sum(numbers)
        elif symbol == "*":
            solution += math.prod(numbers)
            
    print(solution)