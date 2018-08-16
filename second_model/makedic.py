import glob, os
from konlpy.tag import Komoran


class Makedic:
    def __init__(self):
        self.komoran = Komoran()
        self.files = glob.glob("./trainData/*.txt",recursive=True)
        self.w_file = open("./dictionary.txt","w",encoding="utf-8")
        self.word_lst=[]
        self.char_lst=['N','M','V','S']

    def writefile(self):
        for file_name in self.files:
            basename = os.path.basename(file_name)
            categorty = basename.split(".")[0]
            i_file = open(file_name,"r",encoding="utf-8")
            while True:
                text = i_file.readline()
                if not text: 
                    break
                if len(text) > 1:
                    s_line = text[:-1].split("\t")
                    t_line = self.komoran.pos(s_line[0]) 
                    for val in t_line:
                        if not val[0] in self.word_lst and val[1][0] in self.char_lst:
                            if val[1][0] == 'S':
                                if val[1][1] == 'L':
                                    self.word_lst.append(val[0])
                            else:
                                self.word_lst.append(val[0])
            i_file.close()
            
        for value in self.word_lst:
            self.w_file.write(value+'\n')