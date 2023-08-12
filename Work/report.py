# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Import a portfolio from filename and return a list of holdings'''

    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        mainport = []
        for row in rows:
            stock, nshare, price = row[0], int(row[1]), float(row[2].strip())
            mainport.append((stock, nshare, price))
    
    return mainport


if __name__ == '__main__':
    myport = read_portfolio('Data/portfolio.csv')
    for holding in myport:
        print(holding)