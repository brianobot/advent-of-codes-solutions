use std::fs;


fn pairwise<T: Clone>(sequence: Vec<T>) -> Vec<(T, T)> {
    let mut pairs = Vec::new();
    
    for (index, value) in sequence.iter().enumerate() {
        if index == (sequence.len() - 1) {
            break
        }
        
        let pair = (value.clone(), sequence[index + 1].clone());
        pairs.push(pair);
    }
    
    pairs
}

fn report_is_safe(report: Vec<i32>) -> (bool, Option<usize>, Option<String>) {
    let pairs = pairwise(report);    
    let diffs = pairs.iter().map(|(a, b)| b - a).collect::<Vec<_>>();
    
    let mut contains_neg = false;
    let mut contains_pos = false;
    
    for (index, value) in diffs.iter().enumerate() {
        
        if value.abs() > 3 || value.abs() < 1 {
            return (false, Some(index), None);
        }
        
        if *value > 0 {
            contains_pos = true;
        } else {
            contains_neg = true;
        }
        
        if contains_neg && contains_pos {
            return (false, Some(index), None);
        }
    }
    
    (true, None, None)
    
}

fn report_is_safe_with_dampener(report: Vec<i32>) -> (bool, Option<usize>, Option<String>) {
    let mut report_copy = report.clone();
    let (is_safe, failure_index, _) = report_is_safe(report_copy.clone());
    
    if !is_safe {
        if (0..3).contains(&failure_index.unwrap()) { 
            for index in 0..3 {
                let faulty_record = report_copy.remove(index);
                let (second_attempt, _, _) = report_is_safe(report_copy.clone());
                
                if second_attempt {
                    return (true, Some(index), None);
                }
                report_copy.insert(index, faulty_record);
            }
            return (false, Some(1), None);
        } else {
            report_copy.remove(failure_index.unwrap());
            return report_is_safe(report_copy.clone());
        }  
    }
    
    
    (true, None, None)
}

fn get_total_safe_report(reports: Vec<Vec<i32>>, with_dampener: bool) -> i32 {
    let mut total = 0;
    let report_safety_func = if with_dampener { report_is_safe_with_dampener } else { report_is_safe };
    
    for report in reports {
        let (is_safe, _, _) = report_safety_func(report);
        
        if is_safe {
            total += 1;
        }   
    }
    
    total
}


fn main() {
    let content = fs::read_to_string("2024/data/day_2_input.txt").expect("Failed to Read Input Data");
    let reports = content.lines()
            .map(
                |line: &str| 
                    line.split_whitespace()
                        .map(|item| item.parse::<i32>().expect("failed to convert to Integer"))
                        .collect::<Vec<_>>()

            ).collect::<Vec<_>>();
    
    // println!("Reports: {reports:?}");
    
    let total = get_total_safe_report(reports, false);
    println!("Total: {total}");
}