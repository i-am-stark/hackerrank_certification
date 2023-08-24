def missingCharacters(s):
    # Create sets for all digits and lowercase English letters
    all_digits = set("0123456789")
    all_letters = set("abcdefghijklmnopqrstuvwxyz")
    
    # Create a set from the input string
    input_set = set(s)
    
    # Find missing digits and letters
    missing_digits = "".join(sorted(all_digits - input_set))
    missing_letters = "".join(sorted(all_letters - input_set))
    
    # Concatenate and return the result
    return missing_digits + missing_letters

# Read input
s = input()

# Call the function and print the result
result = missingCharacters(s)
print(result)
