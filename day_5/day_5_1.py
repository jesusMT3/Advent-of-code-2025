def is_inside(id: int, interval: tuple):
    lower, upper = interval
    return lower <= id <= upper

if __name__ == "__main__":
    solution = 0
    id_ranges = []
    ids = []
    with open("day_5/input_5.txt", "r") as f:
        for line in f.readlines():
            if "-" in line:
                id_range = tuple([int(i) for i in line.strip().split("-")])
                id_ranges.append(id_range)
            else:
                if line == "\n":
                    pass
                else:
                    ids.append(int(line.strip()))
    
    for id in ids:
        for id_range in id_ranges:
            if is_inside(id, id_range):
                solution += 1
                break
            
    print(solution)