# -*- coding: utf-8 -*-
# Read input values
employee_number = int(input())
worked_hours = int(input())
hourly_rate = float(input())
salary = worked_hours * hourly_rate
print(f"NUMBER = {employee_number}")
print(f"SALARY = U$ {salary:.2f}")