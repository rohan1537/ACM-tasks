# String Reversal – Iterative and Recursive Methods

## Iterative Method
We loop through the string from the end to the beginning, appending each character to a new result string.

### Logic:
- Initialize an empty result string.
- Traverse the input string from the last character to the first.
- Append each character to the result.

## Recursive Method
We reverse the string by calling the function on the substring excluding the first character, and then appending the first character at the end.

### Logic:
- Base case: If the string is empty or has one character, return it.
- Recursive case: Call the function on the substring 's[1:]', then add 's[0]' to the result.
