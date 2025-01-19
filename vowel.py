# Function to count vowels
def count_vowels(s):
    # Define vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    count = 0  # Initialize vowel count
    # Iterate through each character in the string
    for char in s:
        if char in vowels:  # Check if the character is a vowel
            count += 1  # Increment count if vowel found
    return count

# Example usage
input_string = "Creative Coding"
# Call the function and store the result
vowel_count = count_vowels(input_string)
# Print the number of vowels
print("Number of vowels:", vowel_count)
