import glob, os
from konlpy.tag import Komoran
komoran = Komoran()

files = glob.glob("./trainData/*.txt",recursive=True)
w_file = open("./dictionary.txt","w",encoding="utf-8")

word_lst=[]
char_lst=['N','M','V','S']

for file_name in files:
    basename = os.path.basename(file_name)
    categorty = basename.split(".")[0]
    i_file = open(file_name,"r",encoding="utf-8")
    while True:
        text = i_file.readline()
        if not text: 
            break
        if len(text) > 1:
            s_line = text[:-1].split("\t")
            t_line = komoran.pos(s_line[0]) 
            print(t_line)
            for val in t_line:
                if not val[0] in word_lst and val[1][0] in char_lst:
                    if val[1][0] == 'S':
                        if val[1][1] == 'L':
                            word_lst.append(val[0])
                    else:
                        word_lst.append(val[0])
    i_file.close()

for value in word_lst:
    w_file.write(value+'\n')