# chapter 1

- running the ipython console
- using ipython as s system shell
- using the history
- Tab convenient
- executing a script with the `%run`
- `%timeit` 测试时间
- `%debug` to debug and `%pdb` 打开IPython debug 功能
- `%pylab`
- IPython notebook
- customing IPython

## hacking

	In [1]: %run script.py
	ERROR: File `u'script.py'` not found.
	
	In [2]: %pushd ipython hacking
	/home/jeremiahzhang/MachineLearningJourney/ipython hacking
	Out[2]: [u'~/MachineLearningJourney']
	
	In [3]: %run script.py
	Running script.
	'x' is now equal to 12.
	
	In [4]: x
	Out[4]: 12
	
	In [5]: %timeit [x*x for x in range(100000)]
	10 loops, best of 3: 22.5 ms per loop
	
	In [6]: %
	Display all 105 possibilities? (y or n)
	%%!                      %%time                   %hist                    %pastebin                %reload_ext
	%%HTML                   %%timeit                 %history                 %pdb                     %rep
	%%SVG                    %%writefile              %install_default_config  %pdef                    %rerun
	%%bash                   %alias                   %install_ext             %pdoc                    %reset
	%%capture                %alias_magic             %install_profiles        %pfile                   %reset_selective
	%%debug                  %autocall                %killbgscripts           %pinfo                   %run
	%%file                   %autoindent              %load                    %pinfo2                  %save
	%%html                   %automagic               %load_ext                %popd                    %sc
	%%javascript             %bookmark                %loadpy                  %pprint                  %store
	%%latex                  %cd                      %logoff                  %precision               %sx
	%%perl                   %colors                  %logon                   %profile                 %system
	%%prun                   %config                  %logstart                %prun                    %tb
	%%pypy                   %cpaste                  %logstate                %psearch                 %time
	%%python                 %debug                   %logstop                 %psource                 %timeit
	%%python3                %dhist                   %lsmagic                 %pushd                   %unalias
	%%ruby                   %dirs                    %macro                   %pwd                     %unload_ext
	%%script                 %doctest_mode            %magic                   %pycat                   %who
	%%sh                     %ed                      %matplotlib              %pylab                   %who_ls
	%%svg                    %edit                    %notebook                %quickref                %whos
	%%sx                     %env                     %page                    %recall                  %xdel
	%%system                 %gui                     %paste                   %rehashx                 %xmode
	
	In [6]: %quickref
	
	In [7]: %debug
	ERROR: No traceback has been produced, nothing to debug.
	
	In [8]: %pdb
	Automatic pdb calling has been turned ON
	
	In [9]: %pylab
	Using matplotlib backend: TkAgg
	Populating the interactive namespace from numpy and matplotlib
	
	In [10]: x = linspace(-10,10,1000)
	
	In [11]: plot(x, sin(x))
	Out[11]: [<matplotlib.lines.Line2D at 0xb375450c>]
	
	In [12]: ipython notebook
	  File "<ipython-input-12-c5fb5fabe56c>", line 1
	    ipython notebook
	                   ^
	SyntaxError: invalid syntax

if you want to see the history you can use `%quickref` to see the command, you can see lines in it, just like this below:qq

	_i, _ii, _iii    : Previous, next previous, next next previous input
	_i4, _ih[2:5]    : Input history line 4, lines 2-4
	exec _i81        : Execute input history line #81 again
	%rep 81          : Edit input history line #81
	_, __, ___       : previous, next previous, next next previous output
	_dh              : Directory history
	_oh              : Output history
	%hist            : Command history. '%hist -g foo' search history for 'foo'

## IPython Notebook

when I type `ipython notebook' in my console, it appaers:

	❯ ipython notebook   
	2016-04-24 14:48:18.255 [NotebookApp] Using existing profile dir: u'/home/jeremiahzhang/.config/ipython/profile_default'
	2016-04-24 14:48:18.293 [NotebookApp] Using system MathJax
	2016-04-24 14:48:18.373 [NotebookApp] Serving notebooks from local directory: /home/jeremiahzhang/MachineLearningJourney
	2016-04-24 14:48:18.373 [NotebookApp] The IPython Notebook is running at: http://127.0.0.1:8888/
	2016-04-24 14:48:18.373 [NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

it open my firefox browser on the default port 8888. Go to http://127.0.0.1:8888/ in my browser and creat a new Notebook.

But i dont know how to use it.

- creat a new notebook
- type it just like ipython
- *Enter* 新建一行 但是在同一个 input[ ] 中
- *Shift + Enter* 执行命令

