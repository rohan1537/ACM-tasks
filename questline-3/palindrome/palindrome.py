s = input("Enter a string: ")
result = ""

for i in range(len(s)):
    for a, b in [(i, i), (i, i+1)]:
        while a >= 0 and b < len(s) and s[a] == s[b]:
            a -= 1
            b += 1
        if b - a - 1 > len(result):
            result = s[a+1:b]

print("Longest Palindromic Substring:", result)
