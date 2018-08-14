import new_train as train
import test as test
import tensorflow as tf
from function import Functions

categories = ['off_light','on_light','time','weather']

word_dic={}


def readDic():
    f = open("dictionary.txt","r")
    
    while True:
        line = f.readline()
        if not line:
            break
        if not line.split()[0] in word_dic:
            word_dic[line.split()[0]] = 0
    f.close()

if __name__ == '__main__':
    readDic()
    train.train(word_dic)  
    #tf.reset_default_graph() 

    #input_str = input()
    
