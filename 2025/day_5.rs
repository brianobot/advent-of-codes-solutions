use std::fs;
use std::collections::HashSet;


fn merge_ranges(ranges: Vec<String>) -> Vec<String> {
    let mut intervals = ranges
        .iter()
        .map(
            |range| range.splitn(2, "-")
            .map(|i| i.parse::<i64>().unwrap())  
            .collect::<Vec<_>>()
        )
        .collect::<Vec<_>>();
    
    
    intervals.sort();
    println!("Intervals: {:?}", intervals);
    
    let mut merged: Vec<Vec<i64>> = Vec::new();
    
    for range in intervals.iter() {
        if merged.is_empty() || range[0] > merged.last().unwrap()[1] {
            merged.push(range.clone());
        } else {
            let last = merged.last_mut().unwrap();
            last[1] = std::cmp::max(last[1], range[1].clone())
        }
    }
    
    let intervals = merged.iter().map(|range| format!("{}-{}", range[0], range[1])).collect::<Vec<String>>();
    intervals
}


fn get_total_fresh_items(fresh_ids: Vec<String>) -> i64 {
    let merged_range = merge_ranges(fresh_ids.clone());
    let mut total = 0;
    
    for item_range in merged_range {
       
       let value = item_range.splitn(2, "-")
           .map(|i| i.parse::<i64>().unwrap())
           .collect::<Vec<_>>();
       
       let (start, end) = (value[0], value[1]);
       
       total += (end - start) + 1;
    }
    
    total
}

fn get_total_available_fresh_items(fresh_ids: Vec<String>, available_ids: Vec<String>) -> i32 {
    let mut total = 0;
    
    for available_id in available_ids {
        let available_id = available_id.parse::<i32>().expect("Failed to Convert String to Integer");
        for fresh_id in fresh_ids.iter() {
            let (start, end) = fresh_id.split_once("-").expect("Expected One -");
            let start = start.parse::<i32>().expect("Failed to convert start to integer");
            let end = end.parse::<i32>().expect("Failed to convert start to integer");
            let range = start..=end;
            if range.contains(&available_id) {
                total += 1;
                break;
            }
        }
    }
    
    total
}

fn split_list(seq: Vec<String>, sep: String) -> Vec<Vec<String>> {
    let mut parts = Vec::new();
    for item in seq.iter() {
        if item == &sep {
            parts.push(Vec::new());
            continue;
        }
        
        if let Some(last_part) = parts.last_mut() {
            last_part.push(item.clone());
        } else {
            parts.push(vec![item.clone()]);
        }
    }
    
    parts
}

fn main() {
    let binding = fs::read_to_string("2025/data/day_5_input.txt").expect("Failed to Read Data File");
    let lines = binding.lines().map(String::from).collect();
    
    let parts = split_list(lines, "".to_string());
    #[allow(dead_code, unused_variables)]
    let (fresh_ids, available_ids) = (parts[0].clone(), parts[1].clone());
    
    // let total = get_total_available_fresh_items(fresh_ids, available_ids);
    let total = get_total_fresh_items(fresh_ids);
    println!("Total: {:?}", total);
    // 
    // let result = merge_ranges(fresh_ids);
    // println!("Result: {:?}", result);
}