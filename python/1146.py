def sequencia(n=0):
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            lista = []
            for nmr in range(1, n + 1):
                lista.append(nmr)
            lista_tratada = map(str, lista)    
            print(' '.join(lista_tratada))

sequencia()