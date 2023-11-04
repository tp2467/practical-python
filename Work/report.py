# Create a report for a portfolio of stocks.

import sys
sys.path.append('/home/thinh/Documents/practical-python/Work')
import fileparse

def read_portfolio(filename: str) -> dict:
    '''Import a portfolio from filename and return a list of dictionaries
       Each dictionary has keys: 'name', 'shares', and 'price'.
    '''
    
    mainport = fileparse.parse_csv(
        filename=filename,
        types=[str, int, float]
    )    
    
    return mainport


def read_prices(filename: str) -> dict:
    '''
    Read prices from a file name, return a ditionary of stock names and 
    their prices.
    '''
    
    price_list = fileparse.parse_csv(
        filename=filename,
        types=[str, float],
        has_headers=False
    )
    price_dict = dict(price_list)
        
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
    portfolio_file = 'Data/portfolio.csv' 

if __name__ == '__main__':
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')