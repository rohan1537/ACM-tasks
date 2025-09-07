total_sum = 0
for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        total_sum += number
print(total_sum)



a, b = 1, 2
total = 0
while b <= 4_000_000:
    if b % 2 == 0:
        total += b
    a, b = b, a + b
print(total)


