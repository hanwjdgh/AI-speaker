import tensorflow as tf
import numpy as np
import glob, os
import model as model

word_dic={}

def getdiction():
    return word_dic

def train():
    global word_dic
    x_data = []
    y_data = []

    cnt = 0
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
                temp = text[:-1].split(' ')
                for val in temp:
                    if(not val in word_dic):
                        word_dic[val] = 0
        i_file.close()
        cnt += 1

    for file_name in files:
        basename = os.path.basename(file_name)
        categorty = basename.split(".")[0]

        i_file = open(file_name,"r",encoding="utf-8")
        while True:
            word_dic = word_dic.fromkeys(word_dic, 0)
            text = i_file.readline()
            if not text: 
                break
            if len(text) > 1:
                temp = text[:-1].split(' ')
                for val in temp:
                    word_dic[val] += 1
                lst=[]
                for values in word_dic.values():
                    lst.append(values)
            x_data.append(lst)
        i_file.close()

    for i in range(len(x_data)):
        print(x_data[i],y_data[i])

    Model = model.model()

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for step in range(2000):
            sess.run(Model.optimizer, feed_dict={Model.X: x_data, Model.Y: y_data})
            if step % 100 == 0:
                loss, acc = sess.run([Model.cost, Model.accuracy], feed_dict={
                                    Model.X: x_data, Model.Y: y_data})
                print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(
                    step, loss, acc))
            if step == 1999:
                saver = tf.train.Saver()
                save_file = './save/model.ckpt'
                saver.save(sess, save_file)
        
        #pred = sess.run(prediction, feed_dict={X: x_data})
