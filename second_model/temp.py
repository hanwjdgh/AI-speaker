import train as train
import test as test
import tensorflow as tf
from function import Functions

categories = ['off_light','on_light','time','weather']

if __name__ == '__main__':
    train.train()  
    tf.reset_default_graph() 
    var = test.test()[0]
    print('predition {}'.format(var[0]))
    print(Functions.__dict__[categories[var[0]]]("test"))