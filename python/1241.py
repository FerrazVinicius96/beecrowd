def decodificando(n=0):
    n = int(input())
    while n > 0:
        p1, p2 = input().split()
        if p1.endswith(p2):
            print(f'encaixa')
        else:
            print(f'nao encaixa')
        n-=1


decodificando()