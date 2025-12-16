use std::fs;


fn get_common_factors(number: usize) -> Vec<usize> {
    (1..number).filter(|i| number % i == 0).map(|x| x as usize).collect()
}

fn id_is_valid(id: i64) -> bool {
    let str_form = id.to_string();
    let str_len = str_form.len();
    
    for common_factor in get_common_factors(str_len) {
        let first_chunk = &str_form[..common_factor];
        let mut all_same = true;
        
        for chunk in str_form.as_bytes().chunks(common_factor) {
            if chunk != first_chunk.as_bytes() {
                all_same = false;
                break
            }
        }
    
        if all_same {
            return false;
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
