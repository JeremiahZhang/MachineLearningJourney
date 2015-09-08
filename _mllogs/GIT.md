# Learn Git #

- 1-version control
	- practice 
- 2-历史版本
	- 版本回退
- 3-设置版本标签
- 4-小技巧：设置alias
- 5-撤销本地修改(before staging)

## 1-Push a new local repo to Github ##

已经有一个origin repo了，现在新建一个新的local repo（用以记录机器学习的学习历程），然后推送到github上：

- 创建版本库
	- 在自己的电脑文件夹中新建了my machine learning journey的文件夹
	- 然后直接git init here
	- git init
	- 添加readme文件和机器学习的文件夹
- 远程仓库设置
	- creat a new repo
	- copy the SSH of the new repo
	- git add -a
	- git commit -m "add new repo"
	- git remote add learnml <my SSH clone URL add>
	- git push -u learnml master

----------

## 2-git 基础 ##

- working directory：工作区，本地目录，你可以对里面的文件进行操作
- staging area
- .git directory（Repository）

we need to know that：

- changes, not files
	- **Git works with changes, not files**. so when I modify the file in the working directory and git add this file，this modifier will be add to the staging area. After that I use the "git commit" to commit this change to repository.
	- SO use "git add" to track the changes, and then git commit to repo.
- **History** 历史
	- git log
	- git log --pretty=oneline: 用一行来显示git 快照下来的commit历史或版本历史
	- git reflog 
	- git log --pretty=oneline --max-count=2 : 显示最开始的两个
	- git log --pretty=oneline --since='5 minutes ago'
	- git log --pretty=oneline --until='5 minutes ago'
	- git log --pretty=oneline --author=<your name>
	- git log --pretty=oneline --all
	- git log --all --pretty=format:'%h %cd %s (%an)' --since='7 days ago'：查看最近一周的修改变化。”
	- git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short：以另一种显示方式来呈现
- **版本回退**
	- git log or git reflog
	- git reset --hard <使用git log or git reflog中的hash值 前7位就可以了> 
	- cat <filename> :来显示文件内容

> note 在unix 和mac os中版本回退的命令与window的是同的

----------

## 3-Tagging Version ##

- 给commit的版本贴个标签tag：**git tag v1**
- 使用tag name来check out 回退：**git checkout v1^**
- 查看使用的标签 **git tag**
- 查看标签列表 **git hist master --all**

> Learn how to tag commits with names for future reference

### 实践 ###

- 我新建了一个hello.md文件，并添加内容为【# Hello world】
- **git add** 之后
- **git commit** 之后
- **git tag v1**
- **git checkout v1^**
- **cat hello.md** 之后显示
 
		cat：hello.md: No such file or directory

> - 也就是说 git tag v1 是将commit的快照下的那个版本打上标签v1，便于以后回退
> - 那么 v1^ （或v1~1）是表示的是 v1上一个版本或上一代

- **git checkout v1** 之后
- **cat hello.md** 之后 我的文件又回来了，真的太棒了

		# Hello world

- git tag 查看所使用的 tag
- git hist master --all

> So cool, I can see the tag.

----------


## 4-小技巧 ##

- alias：修改git普通命令，使用别名在.gitconfig中修改如，使用起来更方便
	- co = checkout
  	- ci = commit
  	- st = status
  	- br = branch
  	- hist = log --pretty=oneline
  	- type = cat-file -t
  	- dump = cat-file -p
  	- rf = reflog

----------

## 5-撤销本地修改undoing local changes(before staging) ##

> - Learn how to revert changes in the working directory. 
> - 若我本地工作目录中修改了文件hello.md, 但是我并没有提交add 到缓存区中，更没有commit到远程库中，那么我该如何回退或撤销？

- 我在hello.md文件中添加了 
	-  I want to learn how to revert changes in the working directory.
 
				# Hello world

				- I want to learn how to revert changes in the working directory.
 
- 确定上一次的提交是在master上
	- git checkout master
	- 这个使用使得我之前commit的撤回了，回退到我上上会的版本处
		- 比如最近的版本是 v1
		- 使用上面的命令后，回到了上上个版本v1^处
- git status
	- 提示我修改了hello.md文件，但是没有add 和commit
- git checkout hello.md
- git status
- cat hello.md 之后就只剩下了如下内容，说明我撤销了最近一次的本地修改

		# Hello world


> It is so cool. I love Git.

