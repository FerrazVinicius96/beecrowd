valor = int(input())
original = valor

qtd_100 = valor // 100
valor %= 100

qtd_50 = valor // 50
valor %= 50

qtd_20 = valor // 20
valor %= 20

qtd_10 = valor // 10
valor %= 10

qtd_5 = valor // 5
valor %= 5

qtd_2 = valor // 2
valor %= 2

qtd_1 = valor

print(f'{original}')
print(f'{qtd_100} nota(s) de R$ 100,00')
print(f'{qtd_50} nota(s) de R$ 50,00')
print(f'{qtd_20} nota(s) de R$ 20,00')
print(f'{qtd_10} nota(s) de R$ 10,00')
print(f'{qtd_5} nota(s) de R$ 5,00')
print(f'{qtd_2} nota(s) de R$ 2,00')
print(f'{qtd_1} nota(s) de R$ 1,00')