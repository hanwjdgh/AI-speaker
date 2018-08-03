import tensorflow as tf
import numpy as np

class model:
    def __init__(self):
        self.nb_classes = 4  
        self.X = tf.placeholder(tf.float32, [None, 31])
        self.Y = tf.placeholder(tf.int32, [None, 1])  

        self.Y_one_hot = tf.one_hot(self.Y, self.nb_classes)  
        self.Y_one_hot = tf.reshape(self.Y_one_hot, [-1, self.nb_classes])

        self.W = tf.Variable(tf.random_normal([31, self.nb_classes]), name='weight')
        self.b = tf.Variable(tf.random_normal([self.nb_classes]), name='bias')

        self.logits = tf.matmul(self.X, self.W) + self.b
        self.hypothesis = tf.nn.softmax(self.logits)
        self.cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=self.logits,
                                                        labels=self.Y_one_hot)
        self.cost = tf.reduce_mean(self.cost_i)
        self.optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(self.cost)
        self.prediction = tf.argmax(self.hypothesis, 1)

        self.correct_prediction = tf.equal(self.prediction, tf.argmax(self.Y_one_hot, 1))
        self.accuracy = tf.reduce_mean(tf.cast(self.correct_prediction, tf.float32))