use std::fs;


fn get_neighbors(grid: Vec<Vec<char>>, (x_pos, y_pos): (i32, i32)) -> Vec<char> {
    let mut neighbors = Vec::with_capacity(8);
    
    let col_len = grid[0].len();
    let row_len = grid.len();
    
    let offsets = [
        (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
    ];
    
    for (dr, dc) in offsets {
        let (new_row, new_col) = (x_pos + dr, y_pos + dc);
       
       if (0 <= new_row && new_row < row_len) && (0 <= new_col && new_col < col_len) {
           neighbors.push(grid[new_row as usize][new_col as usize]);
       } 
    }
    
    neighbors
}

fn main() {
    let binding = fs::read_to_string("2025/data/day_4_input.txt").expect("Could not read the input file");
    let lines = binding.lines();
    let lines = lines.map(|line| line.to_owned()).collect::<Vec<String>>();
    let grid = lines.iter().map(|row| row.chars().collect::<Vec<char>>()).collect::<Vec<Vec<char>>>();
    
    dbg!(&grid);
    
    let neighbors = get_neighbors(grid, (0, 0));
    println!("Neighbors: {:?}", neighbors);
}