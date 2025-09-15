# Array Rotation – Questline 6

## Problem
Given an integer array `nums`, rotate it to the right by `k` steps.  
Example:  
Input: `nums = [1, 2, 3, 4, 5]`, `k = 3`  
Output: `[3,4, 5, 1, 2]`

## Approach

### Step-by-step Logic:
1. Normalize `k` using `k % len(nums)` to handle large values.
2. Split the array into two parts:
   - Last `k` elements
   - First `len(nums) - k` elements
3. Concatenate the two parts in reverse order.

### Why This Works:
- It avoids shifting elements one by one.
- It’s simple and efficient for beginners to understand.

## Example
```python
nums = [1, 2, 3, 4, 5]
k = 3
# Output: [3,4, 5, 1, 2]
