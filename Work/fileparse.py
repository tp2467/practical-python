# fileparse.py
#
# Exercise 3.3 - 3.7

import csv

def parse_csv(filename,
              select=None, 
              types=None, 
              has_headers=True,
              delimiter=',',
              silence_errors=False):
    '''
    Parse a csv file into a list of records
    '''
    if select is not None and has_headers == False:
        print('select argument requires column headers')
        raise RuntimeError('select argument requires column headers')

    def process_rows_no_header(rows):
        '''
        Process rows from file without any header
        Return a list of n-tuples. Types of the items in each tuple must match
        the order of the types argument in function.
        '''
        
        records = []
        for index, row in enumerate(rows):
            if not row : continue
            try:
                casted_row = tuple([func(val) for func, val in zip(types, row)])
                records.append(casted_row)
            except ValueError as e:
                if silence_errors == True: continue
                print(f"Row {index}: cannot convert {str(row)} ")
                print(e)
                continue

        return records
        
    
    def process_row_w_header(rows):
        '''
        Process rows from file with first line as a header.
        Return a list of dictionary with keys as the header items.
        '''
        headers = next(rows)
        records = []

        col_index = range(len(headers))
        if select is not None:
            col_index = []
            for i, col in enumerate(headers):
                if col in select: col_index.append(i)
        
        filtered_headers = [headers[i] for i in col_index]
        for index, row in enumerate(rows):
            if not row: continue
            if types:
                try:
                    filtered_row = [func(row[i]) for i, func in zip(col_index, types)]
                except ValueError as e:
                    if silence_errors == True: continue
                    print(f"Row {index}: cannot convert {str(row)} ")
                    print(e)
                    continue
            else:
                filtered_row = [row[i] for i in col_index]
            
            record = dict(zip(filtered_headers, filtered_row))
            records.append(record)

        return records
    

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            return process_row_w_header(rows)
        elif not has_headers:
            return process_rows_no_header(rows)        