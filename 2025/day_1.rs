use std::fs;

fn get_dial_current_position(turn: String, start: u32, _cycle: u32) -> (u32, u32) {
    if _cycle == 0 {
        panic!("The Cycle Can not be Zero");
    }
    
    let turn_steps = turn[1..].trim().parse::<u32>().unwrap();
    let direction = if turn.starts_with("L") { -1 } else { 1 };
    let new_position = (start as i32 + (direction * turn_steps as i32)) % _cycle as i32;
    
    let mut crossings = 0;
    for i in 0..turn_steps {
        let current_value = (start as i32 + (direction * i as i32)) % _cycle as i32;
        if current_value == 0 && (i != 0 || i > (turn_steps - 1)) {
            crossings += 1;
        }
    }
    
    (new_position as u32, crossings as u32)
}

fn get_total_zero_hit(seq: Vec<String>, start: u32, _cycle: u32) -> u32 {
    let mut start: u32 = start;
    let mut total_zero_hit: u32 = 0;
    for turn in seq.into_iter() {
        let (current_dial, zero_count) = get_dial_current_position(turn, start, _cycle);
        start = current_dial;
        
        if current_dial == 0 {
            total_zero_hit += 1;
        }
        
        total_zero_hit += zero_count;
    }
    
    return total_zero_hit;
}

fn main() {
    let binding = fs::read_to_string("2025/data/day_1_input.txt").expect("Could not read from file");
    let lines = binding.lines();
    let lines: Vec<String> = lines.map(|l| l.to_owned()).collect();
        
    let result = get_total_zero_hit(lines, 50, 100);
    println!("Total Zero Hit: {:?}", result);
}