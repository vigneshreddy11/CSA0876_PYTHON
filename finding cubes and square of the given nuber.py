def find_cubes_and_squares(number):
    cube = number ** 3
    square = number ** 2
    return cube, square
number = 5
cube, square = find_cubes_and_squares(number)
print(f"The cube of {number} is {cube}")
print(f"The square of {number} is {square}")
