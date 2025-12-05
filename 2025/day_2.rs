use std::fs;
use std::collections::HashSet;


fn get_common_factors(number: i32) -> Vec<i32> {
    (1..number).filter(|i| number % i == 0).collect()
}

fn id_is_valid(id: i64) -> bool {
    let str_form = id.to_string();
    let str_len = str_form.len() as i32;
    
    let common_factors = get_common_factors(str_len);
    for common_factor in common_factors {
        let mut parts: HashSet<&str> = HashSet::new();
        let mut index = (0, common_factor);
        while index.1 <= str_len {
            let part = &str_form[index.0 as usize..index.1 as usize];
            parts.insert(&part);
            index = (index.0 + common_factor, index.1 + common_factor);
        }
    
        if parts.len() == 1 {
            return false
        }
        
    }
    
    true
    
}

fn get_invalid_id_sum(id_ranges: &str) -> i64 {
    let ranges: Vec<&str> = id_ranges.split(",").collect();
    let mut invalid_sum: i64 = 0;
    
    for id_range in ranges {
        let id_range = id_range.split("-").collect::<Vec<&str>>();    
        let (start_index, end_index) = (id_range.get(0).unwrap(), id_range.get(1).unwrap());
        let (start_index, end_index) = (start_index.parse::<i64>().unwrap(), end_index.parse::<i64>().unwrap());
        for id in start_index..=end_index {
            if !id_is_valid(id) {
                invalid_sum += id;
            }
        }
    }
    
    invalid_sum
}


fn main() {
    let content = fs::read_to_string("2025/data/day_2_input.txt").expect("Could not Read Input File");
    let result = get_invalid_id_sum(&content);
    println!("Total Invalid Id Sum = {result}");

}