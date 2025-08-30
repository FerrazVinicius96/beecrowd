def decifrar():
    n = int(input())
    while n > 0:
        palavra_codificada = input()
        chave = int(input())

        # Deslocamento circular no intervalo de 'A' a 'Z'
        codigo = [
            chr((ord(letra) - ord('A') - chave) % 26 + ord('A')) 
            for letra in palavra_codificada
        ]

        print(''.join(codigo))
        n -= 1

decifrar()