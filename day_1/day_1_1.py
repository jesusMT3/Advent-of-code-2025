class Rotation():
    def __init__(self, number: int):
        self.value = number
        self.zeros = 0
        
    def get_value(self):
        return self.value
    
    def get_zeros(self):
        return self.zeros
    
    def __add__(self, other):
        if isinstance(other, str):
            # identify sign and amount 
            sign = other[0]
            amount = int(other[1:])
            
            # add correct amount 
            if sign == "L":
                self.value -= amount
            elif sign == "R":
                self.value += amount
            
            # return if < 0 or > 99
            while self.value < 0:
                self.value += 100
            while self.value > 99:
                self.value -= 100
            
            # add zeros if rotation ends up in zero    
            if self.value == 0:
                self.zeros += 1

        return self
            
            
    
if __name__ == "__main__":
    my_rotation = Rotation(50)
    example_sequence = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    sequence = []
    with open("day_1/input_1.txt", "r") as f:
        for line in f.readlines():
            sequence.append(line[:-1])
    
    for rotation in sequence:
        my_rotation += rotation
            
    print(f"Number of zeros = {my_rotation.get_zeros()}")