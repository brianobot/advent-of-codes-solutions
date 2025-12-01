from itertools import pairwise
from operator import sub
from typing import cast



def report_is_safe(report: list[int]) -> tuple[bool, int]:
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
            return (False, index)
        
        if value >= 0: 
            contains_pos = True
        else: 
            contains_neg = True
        
        if contains_neg and contains_pos:
            return (False, index)
    
    return (True, -1)
    

def report_is_safe_with_dampener(report: list[int]) -> tuple[bool, int]:
    """
    This runs the safety check function and ignores a single case of safety concern
    """
    is_safe, failure_index = report_is_safe(report)
    if not is_safe:
        if failure_index == 1:
            for index in range(0, 2):
                record = report.pop(index)
                result = report_is_safe(report)
                if result[0]:
                    return (True, index)
                report.insert(index, record)
            return (False, 1)
        else:
            report.pop(failure_index)
            return report_is_safe(report)
    return (True, -1)


if __name__ == "__main__":
    # reports = open("2024/data/day_2_input.txt").readlines()
    reports = [
        # [7, 6, 4, 2, 1],
        # [1, 2, 7, 8, 9],
        # [9, 7, 6, 2, 1],
        # [1, 3, 2, 4, 5],
        # [8, 6, 4, 4, 1],
        # [1, 2, 3, 7, 6],
        # [5, 7, 9, 12, 13, 11],
        # [10, 9, 7, 4, 4, 1],
        [1, 6, 7, 8, 9],
        [3, 10, 11, 12, 13],
        [8, 6, 4, 4, 1],
        [2, 4, 6, 5, 7],
        [9, 8, 7, 3, 1],
    ]
    safe_report_count = 0
    for report in reports:
        report = [int(item) for item in report]
        result = report_is_safe_with_dampener(report) 
        if result[0]:
            safe_report_count += 1
            # print(f"{report = }, {result = }")
        else:
            print(f"{report = }, {result = }")
            
    print(f"Safe Report Count = {safe_report_count}")