## sort dict

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

## sort list and tuple

In [1]: a = [3, 4, 5, 6, 8, 7, 2, 1]

In [2]: sort a list
  File "<ipython-input-2-40c822aa285c>", line 1
    sort a list
         ^
SyntaxError: invalid syntax


In [3]: a = [3, 4, 5, 6, 8, 7, 2, 1]

In [4]: # sort a list

In [5]: sorted(a)
Out[5]: [1, 2, 3, 4, 5, 6, 7, 8]

In [6]: a.sort()

In [7]: a
Out[7]: [1, 2, 3, 4, 5, 6, 7, 8]

In [8]: sorted(a, reverse=True)
Out[8]: [8, 7, 6, 5, 4, 3, 2, 1]

In [9]: # i can reverse it

In [10]: a.sort(reverse=True)

In [11]: a
Out[11]: [8, 7, 6, 5, 4, 3, 2, 1]

In [12]: # i see the diffference

In [13]: # a.sort() change list a

In [14]: tup = (1, 3, 2, 4, 9, 8)

In [15]: sorted(tup)
Out[15]: [1, 2, 3, 4, 8, 9]

In [16]: # return a list when sorted(tuple)

In [17]: # sort a list of List or tuples

In [18]: l = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]] 

In [19]: def getKey(item):
   ....:     return item[0]
   ....: end
   ....: 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-19-f39019caf0c0> in <module>()
      1 def getKey(item):
      2     return item[0]
----> 3 end
      4 

NameError: name 'end' is not defined

In [20]: def getKey(item):
   ....:     return item[0]
   ....: 

In [21]: sorted(l, key=getKey)
Out[21]: [[1, 43], [2, 3], [3, 34], [6, 7], [24, 64]]

In [22]: def getkey(item):
   ....:     return item[1]
   ....: 

In [23]: sorted(l, key=getkey)
Out[23]: [[2, 3], [6, 7], [3, 34], [1, 43], [24, 64]]

In [24]: a = [(2, 3), (6, 7), (3, 34), (24, 64), (1, 43)]

In [25]: sorted(a, key=getkey)
Out[25]: [(2, 3), (6, 7), (3, 34), (1, 43), (24, 64)]

In [26]: a = ((2, 3), (6, 7), (3, 34), (24, 64), (1, 43))

In [27]: sorted(a, key=getkey)
Out[27]: [(2, 3), (6, 7), (3, 34), (1, 43), (24, 64)]

## advanced

customize need to dive in later.

## reference

[How to sort a list, tuple](http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/)   
[How to Sort Python Dictionaries by Key or Value](http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/) 
