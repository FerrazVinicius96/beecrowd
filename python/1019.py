segundos_entrada = int(input())

def calcular_hora(inteiro):
    horas = segundos_entrada // 3600
    minutos = (segundos_entrada % 3600) // 60
    segundos_saida = (segundos_entrada % 3600) % 60
    print(horas, minutos, segundos_saida, sep=':')

calcular_hora(segundos_entrada)