# Read the portfolio data and print out how much it cost to purchase all the stocks
# Also handles exceptions
# Exercise: 1.30, 1.31

def portfolio_cost(filename):
    name = []
    price = []
    shares = []
    with open(filename, 'rt') as f:
        header = next(f)
        for line in f:
            parts = line.strip().split(',')
            try:
                name.append(parts[0])
                shares.append(int(parts[1]))
                price.append(float(parts[2]))
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
