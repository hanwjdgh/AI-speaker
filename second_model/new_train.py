import numpy as np
import glob, os
import model as model

def train(word_dic):
    x_data = []
    y_data = []

    files = glob.glob("./ktrainData/*.txt",recursive=True)
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
                temp = text[:-1].split('/')
                print(temp)
       
        i_file.close()

    for i in range(len(x_data)):
        print(x_data[i],y_data[i])