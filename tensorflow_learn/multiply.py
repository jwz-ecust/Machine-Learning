import tensorflow as tf
import numpy as np

# a = tf.placeholder('float')
# b = tf.placeholder('float')
#
# y = tf.mul(a, b)
#
# sess = tf.Session()
#
# print sess.run(y, feed_dict={a: [1, 2, 3], b: [3, 2, 1]})
# print "%f should equal 9.0" % sess.run(y, feed_dict={a: 3, b: 3})


trX = np.linspace(-1, 1, 101)
trY = 2 * trX + np.random.randn(*trX.shape)

X = tf.placeholder('float')
Y = tf.placeholder('float')


w = tf.Variable(0.0, name="weights")
y_model = tf.mul(X, w)


cost = tf.pow((y_model - Y), 2)

train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)


for i in range(10000):
    for (x, y) in zip(trX, trY):
        sess.run(train, feed_dict={X: x, Y: y})

print sess.run(w)[]
