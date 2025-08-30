primeiro_caso = True

while True:
    N = int(input())
    if N == 0:
        break

    palavras = [input().strip() for _ in range(N)]
    max_len = max(len(p) for p in palavras)

    if not primeiro_caso:
        print()
    primeiro_caso = False

    for palavra in palavras:
        print(palavra.rjust(max_len))