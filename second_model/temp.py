import train as train
import test as test
import tensorflow as tf
from function import Functions

categories = ['off_light','on_light','time','weather']

input_list=[]

if __name__ == '__main__':
    train.train()  
    tf.reset_default_graph() 

    input_str = input()
    word_dic = train.getdiction() 

    temp = input_str.split(' ')
    tmp = []

    for var in temp:
        if var in word_dic:
            word_dic[var]+=1
    
    for value in word_dic.values():
        tmp.append(value)
    
    input_list.append(tmp)

    hyper,var = test.test(input_list)
    print(hyper)
    print('predition {}'.format(var[0]))
    print(Functions.__dict__[categories[var[0]]]("test"))