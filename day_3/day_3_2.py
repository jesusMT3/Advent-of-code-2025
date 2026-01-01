from itertools import combinations

import functools

@functools.cache
def func(val, digits):

    # Check if there's any digit to process
    if digits == 0:
        return 0

    # Check if we have to take all of the remaining digits
    if len(val) == digits:
        return int(val)

    # Take this digit
    # For the 12th digit, we need 10 ^ (12 - 1)
    a = (int(val[0]) * 10 ** (digits - 1)) + func(val[1:],
         digits-1)

    # Discard this digit
    b = func(val[1:], digits)

    # Return the greater value
    return max(a, b)

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
        max_joltage = func(sequence, 12)
        solution += max_joltage
    
    print(solution)
                