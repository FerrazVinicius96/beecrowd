# -*- coding: utf-8 -*-

salesperson = str(input())
fixed_salary = float(input())
total_value = float(input())

salary = (total_value * 0.15) + fixed_salary

print(f'TOTAL = R$ {salary:.2f}')