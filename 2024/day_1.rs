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
 
 
 fn 
 
 fn main() {
     
 }