def get_dial_current_position(turn: str, start: int = 0, _cycle: int = 100) -> tuple[int, int]:
    """
    This performs modular arithmetic and returns a tuple with the first element being the 
    current dial after performing the turns the second element is the number of times
    the dial crossed 0
    """
    if _cycle == 0:
        raise ValueError("The Cycle can not be Zero")
        
    turn_steps = int(turn[1:].strip())
    direction = -1 if turn.startswith("L") else 1
    new_position = (start + (direction * turn_steps)) % _cycle
    
    crossings = 0
    for i in range(turn_steps):
        current_value = (start + (direction * i)) % _cycle
        if current_value == 0 and (i != 0 or i > (turn_steps - 1)):
            crossings += 1
        
    return (new_position, crossings)
    
    
def get_total_zero_hit(seq: list[str], start: int = 0, _cycle: int = 100) -> int:
    total_zero_hit = 0
    for turn in seq:
        current_dial, zero_count = get_dial_current_position(turn, start, _cycle)
        start = current_dial
        
        if current_dial == 0:
            total_zero_hit += 1
            
        total_zero_hit += zero_count
        
    return total_zero_hit


def test_get_dial_current_position():
    assert get_total_zero_hit(["R4", "L2"], 0, 2) == 3
    


if __name__ == "__main__":
    seq = open("2025/data/day_1_input.txt").readlines()
    seq = [turn.strip() for turn in seq]
    result = get_total_zero_hit(seq, 50)
    print(f"Total Zero Hit: {result}")
    
