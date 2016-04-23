## load csv

在ipython如何查看python文档or查询，比如我要查open直接在ipyhon中

	help
	io.open

进入：

	    Character Meaning
	    --------- ---------------------------------------------------------------
	    'r'       open for reading (default)
	    'w'       open for writing, truncating the file first
	    'a'       open for writing, appending to the end of the file if it exists
	    'b'       binary mode
	    't'       text mode (default)
	    '+'       open a disk file for updating (reading and writing)
	    'U'       universal newline mode (for backwards compatibility; unneeded
	              for new code)

以上将要省略一些。

之前我只知道

	help(open)

但显示内容不够完全。

## Load ML data

### Load CSV 前注意

1. file header 是否存在
2. comment # ...
3. delimiter 分隔符问题
4. Quotes .like ""

### Pima Data CSV file 

goo.gl/vhm1eu

1. 保存为csv
2. 在ipython中

#### 1`Python Standard Library` # Load CSV

	In [1]: import csv
	
	In [2]: import numpy
	
	In [3]: filename = 'pima-indians-diabetes.data.csv'
	
	In [4]: raw_data = open(filename, 'rb')
	
	In [5]: reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
	
	In [6]: x = list(reader)
	
	In [7]: data = numpy.array(x).astype('float')
	
	In [8]: print(data.shape)
	(768, 9)

#### 2`load CSV files with Numpy` 

	In [13]: import numpy
	
	In [14]: filename = 'pima-indians-diabetes.data.csv'
	
	In [15]: raw_data = open(filename, 'rb')
	
	In [16]: data = numpy.loadtxt(raw_data, delimiter=",")
	
	In [19]: print(data.shape)
	(768, 9)

也可以使用url直接

	import urllib
	
	In [22]: url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
	
	In [23]: raw_data = urllib.urlopen(url)

	In [37]: data = numpy.loadtxt(raw_data, delimiter=',')

	In [38]: print(data.shape)
	(768, 9)

【注】：后来才发现
在CH内外网可能不行，除非。。。你懂的

#### 3 Load CSV data use Pandas.read_csv()

	In [26]: import pandas
	 
	In [27]: filename = 'pima-indians-diabetes.data.csv'
	
	In [28]: names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] #对应9种特征
	
	In [29]: data = pandas.read_csv(filename, names=names)
	
	In [30]: print(data.shape)
	(768, 9)

也可以直接使用 url

	In [32]: url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
	
	In [34]: url_data = pandas.read_csv(url, names=names)
	
	In [35]: print(data.shape)
	(768, 9)
	
直接使用pandas会更加方便a！

Tuesday, 12. April 2016 09:31PM ~~~~
