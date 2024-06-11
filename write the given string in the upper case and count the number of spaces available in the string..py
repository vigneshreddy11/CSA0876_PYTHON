def count(input_string):
    uppercase_string = input_string.upper()
    space_count = input_string.count(' ')

    return uppercase_string, space_count


input_string = "Hello, World! This is a test string."
uppercase_string, space_count = count(input_string)

print("Uppercase string:", uppercase_string)
print("Number of spaces:", space_count)
