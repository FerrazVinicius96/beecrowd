x = int(input())
y = int(input())


start = min(x, y) + 1
end = max(x, y)


odd_sum = 0
for i in range(start, end):
    if i % 2 != 0:
        odd_sum += i


print(odd_sum)