n = int(input())
coelhos = 0
ratos = 0
sapos = 0

while n:
    teste = input().split(" ")
    if teste[1] == 'C':
        coelhos += int(teste[0])
        n -= 1
    elif teste[1] == 'R':
        ratos += int(teste[0])
        n -= 1
    elif teste[1] == 'S':
        sapos += int(teste[0])
        n -= 1

cobaias = coelhos + ratos + sapos

percentual_coelhos = (coelhos * 100) / cobaias
percentual_ratos = (ratos * 100) / cobaias
percentual_sapos = (sapos * 100) / cobaias

print(f'Total: {cobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')