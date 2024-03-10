def find_most_repeated_char(string):
    char_count = {}
    max_count = 0
    most_repeated_char = None

    # Count the occurrences of each character in the string
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        if char_count[char] > max_count:
            max_count = char_count[char]
            most_repeated_char = char

    return most_repeated_char

# Example usage
string = "abbbacaaabacab"
most_repeated_char = find_most_repeated_char(string)

if most_repeated_char:
    print(f"The most repeated character is '{most_repeated_char}'")
else:
    print("The string is empty")
