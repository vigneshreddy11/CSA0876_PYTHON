sample_string = "Hello World"
vowel_count = 0
consonant_count = 0
vowels = {'a', 'e', 'i', 'o', 'u'}
sample_string = sample_string.lower()
for char in sample_string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
