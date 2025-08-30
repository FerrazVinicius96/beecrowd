A = float(input())
B = float(input())
C = float(input())

pesos = [2, 3, 5]
valores = [A, B, C]

acumulador = 0
for valor, peso in zip(valores, pesos):
    acumulador += valor * peso

media_ponderada = acumulador / sum(pesos)
print(f"MEDIA = {media_ponderada:.1f}")