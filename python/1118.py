def calcular_media():
    notas = []

    while len(notas) < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("nota invalida")

    media = sum(notas) / 2
    print(f"media = {media:.2f}")

while True:
    calcular_media()

    while True:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())
        if opcao == 1:
            break  
        elif opcao == 2:
            exit()  
        else:
            continue 
