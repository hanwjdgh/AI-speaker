import tensorflow as tf
import numpy as np
import glob, os
import model as model

def test():
    x_data = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    y_data = [[1]]

    Model = model.model()

    saver = tf.train.Saver()
    save_file = './save/model.ckpt'
    with tf.Session() as sess:

        #sess.run(tf.global_variables_initializer())
        saver.restore(sess, save_file) 
        test_accuracy = sess.run(Model.accuracy,feed_dict={Model.X: x_data, Model.Y: y_data})

    print('Test Accuracy: {}'.format(test_accuracy))