# 2_5_report.py
#
# Exercise 2.5

import csv

def read_portfolio(filename):
    '''Import a portfolio from filename and return a dictionary of holdings'''

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


if __name__ == '__main__':
    from pprint import pprint
    myport = read_portfolio('../Data/portfolio.csv')
    pprint(myport)