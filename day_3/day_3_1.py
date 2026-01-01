from itertools import combinations

if __name__ == "__main__":
    # parse data
    solution = 0
    example_input = ['987654321111111', '811111111111119', 
                        '234234234234278', '818181911112111']
    input = []
    with open("day_3/input_3.txt", "r") as f:
        for line in f.readlines():
            input.append(line[:-1])
    
    for sequence in input:
        # get every combination of 12 batteries
        all_combinations = list(set(combinations(sequence, 2)))
        check_array = []
        for combination in all_combinations:
            string = ""
            for character in combination:
                string += character
            check_array.append(int(string))
    
        solution += max(check_array)
    print(solution)
                