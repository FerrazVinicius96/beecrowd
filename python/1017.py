def receber_horas():
    tempo_viagem = int(input())
    return tempo_viagem

def velo_media():
    velo = int(input())
    return velo

def calcular_gasolina():
    consumo_medio = 12
    resultado = velo_media() * receber_horas() / consumo_medio
    return f'{resultado:.3f}'

print(calcular_gasolina())