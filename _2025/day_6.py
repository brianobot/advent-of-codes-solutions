import operator
from functools import reduce


OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow,
}

def solve_equation(data_columns: list[tuple[str]]) -> int:
    total = 0
    for col in data_columns:
        op = col[-1]
        ops = OPS[op]
        total += reduce(ops,
            list(map(int, col[:-1])))
        
    return total


    
    
def solve_equation_v2(data_columns: list[tuple[str]]) -> int:
    total = 0
    
    for col in data_columns:
        op = col[-1]
        ops = OPS[op]
        lens  = [len(item) for item in col[:-1]]
        padded_item = [item.ljust(max(lens) , "0") for length, item in zip(lens, col[:-1])]
        
        numbers = []
        for n in range(max(lens), 0, -1):
            nth_numbers = [item[n - 1] for item in padded_item]
            nth_numbers = [item for item in nth_numbers if item != "0"]
    
            parsed_number = int("".join(nth_numbers))
            numbers.append(parsed_number)
            
        print("Numbers: ", numbers)
        sum =  reduce(ops, numbers)
        print("Sum: ", sum)
        total += sum
        
    return total



if __name__ == "__main__":
    data = [line.rstrip().split() for line in open("_2025/data/day_6_input.txt").readlines()]
    columns = list(zip(*data))[::-1]
    
    print(f"Data = {columns}")
    # total = solve_equation_v2(columns)
    # print(f"Total = {total}")