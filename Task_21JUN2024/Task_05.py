#String reverse:-

# 1. Using Slicing
def reverse_string_slicing(s):
    return s[::-1]  #slicing

print(reverse_string_slicing("binit"))  # Output: "tinib"

# 2. Using the reversed() Function and join()

def reverse_string_reversed(s):
    return ''.join(reversed(s))

print(reverse_string_reversed("binit"))  # Output: "tinib"

# 3. Using loop

def reverse_string_loop(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string_loop("binit"))  # Output: "tinib"