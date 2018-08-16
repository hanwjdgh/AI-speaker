from train import Train
from test import Test
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

    tr = Train(word_dic)
    tr.preprocess()
    tf.reset_default_graph() 

    input_str = input()
    temp_str = tr.sen2vec(input_str)

    ts = Test(word_dic)
    hyper,var = ts.test(temp_str)
    print(hyper)
    print(var)
    print(Functions.__dict__[categories[var[0]]]("test"))