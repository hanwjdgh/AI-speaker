from train import Train
from function import Functions

def start():
    temp = ""
    func = Functions()

    while 1:
        tr = Train()
        tr.train_data()
        
        input_str = input()
        pre,lst = tr.input_data(input_str)
        check = tr.check_file(pre,input_str)
        print(lst)
        if input_str == "끝":
            break
        
        if check == 0:
            temp = input_str
            print("뭐라는 거야 다시 말해")
            continue
        elif len(temp) > 1:
            tr.write_file(pre,temp)
            temp = ""
        
        #print(dir(func)[dir(func).index(pre)])
        print(Functions.__dict__[pre](input_str))
if __name__ == '__main__':
    start()