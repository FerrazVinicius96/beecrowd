lista = list(map(int, input().split()))

original = lista.copy()

lista.sort()

for num in lista:
    print(num)

print()

for num in original:
    print(num)
