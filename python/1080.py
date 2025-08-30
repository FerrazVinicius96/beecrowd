lista = []
maior_valor = 0

for _ in range(100):
    lista.append(int(input()))

for e in lista:
    if e > maior_valor:
        maior_valor = e

posicao = lista.index(maior_valor)

print(maior_valor)
print(posicao + 1)