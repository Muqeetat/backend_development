def first_non_repeat_char(s):
   
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
	print(first_non_repeat_char("swiss")) 
	print(first_non_repeat_char("aabbdd"))  
