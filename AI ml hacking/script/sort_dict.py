In [1]: numbers = {'first':1, 'second':2, 'third':3, 'Fourth':4}

In [2]: list(numbers)
Out[2]: ['second', 'Fourth', 'third', 'first']

In [3]: sorted(numbers)
Out[3]: ['Fourth', 'first', 'second', 'third']

In [4]: sorted(numbers.values())
Out[4]: [1, 2, 3, 4]

In [5]: sorted(numbers, key=numbers.__getitem__)
Out[5]: ['first', 'second', 'third', 'Fourth']

In [6]: sorted(numbers, key=numbers.__getitem__, reverse=True)
Out[6]: ['Fourth', 'third', 'second', 'first']

In [7]: [value for (key, value) in sorted(numbers.items())]
Out[7]: [4, 1, 2, 3]

In [8]: # sort numbers dict's keys by alphebet

In [9]: sorted(numbers, key=str.lower)
Out[9]: ['first', 'Fourth', 'second', 'third']