linha_escolhida = int(input())  # Não subtrai 1 aqui
operacao = input().upper()

matriz = []

for _ in range(12):
    linha = []
    for _ in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

# Funções para soma e média
def soma(lista):
    return sum(lista)

def media(lista):
    return sum(lista) / len(lista)

# Escolhe a operação
valores_linha = matriz[linha_escolhida]
if operacao == 'S':
    print(f'{soma(valores_linha):.1f}')
elif operacao == 'M':
    print(f'{media(valores_linha):.1f}')