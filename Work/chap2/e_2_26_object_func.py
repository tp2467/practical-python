import csv

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)

headers = next(rows)
row = next(rows)

def parse_date_string(date_string):
    int_func = [int]*3
    return tuple([func(val) for func, val in zip(int_func, date_string.split('/'))])


types = [str, float, parse_date_string, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))

print(record)





f.close()

