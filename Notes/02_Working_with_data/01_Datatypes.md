# 2.1 Datatypes and Data structures

This section introduces data structures in the form of tuples and dicts.

### Primitive Datatypes

Python has a few primitive types of data:

* Integers
* Floating point numbers
* Strings (text)

We have learned about these in the previous section.

### None type

```python
email_address = None
```

This type is often used as a placeholder for optional or missing value.

```python
if email_address:
    send_email(email_address, msg)
```

### Data Structures

Real programs have more complex data than the ones that can be easily represented by the datatypes learned so far.
For example information about a stock:

```code
100 shares of GOOG at $490.10
```

This is an "object" with three parts:

* Name or symbol of the stock ("GOOG", a string)
* Number of shares (100, an integer)
* Price (490.10 a float)

### Tuples

A tuple is a collection of values grouped together.

Example:

```python
s = ('GOOG', 100, 490.1)
```

Sometimes the `()` are ommitted in the syntax.

```python
s = 'GOOG', 100, 490.1
```

Special cases (0-tuple, 1-typle).

```python
t = ()            # An empty tuple
w = ('GOOG', )    # A 1-item tuple
```

Tuples are usually used to represent *simple* records or structures.
Typically, it is a single *object* of multiple parts. A good analogy: *A tuple is like a single row in a database table.*

Tuple contents are ordered (like an array).

```python
s = ('GOOG', 100, 490.1)
name = s[0]                 # 'GOOG'
shares = s[1]               # 100
price = s[2]                # 490.1
```

However, th contents can't be modified.

```pycon
>>> s[1] = 75
TypeError: object does not support item assignment
```

You can, however, make a new tuple based on a current tuple.

```python
s = (s[0], 75, s[2])
```

### Tuple Packing

Tuples are focused more on packing related items together into a single *entity*.

```python
s = ('GOOG', 100, 490.1)
```

The tuple is then easy to pass around to other parts of a program as a single object.

### Tuple Unpacking

To use the tuple elsewhere, you can unpack its parts into variables.

```python
name, shares, price = s
print('Cost', shares * price)
```

The number of variables must match the tuple structure.

```python
name, shares = s     # ERROR
Traceback (most recent call last):
...
ValueError: too many values to unpack
```

### Tuples vs. Lists

Tuples are NOT just read-only lists. Tuples are most ofter used for a *single item* consisting of multiple parts.
Lists are usually a collection of distinct items, usually all of the same type.

```python
record = ('GOOG', 100, 490.1)       # A tuple representing a stock in a portfolio

symbols = [ 'GOOG', 'AAPL', 'IBM' ]  # A List representing three stock symbols
```

### Dictionaries

A dictionary is a hash table or associative array.
It is a collection of values indexed by *keys*. These keys serve as field names.

```python
s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
```

### Common operations

To read values from a dictionary use the key names.

```pycon
>>> print(s['name'], s['shares'])
GOOG 100
>>> s['price']
490.10
>>>
```

To add or modify values assign using the key names.

```pycon
>>> s['shares'] = 75
>>> s['date'] = '6/6/2007'
>>>
```

To delete a value use the `del` statement.

```pycon
>>> del s['date']
>>>
```

### Why dictionaries?

Dictionaries are useful when there are *many* different values and those values
might be modified or manipulated.  Dictionaries make your code more readable.

```python
s['price']
# vs
s[2]
```

## Exercises

### Note

In the last few exercises, you wrote a program that read a datafile `Data/portfolio.csv`. Using the `csv` module, it is easy to read the file row-by-row.

```pycon
>>> import csv
>>> f = open('Data/portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name', 'shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Although reading the file is easy, you often want to do more with the data than read it. 
For instance, perhaps you want to store it and start performing some calculations on it. 
Unfortunately, a raw "row" of data doesn’t give you enough to work with. For example, even a simple math calculation doesn’t work:

```pycon
>>> row = ['AA', '100', '32.20']
>>> cost = row[1] * row[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
```

To do more, you typically want to interpret the raw data in some way and turn it into a more useful kind of object so that you can work with it later.
Two simple options are tuples or dictionaries.

### (a) Tuples

At the interactive prompt, create the following tuple that represents
the above row, but with the numeric columns converted to proper
numbers:

```pycon
>>> t = (row[0], int(row[1]), float(row[2]))
>>> t
('AA', 100, 32.2)
>>>
```

Using this, you can now calculate the total cost by multiplying the shares and the price:

```pycon
>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>>
```

Is math broken in Python? What’s the deal with the answer of
3220.0000000000005?  

This is an artifact of the floating point hardware on your computer
only being able to accurately represent decimals in Base-2, not
Base-10.  For even simple calculations involving base-10 decimals,
small errors are introduced. This is normal, although perhaps a bit
surprising if you haven’t seen it before.

This happens in all programming languages that use floating point
decimals, but it often gets hidden when printing. For example:

```pycon
>>> print(f'{cost:0.2f}')
3220.00
>>>
```

Tuples are read-only. Verify this by trying to change the number of shares to 75.

```pycon
>>> t[1] = 75
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

Although you can’t change tuple contents, you can always create a completely new tuple that replaces the old one.

```pycon
>>> t = (t[0], 75, t[2])
>>> t
('AA', 75, 32.2)
>>>
```

Whenever you reassign an existing variable name like this, the old
value is discarded.  Although the above assignment might look like you
are modifying the tuple, you are actually creating a new tuple and
throwing the old one away.

Tuples are often used to pack and unpack values into variables. Try the following:

```pycon
>>> name, shares, price = t
>>> name
'AA'
>>> shares
75
>>> price
32.2
>>>
```

Take the above variables and pack them back into a tuple

```pycon
>>> t = (name, 2*shares, price)
>>> t
('AA', 150, 32.2)
>>>
```

### (b) Dictionaries as a data structure

An alternative to a tuple is to create a dictionary instead.

```pycon
>>> d = {
        'name' : row[0],
        'shares' : int(row[1]),
        'price'  : float(row[2])
    }
>>> d
{'name': 'AA', 'shares': 100, 'price': 32.2 }
>>>
```

Calculate the total cost of this holding:

```pycon
>>> cost = d['shares'] * d['price']
>>> cost
3220.0000000000005
>>>
```

Compare this example with the same calculation involving tuples above. Change the number of shares to 75.

```pycon
>>> d['shares'] = 75
>>> d
{'name': 'AA', 'shares': 75, 'price': 75}
>>>
```

Unlike tuples, dictionaries can be freely modified. Add some attributes:

```pycon
>>> d['date'] = (6, 11, 2007)
>>> d['account'] = 12345
>>> d
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
>>>
```

### (c) Some additional dictionary operations

If you turn a dictionary into a list, you’ll get all of its keys:

```pycon
>>> list(d)
['name', 'shares', 'price', 'date', 'account']
>>>
```

Similarly, if you use the `for` statement to iterate on a dictionary, you will get the keys:

```pycon
>>> for k in d:
        print('k =', k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

Try this variant that performs a lookup at the same time:

```pycon
>>> for k in d:
        print(k, '=', d[k])

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
account = 12345
>>>
```

You can also obtain all of the keys using the `keys()` method:

```pycon
>>> keys = d.keys()
>>> keys
dict_keys(['name', 'shares', 'price', 'date', 'account'])
>>>
```

`keys()` is a bit unusual in that it returns a special `dict_keys` object.

This is an overlay on the original dictionary that always gives you the current keys—even if the dictionary changes. For example, try this:

```pycon
>>> del d['account']
>>> keys
dict_keys(['name', 'shares', 'price', 'date'])
>>>
```

Carefully notice that the `'account'` disappeared from `keys` even though you didn’t call `d.keys()` again.

A more elegant way to work with keys and values together is to use the `items()` method. This gives you `(key, value)` tuples:

```pycon
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
```

If you have tuples such as `items`, you can create a dictionary using the `dict()` function. Try it:

```pycon
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
>>>
```

[Next](02_Containers)