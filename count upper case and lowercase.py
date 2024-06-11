sample_string = "Hello World"
upper_count = 0
lower_count = 0
for char in sample_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
