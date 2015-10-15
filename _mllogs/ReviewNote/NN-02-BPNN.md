# BP-NN #

- a fast matrix-based algorithm to compute the output from a neural network
- 2 assumptions of cost function
	+  均方误差 MSE 系数为什么有1/2 在GD计算中 求导后 正好2*1/2 将系数化为1 数学上的处理方便
	+  Cost Function 是 output `a`的函数 也就是 权值`w`与偏差bias`b`的函数
- BP
	+ an intermediate quantity: the error in the `j-th` neuron in the `l-th` layer 第l层 第j个神经元or节点处的误差 Backpropagation will give us a procedure to compute the error δlj



> Backpropagation is about understanding how changing the weights and biases in a network changes the cost function.