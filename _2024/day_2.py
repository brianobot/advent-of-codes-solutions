from itertools import pairwise
from operator import sub
from typing import cast



def report_is_safe(report: list[int]) -> tuple[bool, int | None, str | None]:
    """
    Checks if a report is safe according to the rules of the challenge and returns
    the state and the index of the first noted issue with the report
    """
    pairs = list(pairwise(report))
    diffs = [cast(int, sub(a, b)) for a, b in pairs]
    
    contains_neg = False
    contains_pos = False
    for index, value in enumerate(diffs, start=1):
        if abs(value) > 3 or abs(value) < 1:
            return (False, index, f"Difference {abs(value)} greater than 3 or less than 1")
        
        if value >= 0: 
            contains_pos = True
        else: 
            contains_neg = True
        
        if contains_neg and contains_pos:
            return (False, index, "Contains Increasing and decreasing difference")
    
    return (True, None, None)
    

def report_is_safe_with_dampener(report: list[int]) -> tuple[bool, int | None, str | None]:
    """
    This runs the safety check function and ignores a single case of safety concern
    """
    report_copy = report.copy()
    is_safe, failure_index, reason = report_is_safe(report_copy)
    
    if not is_safe:
        if failure_index in range(3):
            for index in range(0, 3):
                faulty_record = report_copy.pop(index)
                result = report_is_safe(report_copy)
                if result[0]:
                    return (True, index, None)
                report_copy.insert(index, faulty_record)
            return (False, 1, reason)
        else:
            report_copy.pop(cast(int, failure_index))
            return report_is_safe(report_copy)
    return (True, None, None)


def get_total_safe_report(reports: list[list[int]], with_dampener: bool = False):
    total = 0
    report_safety_func = report_is_safe_with_dampener if with_dampener else report_is_safe
    for report in reports:
        is_safe, *_ = report_safety_func(report)
        if is_safe:
            total += 1
        
    return total
    

if __name__ == "__main__":
    reports = [list(map(int, line.split())) for line in open("_2024/data/day_2_input.txt").readlines()]
    
    safe_reports_count = get_total_safe_report(reports, True)
    
    print("Safe Report Count: ", safe_reports_count)