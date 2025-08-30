def soma(lista):
    return sum(lista)

def media(lista):
    return sum(lista)/len(lista)

coluna_escolhida = int(input())
operacao = input().upper()
matriz = []

for l in range(12):
    linha = []
    for c in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

coluna = []

for i, e in enumerate(matriz):
    coluna.append(matriz[i][coluna_escolhida])

if operacao == 'S':
    print(f'{soma(coluna):.1f}')
elif operacao == 'M':
    print(f'{media(coluna):.1f}')