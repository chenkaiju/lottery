import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, LSTM, TimeDistributed, RepeatVector
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam

def readTrain():
    train = pd.read_csv("power_lotto_100001_107090.csv")
    #print(train.dtypes)

    number = train[['NUMBER', 'SPECIAL NUMBER']]
    number2 = pd.DataFrame()
    for index, row in number.iterrows():
        #print ((row['NUMBER'].split(',')))
        row['NUMBER'] = list(map(int, row['NUMBER'].split(',')))
        a = [0] * 49
        for num in row['NUMBER']:
            a[num-1] = 1

        b = [0] * 8
        b[row['SPECIAL NUMBER']-1] = 1

        number2 = number2.append({'a': a, 'b':b}, ignore_index=True)

    

    return number2

if __name__=="__main__":
    number = readTrain()

    print(number)
