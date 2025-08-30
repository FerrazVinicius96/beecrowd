x = int(input())
y = int(input())

start = min(x, y) + 1
end = max(x, y)

for v in range(start, end):
    if v % 5 == 2:
        print(v)
    elif v % 5 == 3:
        print(v)
    else:
        ...