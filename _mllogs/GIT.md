# Learn Git #

- version control

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

## git 基础 ##

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

> note 在unix 和mac os中版本回退的命令与window的是同的

----------


## 小技巧 ##

- alias：修改git普通命令，使用别名在.gitconfig中修改如，使用起来更方便
	- co = checkout
  	- ci = commit
  	- st = status
  	- br = branch
  	- hist = log --pretty=oneline
  	- type = cat-file -t
  	- dump = cat-file -p
  	- rf = reflog