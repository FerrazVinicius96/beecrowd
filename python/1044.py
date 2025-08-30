A, B = input().split(' ')
A = int(A)
B = int(B)

if B >= A:
    if B % A == 0:
        print(f'Sao Multiplos')
    else:
        print(f'Nao sao Multiplos')
else:
    if A % B == 0:
        print(f'Sao Multiplos')
    else:
        print(f'Nao sao Multiplos')