use std::fs;
use std::collections::HashMap;


const OPS: HashSet<&str, &str> = HashSet::from([
    ("+", )
])


fn solve_equation(data_columns: Vec<Vec<&str>>) -> i32 {
    let mut total = 0;
    
    for col in data_columns {
        let op = col.last();
        let ops = OPS.get(op)
    }
    
    total
}

fn main() {
    let content = fs::read_to_string("_2025/data/day_6_input.txt").expect("Failed to Read Input Data");
    let lines: Vec<Vec<&str>> = content
            .lines()
            .map(
                |line| line
                    .split_whitespace()
                    .collect::<Vec<_>>()
            )
            .collect::<Vec<_>>();
    
    println!("{lines:?}");
}