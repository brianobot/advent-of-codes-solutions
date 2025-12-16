use std::fs;


fn get_neighbors(grid: Vec<Vec<char>>, (x_pos, y_pos): (i32, i32)) -> Vec<char> {
    let mut neighbors = Vec::with_capacity(8);
    
    let col_len = grid[0].len() as usize;
    let row_len = grid.len() as usize;
    
    let offsets = [
        (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
    ];
    
    for (dr, dc) in offsets {
        let (new_row, new_col) = (x_pos + dr, y_pos + dc);
       
       if (0 <= (new_row as i32) && (new_row as i32) < (row_len as i32)) && (0 <= (new_col as i32) && (new_col as i32) < (col_len as i32)) {
           neighbors.push(grid[new_row as usize][new_col as usize]);
       } 
    }
    
    neighbors
}

fn get_total_neighbors(grid: Vec<Vec<char>>, point: (i32, i32)) -> i32 {
    get_neighbors(grid, point).iter().filter(|&x| *x == '@').count() as i32
}


fn calculate_total_accessible_paper_roll(grid: Vec<Vec<char>>) -> (i32, Vec<Vec<char>>) {
    let mut original_grid_copy = grid.clone();
    let mut total_accessible_paper_roll = 0;
    
    for (row_index, row) in grid.iter().enumerate() {
        for (column_index, value) in row.iter().enumerate() {
            if *value == '@' {
                let point = (row_index as i32, column_index as i32);
                if get_total_neighbors(grid.clone(), point) < 4 {
                    total_accessible_paper_roll += 1;
                    original_grid_copy[row_index][column_index] = '.';              }
            }
        }
    }
    
    (total_accessible_paper_roll, original_grid_copy)
}


fn _main(grid: Vec<Vec<char>>) -> i32 {
    let mut grid = grid.clone();
    let mut total_accessible_paper_rol = 0;
    let mut found_accessible_paper_rol = true;
    
    while found_accessible_paper_rol {
        let (total, new_grid) = calculate_total_accessible_paper_roll(grid);
        total_accessible_paper_rol += total;
        grid = new_grid;
        
        if total == 0 {
            found_accessible_paper_rol = false;
        }
    }
    
    total_accessible_paper_rol
    
}


fn main() {
    let binding = fs::read_to_string("2025/data/day_4_input.txt").expect("Could not read the input file");
    let lines = binding.lines();
    let lines = lines.map(|line| line.to_owned()).collect::<Vec<String>>();
    let grid = lines.iter().map(|row| row.chars().collect::<Vec<char>>()).collect::<Vec<Vec<char>>>();
        
    let total = _main(grid);
    println!("TOTAL: {:?}", total);
}