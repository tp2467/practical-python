# mortgage_extra.py
#
# Exercise 1.10

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = float(input('Enter start month with extra payment: '))
extra_payment_end_month = float(input('Enter last month with extra payment: '))
extra_payment = float(input('Enter extra payment: '))

while principal > 0:
    if (month >= (extra_payment_start_month-1)) and (month < extra_payment_end_month):
        principal = principal * (1+rate/12) - payment - extra_payment
        if principal <= 0.0:
            total_paid = total_paid + payment + extra_payment + principal  
            principal = 0.0  
        else:
            total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment 
        if principal < 0.0:
            total_paid = total_paid + payment + principal
            principal = 0
        else:
            total_paid = total_paid + payment
    print(month, total_paid, round(principal, 2))
    month = month + 1
print('Total paid', total_paid)
print('Total months', month)
print('Total years', month/12)