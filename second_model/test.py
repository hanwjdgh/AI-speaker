import tensorflow as tf
import numpy as np
import glob, os
import model as model

def test(x_data):
    Model = model.model()

    saver = tf.train.Saver()
    save_file = './save/model.ckpt'
    with tf.Session() as sess:
        #sess.run(tf.global_variables_initializer())
        saver.restore(sess, save_file) 
        hyper,prediction = sess.run([Model.hypothesis,Model.prediction],feed_dict={Model.X: x_data})
    
    return hyper,prediction