# Example use of `make_table_str`

The function `make_table_str` takes in a dict of data and creates a table of the
data, as a string. Notice that columns are separated by two spaces.

```python
>>> data = {"colA": [1, 2, 3], "colB": [10, 20, 30]}
>>> table = make_table_str(data)
>>> print(table)
```
```out
colA  colB
----------
1     10  
2     20  
3     30  
```

The width of the columns should be wide enough to contain the column headers:

```python
>>> data = {"colAAAAA": [1, 2, 3], "colB": [10, 20, 30]}
>>> table = make_table_str(data)
>>> print(table)
```
```out
colAAAAA  colB
--------------
1         10  
2         20  
3         30  
```

The width of the columns should also be wide enough to contain the main table
entries:

```python
>>> data = {
... "colA": [1, 2, 3],
... "colB": ["foo", "barrrrrrr", "baz"],
... "colC": [10, 20, 30]
... }
>>> table = make_table_str(data)
>>> print(table)
```
```out
colA  colB       colC
---------------------
1     foo        10  
2     barrrrrrr  20  
3     baz        30  
```
