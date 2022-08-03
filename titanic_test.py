import pandas as pd

def input_file():
    train_data=pd.read_csv('train.csv')
    test_data=pd.read_csv('test.csv')
    return train_data, test_data

def main():
    #print('main')
    train,test=input_file()

    #print(train)
    #print(test)

if __name__=="__main__":
    main()