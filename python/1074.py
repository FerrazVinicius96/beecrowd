n = int(input())

while n:
    numero = int(input())
    verificacao = numero % 2
    if numero == 0:
        positivo_negativo = 'NULL'
        print(f'{positivo_negativo}')
        n-=1
        continue
    if numero > 0:
        positivo_negativo = 'POSITIVE'
    else:
        positivo_negativo = 'NEGATIVE'
    if verificacao == 0:
        odd_even = 'EVEN'
    else:
        odd_even = 'ODD'        
    print(f'{odd_even} {positivo_negativo}')
    n-=1