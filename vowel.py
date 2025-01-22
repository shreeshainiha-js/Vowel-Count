def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0 
    for char in s:
        if char in vowels:  # Check if the character is a vowel
            count += 1  # Increment count if vowel found
    return count
input_string = "Creative Coding"
vowel_count = count_vowels(input_string) # function call
print("Number of vowels:", vowel_count)
