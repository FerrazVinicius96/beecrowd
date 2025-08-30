salario = float(input())
aumento_01, aumento_02, aumento_03, aumento_04, aumento_05 = 0.15, 0.12, 0.1, 0.07, 0.04

if salario <= 400:
    reajuste = salario * aumento_01
    salario_final = salario + reajuste
    print(f'Novo salario: {salario_final:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {int(aumento_01 * 100)} %')
elif salario > 400 and salario <= 800:
    reajuste = salario * aumento_02
    salario_final = salario + reajuste
    print(f'Novo salario: {salario_final:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {int(aumento_02 * 100)} %')
elif salario > 800 and salario <= 1200:
    reajuste = salario * aumento_03
    salario_final = salario + reajuste
    print(f'Novo salario: {salario_final:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {int(aumento_03 * 100)} %')
elif salario > 1200 and salario <= 2000:
    reajuste = salario * aumento_04
    salario_final = salario + reajuste
    print(f'Novo salario: {salario_final:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {int(aumento_04 * 100)} %')
else:
    reajuste = salario * aumento_05
    salario_final = salario + reajuste
    print(f'Novo salario: {salario_final:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {int(aumento_05 * 100)} %')