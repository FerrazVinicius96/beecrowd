def distance():
    x1, y1 = list(map(float, input().split()))
    x2, y2 = list(map(float, input().split()))
    resu_inter = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    resu_final = resu_inter ** 0.5
    return f'{resu_final:.4f}'

print(distance())