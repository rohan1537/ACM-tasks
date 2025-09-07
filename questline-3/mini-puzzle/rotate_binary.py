s = input("Enter a binary string: ")
k = int(input("Enter number of steps to rotate: "))
k = k % len(s)
rotated = s[k:] + s[:k]
print("Decimal value:", int(rotated, 2))
