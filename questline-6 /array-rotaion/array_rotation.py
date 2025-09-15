def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    return nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5]
k = 3


rotated = rotate_array(nums, k)
print("Original:", nums)
print("Rotated:", rotated)
