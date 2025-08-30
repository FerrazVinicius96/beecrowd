cardapio = [
    {'codigo': 1, 'alimento': 'Cachorro quente', 'preco': 4.00},
    {'codigo': 2, 'alimento': 'X-Salada', 'preco': 4.5},
    {'codigo': 3, 'especificacao': 'X-Bacon', 'preco': 5.00},
    {'codigo': 4, 'especificacao': 'Torrada simples', 'preco': 2.00},
    {'codigo': 5, 'especificacao': 'Refrigerante', 'preco': 1.50}
]

codigo, qtd = map(int, input().split())

for elemento in cardapio:
    if elemento['codigo'] == codigo:
        total = elemento['preco'] * qtd
        print(f'Total: R$ {total:.2f}')