
import re

def is_valid_instruction(part: str, pattern: str = r'^mul\(\s*-?\d+\s*,\s*-?\d+\s*\)$') -> bool | None:
    """
    False means the instruction contains invalid parts
    True means the instruction is a complete valid set
    None means the instruction is valid but not yet complete
    """
    
    if bool(re.match(pattern, part)):
        return True
        
    if not "mul(".startswith(part) and len(part) <= 4:
        return False
        
    if part.count("(") > 1 or part.count(")") > 1:
        return False
    
    return None
    

def get_instruction_predicate(part, do_instruction: bool) -> bool:
    if part.endswith("do()"):
        return True
    elif part.endswith("don't()"):
        return False
    return do_instruction


def extract_instructions(data: str) -> list[str]:
    instructions = []
    do_instruction = True
    instruction_parts = ""
    current_instruction = ""
    
    for char in data:       
        if char in {"m", "u", "l", "(", ")", ",", "-"} or char.isdigit():
            current_instruction += char
        else:
            current_instruction = ""
        
        instruction_parts += char
        # print(f"{instruction_parts = }")
        
        do_instruction = get_instruction_predicate(instruction_parts, do_instruction)
        # print(f"{do_instruction = }")
        
        valid_instruction = is_valid_instruction(current_instruction)
        match valid_instruction:
            case True:
                if do_instruction:
                    instructions.append(current_instruction)
                current_instruction = ""
            case False:
                current_instruction = ""
            case None:
                continue
            
    return instructions


def get_total(instructions: list[str]) -> int:
    total = 0
    for instruction in instructions:
        a, b = tuple(map(int, instruction[4:-1].split(",")))
        total += (a * b)
    
    return total


if __name__ == "__main__":
    data = open("_2024/data/day_3_input.txt").read()
    
    # print("Data = ", data) 
    
    instructions = extract_instructions(data)
    print(f"Valid Instruction Count = {len(instructions)}")
    
    total = get_total(instructions)
    print("Total = ", total)