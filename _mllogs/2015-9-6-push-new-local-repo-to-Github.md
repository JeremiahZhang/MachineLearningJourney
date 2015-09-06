# Push a new local repo to Github #

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