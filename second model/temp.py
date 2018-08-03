import train as train
import test as test
import tensorflow as tf

if __name__ == '__main__':
    train.train()  
    tf.reset_default_graph() 
    test.test()