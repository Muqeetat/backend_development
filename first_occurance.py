def first_non_repeat(s):
    if not s:
        return ""  # If the input string is empty, return an empty string
        
    char_count = {}  # Dictionary to store the count of each character

    for char in s:
        if char in char_count:
            char_count[char] += 1  # If character exists, increase count
        else:
            char_count[char] = 1  # If character is new, set count to 1

    # print(char_count)
    for char in s:
        if char_count[char] == 1:
            return char  # Return the first non-repeating character
            
    return -1  # If no non-repeating character is found, return -1


if __name__ == "__main__":
	print(first_non_repeat("swiss")) 
	print(first_non_repeat("aabbdd"))  


# Test cases using assert
assert first_non_repeat('bcceeee') == 'b'
assert first_non_repeat('aaabbbcaaas') == 'c'
assert first_non_repeat('aabbdd') == -1

print("All tests passed successfully!")