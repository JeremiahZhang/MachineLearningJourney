# Using neural nets to recognize handwritten digits #

[学习章节](http://neuralnetworksanddeeplearning.com/chap1.html)

- 神经元
	- Perceptrons
	- Sigmoid Neurons
- 神经网络结构
- 神经网络学习 
	+ gradient descent
		+ Stochastic GD Applied in recognition
		+ Batch GD 

----------
## 神经网路 ##

- 什么是[人工神经网络](https://en.wikipedia.org/wiki/Artificial_neural_network)(artificial neural network，缩写ANN)？
- 它是用来干什么的？
- 如何使用它？

人工神经网络模拟人脑的神经网络 但是大大的简化了 所以称之为人工神经网络

来看看人脑神经网络

![NN-1](https://ilaif.files.wordpress.com/2015/02/neural-network.jpg)

简化

![NN-2](http://1.bp.blogspot.com/-ewmhj_UedLs/VEIhLPJsRkI/AAAAAAAAAAs/PGuuX9wn1mg/s1600/neuron.png)

ANN是用来干嘛的？

人类大脑可以处理负责的事物 我日常学习 做决策需要神经元的作用 有时 我做的决策比较好 有时不然 那么ANN模拟人脑 也可以进行“学习” “决策”
虽然达不到人类的效果 但是可以辅助人 

## 神经元 ##

