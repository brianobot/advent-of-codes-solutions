

def get_largest_joltage(battery_bank: str) -> int:
    values = list(battery_bank)
    max = int("".join(battery_bank[0:2]))
    for idx, i in enumerate(values):
        for j in values[idx + 1:]:
            value = int(f"{i}{j}")
            if value > max:
                max = int(f"{i}{j}")
    return max


def get_total_joltage(battery_banks: list[str]) -> int:
        return sum([get_largest_joltage(item) for item in battery_banks])


if __name__ == "__main__":
    battery_banks = [line.strip() for line in open("2025/data/day_3_input.txt").readlines()]

    total_joltage = get_total_joltage(battery_banks)
    print(f"Total Joltage: {total_joltage}")