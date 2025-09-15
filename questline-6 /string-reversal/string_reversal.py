def reverse_iterative(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

input_string = "Skibidi"

print("Original String:", input_string)
print("Iterative Reverse:", reverse_iterative(input_string))
print("Recursive Reverse:", reverse_recursive(input_string))