use std::cmp;
use std::fs;


fn calculate_total_distance_diff(locations_a: Vec<u32>, locations_b: Vec<u32>) -> u32 {
    let mut location_a = locations_a.clone();
    let mut location_b = locations_b.clone();
    
    // Sort both list first
    location_a.sort();
    location_b.sort();
    
    let mut total = 0;
    for (a, b) in location_a.iter().zip(location_b.iter()) {
        total += cmp::max(a, b) - cmp::min(a, b);
    }
    
    total
 }
 
 
 fn calculate_total_similarity_score(locations_a: Vec<i32>, locations_b: Vec<i32>) -> i32 {
     let mut total = 0;
     
     for location_id in locations_a {
         let similarity_score = locations_b.iter().filter(|item| **item == location_id).count() as i32 * location_id;
         total += similarity_score;
     }
     
     total 
 }
 

 fn main() {
     let mut list_a = Vec::new();
     let mut list_b = Vec::new();
     
     let content = fs::read_to_string("_2024/data/day_1_input.txt").expect("Failed to Read Input File");
     
     for line in content.lines() {
         let numbers = line.split_whitespace().map(|item| item.parse::<i32>().expect("Fail to convert to integer")).collect::<Vec<_>>();
         
         list_a.push(numbers[0]);
         list_b.push(numbers[1]);
     }
     
     let result = calculate_total_similarity_score(list_a, list_b);
     println!("Result = {result}");
 }