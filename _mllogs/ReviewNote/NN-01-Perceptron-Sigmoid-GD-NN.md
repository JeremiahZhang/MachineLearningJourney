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

- 学习
- 决策 

## 神经元 ##

- Perceptrons
- Sigmoid

处理需要神经元 ANN中的常见神经元为以上两种

Perceptron 感知器 比较简单 如图所示

![perceptrons](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-Perceptrons.JPG)
公式
![formula](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-formula1.JPG)

理解

- 每一个输入`x`都伴随着一个权重`w` 同时由一个阈值threshold来决定输出结果  
- 感知器神经元的`input` x 要么为0 要么为1 （二进制输入） 输出也是0 or 1
- 这可以用来做决策 yes(1) or no(0), life(1) or death(0)? etc
	- 例子 我目前在广州 2015年12月12日孙燕姿正好要在天河体育馆开一场演唱会 假如以感知器来模拟我要不要去
		- input 1 x1 现在喜欢孙燕姿么？ 权值 我对燕姿的喜欢程度 影响份量 w1 = 4
		- input 2 x2 天气好我就去 不好就不去？ 权值 w2 = 2
		- input 3 x3 地铁直达不？ 权值 w3 = 2
		- 阈值为 threshold = 3 
	- 通过公式计算 x1`*`w1 + x2`*`w2 + x3`*`w3 > or <= threshold
		- 只要我现在喜欢孙燕姿（不论天气好坏还是地铁直达与否）or（天气好+地铁直达）那么 我肯定会去了

嗯 以上就是简单的感知器神经元 神经网络的每个神经元若采用感知器神经元 那么每一次的output都是如公式2决定 以下为3层神经网络
![Perceptrons-NN](https://raw.githubusercontent.com/JeremiahZhang/MachineLearningJourney/master/_images/15-10-14-Perceptrons-NN.JPG)

其实也就是说 上面神经网络中每个神经元通过公式2来决定输出的情况 那么 公式2就可当作是激活神经元的一个函数(activation function)。

Sigmoid神经元与Perceptron神经元的区别就在于这个激活神经元的激活函数activation function