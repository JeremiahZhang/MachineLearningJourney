# D1 scipy Basic

- Numpy
- matplotlib
- pandas

## Numpy

### help function

[search help](http://docs.scipy.org/doc/numpy/reference/routines.help.html#routines-help) 

lookfor:注意是**关键词**搜索 Do a keyword search on docstrings

	# 在ipython中
	import numpy
	numpy.lookfor('binary representation') % just like google keywords search but on docstrings

info: 了解 **function**, **class** or **module** 的方法

	# 在ipython中
	import numpy
	numpy.info(numpy.array)

source: Print or write to a file the source code for a **Numpy object** 查看 numpy 对象

	numpy.source(numpy.interp)

Monday, 11. April 2016 07:29PM 

### Access Data

	In [1]: import numpy
	
	In [2]: np = numpy
	
	In [3]: mylist = [[1, 2, 3], [3, 4, 5]]
	
	In [4]: myarray = np.array(mylist)
	
	In [5]: print(myarray)
	[[1 2 3]
	 [3 4 5]]
	
	In [6]: print(myarray.shape)
	(2, 3)
	
	In [7]: print 'first row: {}'.format(myarray[0])
	first row: [1 2 3]
	
	In [8]: print 'last row:{}'.format(myarray[1])
	last row:[3 4 5]
	
	In [9]: print 'last row:{}'.format(myarray[-1])
	last row:[3 4 5]
	
	In [10]: print 'Specific row and col:{}'.format(myarray[0, 2]
	   ....: )
	Specific row and col:3
	
	In [12]: print 'Whole col:{}'.format(myarray[:,2])
	Whole col:[3 5]

可以看出和matlab矩阵类似
不过这里的数字计数是从0开始 就是和python中的一样

### Arithmetic

	In [15]: myarray1 = np.array([2, 2, 3])
	
	In [16]: myarray2 = np.array([3, 3, 3])
	
	In [17]: print 'Addition: {}'.format(myarray1 + myarray2)
	Addition: [5 5 6]
	
	In [18]: print 'Multiplication: {}'.format(myarray1 * myarray2)
	Multiplication: [6 6 9]
	
	In [19]: print 'divided: {}'.format(myarray1 / myarray2)
	divided: [0 0 1]

这个也还好，就是计小数需要另外设置。

like this:

	In [22]: array_division = np.true_divide(myarray1, myarray2)
	
	In [23]: print 'divided: {}'.format(array_division)
	divided: [ 0.6667  0.6667  1.    ]

refer to 

	http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.true_divide.html

可以直接在ipython中

	np.info(np.true_divide)

## matplotlib

- line plot
- scatter plot

### line plot

	In [1]: import matplotlib.pyplot as plt
	
	In [2]: import numpy as np
	
	In [4]: myarray = np.array([1, 2, 3])
	
	In [5]: plt.plot(myarray)
	Out[5]: [<matplotlib.lines.Line2D at 0xb3d0baec>]
	
	In [7]: plt.xlabel('some x axis')
	Out[7]: <matplotlib.text.Text at 0xb3d7d48c>
	
	In [8]: plt.ylabel('some y axis')
	Out[8]: <matplotlib.text.Text at 0xb3d8dc8c>
	
	In [9]: plt.show()

展示图片

### scatter plot

	In [10]: x = myarray
	
	In [11]: y = np.array([2, 4, 6])
	
	In [12]: plt.scatter(x,y)
	Out[12]: <matplotlib.collections.PathCollection at 0xb3806aac>
	
	In [13]: plt.xlabel('x axis')
	Out[13]: <matplotlib.text.Text at 0xb3ce702c>
	
	In [14]: plt.ylabel('y axis')
	Out[14]: <matplotlib.text.Text at 0xb3dd7f8c>
	
	In [15]: plt.show()

展示图片

## pandas

- Series 1维array， row 和 columns 和加标签
- DataFrame 多维的

### Series

	In [16]: import numpy as np
	
	In [17]: import pandas
	
	In [18]: myarray = np.array([1, 2, 3])
	
	In [19]: rownames = ['a', 'b', 'c']
	
	In [20]: myseries = pandas.Series(myarray, index=rownames)
	
	In [21]: print (myseries)
	a    1
	b    2
	c    3
	dtype: int32
	
	In [22]: print myseries
	a    1
	b    2
	c    3
	dtype: int32

就是配对呗 不过注意其类型

	In [23]: type(myseries)
	Out[23]: pandas.core.series.Series

	In [24]: print myseries[0]
	1
	
	In [25]: print myseries['a'] 
	1

和 dictionary 类似 可根据 index 来索引

	In [27]: dict = {'a': 1, 'b': 2, 'c': 3}
	
	In [29]: dict['a']
	Out[29]: 1

### DataFrame

	In [30]: myarray = np.array([[1, 2, 3], [4, 5, 6]])
	
	In [31]: rowname = ['rowa', 'rowb']
	
	In [32]: colname = ['one', 'two', 'three']
	
	In [34]: mydataframe = pandas.DataFrame(myarray, index=rowname, columns=colname)
	
	In [35]: print(mydataframe)
	      one  two  three
	rowa    1    2      3
	rowb    4    5      6
	
	[2 rows x 3 columns]

只可以用**列标签**索引

	In [36]: print 'one column:{}'.format(mydataframe['one'])
	one column:rowa    1
	rowb    4
	Name: one, dtype: int32
	
	In [37]: print 'one column:{}'.format(mydataframe.one)
	one column:rowa    1
	rowb    4
	Name: one, dtype: int32
	
	In [38]: print 'one column:{}'.format(mydataframe.two)
	one column:rowa    2
	rowb    5
	Name: two, dtype: int32
	
	In [39]: print 'one column:{}'.format(mydataframe.three)
	one column:rowa    3
	rowb    6
	Name: three, dtype: int32
	
	In [40]: print 'one row:{}'.format(mydataframe.rowa)
	---------------------------------------------------------------------------
	AttributeError                            Traceback (most recent call last)
	<ipython-input-40-796b4cce6065> in <module>()
	----> 1 print 'one row:{}'.format(mydataframe.rowa)
	
	/usr/lib/python2.7/dist-packages/pandas/core/generic.pyc in __getattr__(self, name)
	   1813                 return self[name]
	   1814             raise AttributeError("'%s' object has no attribute '%s'" %
	-> 1815                                  (type(self).__name__, name))
	   1816 
	   1817     def __setattr__(self, name, value):
	
	AttributeError: 'DataFrame' object has no attribute 'rowa'
	
	In [41]: print 'one row:{}'.format(mydataframe['rowa'])


