import tensorflow as tf
import numpy as np
import glob, os
import model as model
from konlpy.tag import Komoran

class Train:
    def __init__(self,dic):
        self.word_dic = dic
        self.komoran = Komoran()
        self.Model = model.model(len(self.word_dic))

    def sen2vec(self,sen):  
        self.word_dic = self.word_dic.fromkeys(self.word_dic, 0)
        lst=[]
        for val in self.komoran.pos(sen):
            if val[0] in self.word_dic:
                self.word_dic[val[0]]+=1
        for value in self.word_dic.values():
            lst.append(value)
        return lst

    def preprocess(self):
        cnt=0
        x_data = []
        y_data = []
        files = glob.glob("./trainData/*.txt",recursive=True)
        for file_name in files:
            basename = os.path.basename(file_name)
            categorty = basename.split(".")[0]

            i_file = open(file_name,"r",encoding="utf-8")
            while True:             
                text = i_file.readline()
                if not text: 
                    break
                if len(text) > 1:
                    lst = [cnt]
                    y_data.append(lst)
                    temp = text[:-1]
                    x_data.append(self.sen2vec(temp))
            i_file.close()
            cnt+=1

        self.train(x_data,y_data)

    def train(self,x_lst,y_lst):
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())

            for step in range(2000):
                sess.run(self.Model.optimizer, feed_dict={self.Model.X: x_lst, self.Model.Y: y_lst})
                if step % 100 == 0:
                    loss, acc = sess.run([self.Model.cost, self.Model.accuracy], feed_dict={
                                        self.Model.X: x_lst, self.Model.Y: y_lst})
                    print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(step, loss, acc))
                if step == 1999:
                    saver = tf.train.Saver()
                    save_file = './save/model.ckpt'
                    saver.save(sess, save_file)