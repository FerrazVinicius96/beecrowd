lista_1 = ['1'] #2 leds
lista_2 = ['7'] #3 leds
lista_3 = ['4'] #4 leds
lista_4 = ['2', '3', '5'] #5 leds
lista_5 = ['6', '9', '0']
lista_6 = ['8']

n = int(input())
while n > 0:
    contador = 0
    numero = input()
    for e in numero:
        if e in lista_1:
            contador+=2
        elif e in lista_2:
            contador+=3
        elif e in lista_3:
            contador+=4
        elif e in lista_4:
            contador+=5
        elif e in lista_5:
            contador+=6
        elif e in lista_6:
            contador+=7
    print(f'{contador} leds')
    n-=1