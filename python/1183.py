def soma(lista):
    return sum(lista)

def media(lista):
    return sum(lista)/len(lista)

matriz = []
operacao = input().upper()

for l in range(12):
    linha = []
    for c in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

valores = []
for i in range(12):
    for j in range(12):
        if j > i:
            valores.append(matriz[i][j])

if operacao == 'S':
    print(f'{soma(valores):.1f}')
elif operacao == 'M':
    print(f'{media(valores):.1f}')