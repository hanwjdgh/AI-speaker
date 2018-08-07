import tensorflow as tf
import numpy as np
import glob, os
import model as model

def test():
    x_data = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    Model = model.model()

    saver = tf.train.Saver()
    save_file = './save/model.ckpt'
    with tf.Session() as sess:

        #sess.run(tf.global_variables_initializer())
        saver.restore(sess, save_file) 
        prediction = sess.run([Model.prediction],feed_dict={Model.X: x_data})

    return prediction