use std::fs;


fn is_valid_instruction(part: String) -> Option<bool> {
    
}

fn extract_instructions(data: String) -> Vec<String> {
    let mut instructions = Vec::new();
    let mut do_instruction = true;
    
    let mut instruction_parts = String::new();
    let mut current_instruction = String::new();
    
    let special_chars = ['m', 'u', 'l', '(', ')', ',', '-'];
    
    for char in data.chars() {
        if special_chars.contains(&char) {
            current_instruction.push(char);
        } else {
            current_instruction = "";
        }
    }
    
    valid_instruction = is_valid_instruction(current_instruction);
    
    match valid_instruction {
        
    }
    
    instructions
    
}


fn main() {
    let data = fs::read_to_string("_2024/data/day_3_input.txt").expect("Failed to Read Input File");
    
    println!("Data = {data}");
    
    let instructions = extract_instructions(data);
}