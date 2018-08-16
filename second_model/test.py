import tensorflow as tf
import numpy as np
import glob, os
import model as model

class Test:
    def __init__(self,word_dic):
        self.Model = model.model(len(word_dic))
        self.save_file = './save/model.ckpt'
        
    def test(self, x_data):
        saver = tf.train.Saver()
        with tf.Session() as sess:
            #sess.run(tf.global_variables_initializer())
            saver.restore(sess, self.save_file) 
            hyper, prediction = sess.run([self.Model.hypothesis,self.Model.prediction], feed_dict={ 
                self.Model.X: [x_data]})
        
        return hyper,prediction