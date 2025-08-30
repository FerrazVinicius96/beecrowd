n = int(input())

for _ in range(n):
    dieta = input().strip()
    cafe = input().strip()
    almoco = input().strip()

   
    consumido = cafe + almoco

 
    dieta_set = set(dieta)
    dieta_contagem = {}

    for alimento in dieta:
        dieta_contagem[alimento] = dieta_contagem.get(alimento, 0) + 1

    valido = True

    for alimento in consumido:
        if alimento not in dieta_contagem or dieta_contagem[alimento] == 0:
            valido = False
            break
        dieta_contagem[alimento] -= 1

    if not valido:
        print("CHEATER")
    else:
       
        jantar = []
        for alimento in sorted(dieta):
            if dieta_contagem[alimento] > 0:
                jantar.append(alimento)
        print("".join(jantar))