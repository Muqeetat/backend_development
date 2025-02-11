def compress_string(s):
    
    if not s:
        return ""  # If the input string is empty, return an empty string
    
    result = []  # List to store the compressed version of the string
    count = 1    # Counter to track occurrences

    
    for i in range(1, len(s)):    # Iterate through the string starting from the second character
        if s[i - 1] == s[i]:  # If the current character matches the previous one, increase the count
            count += 1
        else:
            result.append(s[i - 1])  # Append the character to the compressed list
            if count > 1:
                result.append(str(count))  # Append the count if greater than 1
            count = 1  # Reset count for the next character

    
    result.append(s[-1])  # Append the last character and its count if it is greater than 1
    if count > 1:
        result.append(str(count))

    # print(f"Final list: {result}")  

    return ''.join(result)  # Join all items in the list into a string

 
if __name__ == "__main__":
    s = "adddsssssa"
  
    print(compress_string(s))




# # Test cases using assert
# assert compress_string('bbcceeee') == 'b2c2e4'
# assert compress_string('aaabbbcccaaa') == 'a3b3c3a3'
# assert compress_string('a') == 'a'

# print("All tests passed successfully!")