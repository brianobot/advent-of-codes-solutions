from icecream import ic


def get_neighbors(grid: list[list[str]], point: tuple[int, int]) -> list[str]:
    neighbors = []
    
    col_len = len(grid[0])
    row_len = len(grid)
    
    x_pos, y_pos = point
    
    offsets = [
        (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
    ]
    
    for dr, dc in offsets:
        new_row, new_col = x_pos + dr, y_pos + dc
        
        if 0 <= new_row < row_len and 0 <= new_col < col_len:
            neighbors.append(grid[new_row][new_col])
    
    return neighbors
    
    
def get_total_neighbors(grid: list[list[str]], point: tuple[int, int]) -> int:
    return get_neighbors(grid, point).count("@")
    

def calculate_total_accessible_paper_roll(grid: list[list[str]]) -> tuple[int, list[list[str]]]:
    """
    This returns the total accessible paper rolls and a copy of the original grid with the accessible ones removed
    """
    original_grid_copy  = [row.copy() for row in grid]
    total_accessible_paper_roll = 0

    
    for row_index, row in enumerate(grid):
        for column_index, value in enumerate(row):
            # we only care for a spot if there is a paper roll on it
            if value == "x":
                original_grid_copy[row_index][column_index] = "."
            if value == "@":
                point = (row_index, column_index)
                if get_total_neighbors(grid, point) < 4:
                    total_accessible_paper_roll += 1
                    original_grid_copy[row_index][column_index] = "x"
            
            
    return (total_accessible_paper_roll, original_grid_copy)
    
    
    
def main(grid: list[list[str]]):
    total_accessible_paper_roll = 0
    found_accessible_paper_roll = True
    while found_accessible_paper_roll:
        total, new_gid = calculate_total_accessible_paper_roll(grid)
        total_accessible_paper_roll += total
        grid = new_gid

        if not total:
            found_accessible_paper_roll = False
        
    return total_accessible_paper_roll
    

def read_input_data() -> list[list[str]]:
    rows = [row.strip() for row in open("_2025/data/day_4_input.txt").readlines()]
    return [list(row) for row in rows]
    


if __name__ == "__main__":
    grid = read_input_data()
    ic(grid)
    
    # total = calculate_total_accessible_paper_roll(grid)
    total = main(grid)
    print(f"{total = }")