def nth_max_min(numbers, n):
    # Remove duplicates by converting the list to a set
    unique_numbers = list(set(numbers))
    
    # Sort the numbers in ascending order
    unique_numbers.sort()
    
    # Check if n is within the range of the unique numbers list
    if n > len(unique_numbers) or n <= 0:
        return None, None
    
    nth_min = unique_numbers[n - 1]
    nth_max = unique_numbers[-n]
    
    return nth_min, nth_max

# Example usage
numbers = [4, 2, 5, 1, 2, 7, 4, 3, 6]
n = 3
nth_min, nth_max = nth_max_min(numbers, n)

if nth_min is not None and nth_max is not None:
    print(f"The {n}rd minimum element is: {nth_min}")
    print(f"The {n}rd maximum element is: {nth_max}")
else:
    print(f"The value of n ({n}) is out of range for the unique numbers in the list.")
