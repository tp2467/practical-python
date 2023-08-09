# Read the portfolio data and print out how much it cost to purchase all the stocks
# Also handles exceptions
# Exercise: 1.32, 

import csv
def portfolio_cost(filename):
    name = []
    price = []
    shares = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for line in rows:
            try:
                name.append(line[0])
                shares.append(int(line[1]))
                price.append(float(line[2]))
            except ValueError:
                print('Warning: cannot convert shares or price.')
                break
    
    total_cost = 0
    for i in range(len(shares)):
        total_cost += shares[i]*price[i]

    return total_cost

if __name__ == '__main__':
    print('Test case 1:')
    total_cost1 = portfolio_cost('Data/portfolio.csv')
    print('Total cost 1', total_cost1)
    print()
    
    print('Test case 2:')
    total_cost2 = portfolio_cost('Data/missing.csv')
    print('Total cost 2', total_cost2)
