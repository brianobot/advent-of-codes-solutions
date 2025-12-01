
def calculate_total_distance_diff(locations_a: list[int], locations_b: list[int]) -> int:
    """
    Takes 2 list of integers and calculates the difference between each ordered element from each list
    and return the total difference from the calculation.
    """
    total = 0
    for a, b in zip(sorted(locations_a), sorted(locations_b)):
        diff = max(a, b) - min(a, b)
        total += diff
    return total
    
    
def calculate_total_similarity_score(locations_a: list[int], locations_b: list[int]) -> int:
    """
    Takes 2 list of integers and calculates the total similarity score for each value in the first list
    the similarity score is the product of the item in the first list and the number of occurrence of that value
    in the second list.
    """
    total = 0
    for location_id in locations_a:
        similarity_score = locations_b.count(location_id) * location_id
        total += similarity_score
    return total
    
    
if __name__ == "__main__":
    list_a = []
    list_b = []
    data = open("2024/data/day_1_input.txt")
    
    for line in data.readlines():
        a, b = line.split()
        list_a.append(int(a))
        list_b.append(int(b))
        
    print(f"{calculate_total_similarity_score(list_a, list_b) = }")