from day_4_1 import get_adjacent_positions ,count_rolls, parse_file

if __name__ == "__main__":
    solution = 0
    input = parse_file("day_4/input_4.txt")
    while True:
        extracted_rolls = 0
        for i in range(len(input)):
            for j in range(len(input[0])):
                if input[i][j] == "@":
                    count = count_rolls(get_adjacent_positions(input, i, j))
                    if count < 4:
                        extracted_rolls += 1
                        input[i][j] = "."
        if extracted_rolls == 0:
            print("solution: ", solution)
            exit()
        else:
            solution += extracted_rolls
    
    