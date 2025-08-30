while True:
    numeros = input().split(" ")
    numeros_formatados = list(map(int, numeros))
    numero_1, numero_2 = numeros_formatados

    if numero_1 <= 0 or numero_2 <=0:
        break

    sequencia = []
    soma = 0

    if numero_1 > numero_2:
        for i in range(numero_2, numero_1 + 1, 1):
            soma += i
            sequencia.append(i)

    else:
        for i in range(numero_1, numero_2 + 1, 1):
            soma += i
            sequencia.append(i)
        
    sequencia_formatada = " ".join(map(str, sequencia))
    print(f'{sequencia_formatada} Sum={soma}')

    