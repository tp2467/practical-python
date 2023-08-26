# Read the portfolio data and print out how much it cost to purchase all the stocks
# Also handles exceptions and sys.argv
# Exercise: 2.16 Use zip to parse corresponding columns

import csv
import sys

def portfolio_cost(filename):
    name = []
    price = []
    shares = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for linenum, line in enumerate(rows, start=1):
            record = dict(zip(header, line))
            try:
                name.append(record['name'])
                shares.append(int(record['shares']))
                price.append(float(record['price']))
            except ValueError:
                print(f"Row {linenum}: Couldn't convert: {line}")
                continue
    
    total_cost = 0
    for i in range(len(shares)):
        total_cost += shares[i]*price[i]

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

if __name__ == '__main__':
    print('Test case 1:')
    total_cost1 = portfolio_cost(filename)
    print('Total cost 1', total_cost1)
    print()
    
    print('Test case 2:')
    total_cost2 = portfolio_cost('Data/missing.csv')
    print('Total cost 2', total_cost2)
