# report.py
#
# Exercise 2.4

import sys

def read_portfolio(filename: str) -> dict:
    '''Import a portfolio from filename and return a list of dictionaries
       Each dictionary has keys: 'name', 'shares', and 'price'.
    '''
    import csv
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        mainport = []
        
        for row in rows:
            record = dict(zip(header, row))
            stock = record['name']
            nshare = int(record['shares']) 
            price = float(record['price'].strip())
            mainport.append({'name':stock, 'shares':nshare, 'price':price})  
    
    return mainport


def read_prices(filename: str) -> dict:
    '''
    Read prices from a file name, return a ditionary of stock names and 
    their prices.
    '''
    import csv
    with open(filename, 'rt') as pricefile:
        rows = csv.reader(pricefile)
    
        price_dict = {}
        for row_num, row in enumerate(rows):
            if len(row) == 0: continue
            price_dict[row[0]] = float(row[1])
        
    return price_dict


def make_report(portfolio:list, prices:dict) ->list:
    '''
    Generate a list of the stock, number of shares, original price, and price 
    change of all stocks in the porfolio.
    Input:
        portfolio: list of dictionary of the form {'name':stock, 'shares':num_shares, 'price':price}  }
        price: dictionary of price of the form {'stock_symbol': price}
    '''
    
    report = []
    for holding in portfolio:
        price_change = prices[holding['name']] - holding['price']
        report.append(
            (holding['name'], 
             holding['shares'], 
             prices[holding['name']], 
             price_change
            )
        )
    
    return report


def print_report(report):
    '''
    Print out all positions and their cost and profit.
    Args
        report: list of tuples of holdings.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')

    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ' )*len(headers) )
    for record in report:
        print('%10s %10s %10.2f %10.2f' % record)


def portfolio_report(portfolio_filename, price_filename):
    portfolio = read_portfolio(portfolio_filename)
    price_list = read_prices(price_filename)
    report = make_report(portfolio, price_list)
    print_report(report)


if len(sys.argv) == 2:
    portfolio_file = sys.argv[1]
else:
    portfolio_file = '../Data/portfolio.csv' 

if __name__ == '__main__':
    portfolio_report('../Data/portfolio.csv', '../Data/prices.csv')