# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None):
    '''
    Parse a csv file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        headers = next(rows)
        records = []

        col_index = range(len(headers))
        if select is not None:
            col_index = []
            for i, col in enumerate(headers):
                if col in select: col_index.append(i)
        
        for row in rows:
            if not row: continue
            record = dict(zip([headers[i] for i in col_index ], [row[i] for i in col_index ]))
            records.append(record)

    return records