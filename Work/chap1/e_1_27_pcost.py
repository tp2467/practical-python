# Read the portfolio data and print out how much it cost to purchase all the stocks

name = []
price = []
shares = []
with open('Data/portfolio.csv', 'rt') as f:
    header = next(f)
    for line in f:
        parts = line.strip().split(',')
        name.append(parts[0])
        shares.append(int(parts[1]))
        price.append(float(parts[2]))

total_cost = 0
for i in range(len(shares)):
    total_cost += shares[i]*price[i]

print('Total cost', total_cost)

