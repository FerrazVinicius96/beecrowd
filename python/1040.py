notas = list(map(float, input().split()))
pesos = [2, 3, 4, 1]

acumulador = 0
soma_pesos = sum(pesos)

for nota, peso in zip(notas, pesos):
    acumulador += nota * peso

media_final = acumulador / soma_pesos
print(f'Media: {media_final:.1f}')
if media_final >= 7:
    print(f'Aluno aprovado.')
elif media_final < 5:
    print(f'Aluno reprovado.')
elif media_final <= 6.9 and media_final >= 5:
    print(f'Aluno em exame.')
    nota_rec = float(input())
    print(f'Nota do exame: {nota_rec}')
    nova_media = (media_final + nota_rec) / 2
    if nova_media >= 5:
        print(f'Aluno aprovado.')
        print(f'Media final: {nova_media}')
    elif nova_media < 5:
        print(f'Aluno reprovado.')
        print(f'Media final: {nova_media}')