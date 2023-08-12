# report.py
#
# Exercise 2.4

import csv

# def read_portfolio(filename):
#     '''Import a portfolio from filename and return a list of holdings
#        Exercise 2_4
#     '''

#     with open(filename) as f:
#         rows = csv.reader(f)
#         next(rows)
#         mainport = []
#         for row in rows:
#             stock, nshare, price = row[0], int(row[1]), float(row[2].strip())
#             mainport.append((stock, nshare, price))
    
#     return mainport

def read_portfolio(filename):
    '''Import a portfolio from filename and return a dictionary of holdings
       Exercise 2_5
    '''

    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        mainport = []
        for row in rows:
            stock, nshare, price = row[0], int(row[1]), float(row[2].strip())
            mainport.append({
                'name':stock,
                'shares':nshare,
                'price':price}
                )  
    
    return mainport


def read_prices(filename):
    with open(filename, 'rt') as pricefile:
        rows = csv.reader(pricefile)
    
        price_dict = {}
        for row in rows:
            if len(row) == 0: continue
            price_dict[row[0]] = float(row[1])
        
    return price_dict

if __name__ == '__main__':
    from pprint import pprint
    myport = read_portfolio('Data/portfolio.csv')
    currentprices = read_prices('Data/prices.csv')

    print('My portfolio:')
    pprint(myport)
    print()
    print('Current prices')
    pprint(currentprices)

    gainloss = 0
    for holding in myport:
        gainloss += holding['shares'] * (currentprices[holding['name']] - holding['price'])
    
    


    print()
    print('Current gain/loss: ', gainloss)


