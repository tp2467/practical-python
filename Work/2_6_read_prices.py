import csv

def read_prices(filename):
    with open(filename, 'rt') as pricefile:
        rows = csv.reader(pricefile)
        next(rows)
    
        price_dict = {}
        for row in rows:
            if len(row) == 0: continue
            price_dict[row[0]] = float(row[1])
        
    return price_dict

if __name__ == '__main__':
    from pprint import pprint
    prices = read_prices('Data/prices.csv')
    pprint(prices)