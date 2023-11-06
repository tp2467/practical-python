# Read the portfolio data and print out how much it cost to purchase all 
# the stocks

import csv
import sys
sys.path.append('/home/thinh/Documents/practical-python/Work')
import report

def calculate_portfolio_cost(portfolio_file_path):
    portfolio = report.read_portfolio(portfolio_file_path)
    
    total_cost = sum([int(stock['shares']) * float(stock['price']) for stock in portfolio ])
    
    return total_cost

if len(sys.argv) == 2:
    portfolio_file_path = sys.argv[1]
else:
    portfolio_file_path = 'Data/portfolio.csv'

if __name__ == '__main__':
    print('Test case 1:')
    total_cost1 = calculate_portfolio_cost(portfolio_file_path)
    print('Total cost 1', total_cost1)
    print()
    
    print('Test case 2:')
    total_cost2 = calculate_portfolio_cost('Data/portfoliodate.csv')
    print('Total cost 2', total_cost2)
