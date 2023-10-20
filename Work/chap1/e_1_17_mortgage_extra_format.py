# mortgage_extra.py
#
# Exercise 1.17
# Print with format

principal = 304000 #400000.0
rate = 0.06999
payment = 2022 #2477.16
total_paid = 0.0
month = 0

# principal = float(input('Enter principal: '))
# rate = float(input('Enter rate: '))
# payment = float(input('Enter monthly mortgage payment: '))
initial_principal = principal
extra_payment_start_month = float(input('Enter start month with extra payment: '))
extra_payment_end_month = float(input('Enter last month with extra payment: '))
extra_payment = float(input('Enter extra payment: '))

month_header = 'Month'
total_paid_header = 'Total paid'
principal_remaining_header = 'Principal remaining'

print(f'{month_header:>6} {total_paid_header:<15}  {principal_remaining_header:<10}')
while principal > 0:
    if (month >= (extra_payment_start_month-1)) and (month < extra_payment_end_month):
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print(f'{month:>6} ${round(total_paid,2):<15,} ${round(principal, 2):<10,}')
    month = month + 1
    
print(f'Total paid   ${total_paid:>15,.3f}')
print(f'Total months  {month:>15}')
print(f'Total years   {month/12:>15.0f}', )
print(f'Interest paid: ${total_paid - initial_principal:>15,.3f}')
print(f'Average interest paid per year: {(total_paid - initial_principal)/(month/12):>15.2f}')
print(f'Interest to original loan ratio: {(total_paid - initial_principal)/initial_principal:15.2f}')