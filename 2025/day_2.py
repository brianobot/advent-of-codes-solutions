

def get_common_factors(number: int) -> list[int]:
    common_factors = []
    for i in range(1, number):
        if number % i == 0:
            common_factors.append(i)
    return common_factors


def id_is_valid(id: int) -> bool:
    str_form = str(id)
    str_len = len(str_form)
    common_factors = get_common_factors(str_len)
    for common_factor in common_factors:
        parts = set()
        index = (0, common_factor)
        while index[1] <= str_len:
            part = str_form[index[0]:index[1]]
            parts.add(part)
            index = (index[0] + common_factor, index[1] + common_factor)
            
        if len(parts) == 1:
            return False

    return True


def get_invalid_id_sum(id_ranges: str) -> int:
    ranges = id_ranges.split(",")
    invalid_sum = 0
    for id_range in ranges:
        start_index, end_index = [int(index) for index in id_range.split("-")]
        for id in range(start_index, end_index + 1):
            if not id_is_valid(id):
                print(f"Found Invalid ID = {id}")
                invalid_sum += id
    return invalid_sum
    

if __name__ == "__main__":
    id_ranges = open("2025/data/day_2_input.txt").read()
    total_invalid_sum = get_invalid_id_sum(id_ranges)
    print(f"Total Invalid Sum = {total_invalid_sum}")
