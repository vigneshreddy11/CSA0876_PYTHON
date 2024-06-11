from collections import Counter

def count_occurrences(numbers):
    return Counter(numbers)

# Example usage
numbers = [1, 2, 3, 1, 2, 1, 4, 3, 5, 1, 2, 3, 6, 3, 2]
occurrences = count_occurrences(numbers)

print("Occurrences of each number:")
for number, count in occurrences.items():
    print(f"{number}: {count}")
