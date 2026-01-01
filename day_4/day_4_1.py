def get_adjacent_positions(matrix, row, column):
    adjacent_positions = []
    # go through rows and columns
    for i in range(row-1, row+2):
        for j in range(column-1, column+2):
            # check if coordinates are outside of bounds
            if 0 <= i < len(matrix) and 0 <= j < len(matrix):
                adjacent_positions.append(matrix[i][j])
            # pop element which is the selected one
            if i == row and j == column:
                adjacent_positions.pop(-1)
    return adjacent_positions

def count_rolls(adjacent_positions):
    n_rolls = 0
    for position in adjacent_positions:
        if position == "@":
            n_rolls += 1
    return n_rolls

def parse_file(filename: str):
    parsed_file = []
    with open(filename, "r") as f:
        for line in f.readlines():
            row = []
            for character in line.strip():
                row.append(character)
            parsed_file.append(row)
    return parsed_file

if __name__ == "__main__":
    # parse input from file into matrix
    solution = 0
    input = parse_file("day_4/input_4.txt")

    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "@":
                count = count_rolls(get_adjacent_positions(input, i, j))
                if count < 4:
                    solution += 1
                
    print(solution)
    
    