# Read the portfolio data and print out how much it cost to purchase all the stocks
# Also handles exceptions and sys.argv
# Exercise: 2.16 Use zip to parse corresponding columns

import csv
import sys

def calculate_portfolio_cost(portfolio_file_path):
    stock_name = []
    stock_price = []
    shares = []
    with open(portfolio_file_path, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for line_num, line in enumerate(rows, start=1):
            record = dict(zip(header, line))
            try:
                stock_name.append(record['name'])
                stock_price.append(float(record['price']))
                shares.append(int(record['shares']))
            except ValueError:
                print(f"Row {line_num}: Couldn't convert: {line}")
                continue
    
    total_cost = sum_product_shares_and_prices(shares, stock_price)

    return total_cost

def sum_product_shares_and_prices(shares, stock_prices):
    total_portfolio_cost = 0.0
    for share_num, price in zip(shares, stock_prices):
        total_portfolio_cost += share_num*price
    return total_portfolio_cost

if len(sys.argv) == 2:
    portfolio_file_path = sys.argv[1]
else:
    portfolio_file_path = '../Data/portfolio.csv'

if __name__ == '__main__':
    print('Test case 1:')
    total_cost1 = calculate_portfolio_cost(portfolio_file_path)
    print('Total cost 1', total_cost1)
    print()
    
    print('Test case 2:')
    total_cost2 = calculate_portfolio_cost('../Data/portfoliodate.csv')
    print('Total cost 2', total_cost2)
