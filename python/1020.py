anos_em_dias = int(input())

anos = anos_em_dias // 365
meses = (anos_em_dias % 365) // 30
dias = (anos_em_dias % 365) % 30
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')