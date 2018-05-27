import glob,os
from bayes import BayesianFilter

class Train:
    def __init__(self):
        self.bf = BayesianFilter()
        self.files = glob.glob("./trainData/*.txt",recursive=True)
    
    def train_data(self):
        for file_name in self.files:
            basename = os.path.basename(file_name)
            categorty = basename.split(".")[0]
            file = open(file_name,"r",encoding="utf-8")

            while True:
                text = file.readline()
                self.bf.fit(text,categorty)
                if not text: 
                    break
            file.close()

    def input_data(self,i_data):
        pre, scorelist = self.bf.predict(i_data)
        return pre

    def check_file(self,pre,input_str):
        s_filename = "./trainData/"+pre+".txt"
        file = open(s_filename,"r",encoding="utf-8")
        t_list =[]
        while True:
            text = file.readline()
            if len(text) > 1:
                t_list.append(text[:-1])
            if not text: 
                break
        file.close()

        if input_str not in t_list:
            return 0
        else:
            return 1
        
    def write_file(self,pre,input_str):    
        s_filename = "./trainData/"+pre+".txt"
        w_file = open(s_filename,"a",encoding="utf-8")
        w_file.write(input_str)
        w_file.write("\n")
        w_file.close()
         