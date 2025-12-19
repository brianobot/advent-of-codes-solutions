

def merge_ranges(ranges: list[str]) -> list[str]:
    # Parse and sort ranges by start value
    intervals = sorted(
        (int(start), int(end)) 
        for start, end in (r.split("-") for r in ranges)
    )

    merged = []
    # merges = [
    # [start, end]
    # ]

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            # No overlap
            merged.append([start, end])
        else:
            # Overlap — extend the previous range
            merged[-1][1] = max(merged[-1][1], end)

    return [f"{start}-{end}" for start, end in merged]


def get_total_fresh_items(fresh_ids: list[str]) -> int:
    merged_ranges = merge_ranges(fresh_ids)
    total = 0
    
    for item_range in merged_ranges:
        print(f"Item Range: {item_range}")
        start, end = map(int, item_range.split("-"))
        total += ((end - start) + 1)
        
    return total
        

def get_total_available_fresh_items(fresh_ids: list[str], available_ids: list[str]) -> int:
    total = 0
    for available_id in available_ids:
        available_id = int(available_id)
        for fresh_id in fresh_ids:
            start, end = map(int, fresh_id.split("-"))
            if available_id in range(start, end + 1):
                total += 1
                break
    
    return total


def split_list(seq: list[str], sep: str = "") -> list[list[str]]:
    parts = [[]]
    for item in seq:
        if item == sep:
            parts.append([])
            continue
        
        parts[-1].append(item)
    return parts


if __name__ == "__main__":
    data = [line.strip() for line in open("2025/data/day_5_input.txt").readlines()]
    fresh_ids, available_ids = split_list(data, "")
    
    # total = get_total_available_fresh_items(fresh_ids, available_ids)
    total = get_total_fresh_items(fresh_ids)
    print(f"Total: {total}")
