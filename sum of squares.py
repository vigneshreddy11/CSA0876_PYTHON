def sum_of_squares(numbers):
    total = 0
    for number in numbers:
        total += number**2
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
result = sum_of_squares(numbers)
print(f"The sum of the squares of the list is: {result}")
