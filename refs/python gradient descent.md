# Python实现梯度下降法

url：http://www.pyimagesearch.com/2016/10/10/gradient-descent-with-python/

by AdrianRosebroc on October 10, 2016 in Deep Learning, Machine Learning, Tutorials

![gradient_descent_header](http://www.pyimagesearch.com/wp-content/uploads/2016/10/gradient_descent_header.jpg)



每种关系都是基于爱，信任，相互尊重而建立的.

**昨天，我像爱情长跑7.5年的女友求婚. 她答应了.**

这是我这辈子最快乐的时候，我感觉我是世界上最幸福的人，不仅仅因为她，还因为PyImageSearch社区长达三年的支持. 感谢你们的一路陪伴！



**和爱情婚姻一样， 机器学习和神经网络分类也有它的构建基础.**

​	在过去的几周里，我们对机器学习和神经网络中的线性分类进行了介绍， 讨论了参数学习的概念以及这种学习类型如何定义一种得分函数（从输入数据到输出类标签的映射）.

​	得分函数的参数：权重参数 W 和 基向量 b.它接受这些参数作为输入，对每一个输入点x<sub>i</sub>返回一个预测的类标签.

​	这里，我们主要讨论两种常见的损失函数：多类支持向量机损失和交叉熵损失（和Softmax分类器相比恰恰相反. 从根本上来讲，损失函数是用来衡量对给定测试集数据(比如 一组参数)预测(对数据集数据分类)的好坏.
​	以上，我们于是可以去关注机器学习,神经网络和深度学习最重要的概念-优化.
	通过这次讨论, 我们已经知道了高的分类精确度取决于找到一组合适的权重W,数据才能正确的分类. 对于给定的W,通过得分函数来计算输出类. 最终, 我们才能通过损失函数得知对给定的W我们分类的好坏.
	**但是我们如何着手找到包含高分类精度的权重矩阵W?**
	如果随机初始化W, 评估, 然后不断重复下去. 这样能得到某个点找到有最合适分类进度的W吗?	这样其实有可能会奏效. 但是大多数情况下, 我们取而代之的是: 定义一个优化算法, 不断的迭代下去优化权重矩阵W.
	这篇博客, 我将批判地看待最常用寻找最优W的算法-梯度下降法.

##梯度下降法与Python
梯度瞎讲算法来源于
1.标准的"vanilla 实现
2.



---

in the same breath    means:  

if you say two things in the same breath, you say two things that are so different that if one is true, the other must be false.

---





































