import pandas as pd
from pandas._libs import indexing
from pandas.core.frame import DataFrame
import time
from datetime import datetime
import math

df = pd.read_csv('/Users/rakshanfathima/Desktop/data.csv')
print(df.to_string())

 # counts number of times each AID is clicked
df.value_counts('AID') 

array = []
# gets unique values from dataframe and stores in the array
array = df['AID'].unique()
print(array)


def timedifference():
    for i in range(0, len(df_new)):
        # print(i)
        if i == 0:
            continue
        else:
            df_new['TimeDifference'].iloc[i - 1] = df_new['TimeDifference'].iloc[i] - df_new['TimeDifference'].iloc[ i - 1]
    print(df_new.to_string())


def dataprocessing():
    timediff = df_new['TimeDifference']
    print(timediff)
    start = 0
    for i in range(0, len(timediff)):
        if (timediff[i] - timediff[0] >= 1800):
            
            frame = df_new.iloc[start:i + 1]

            print(frame)
            frame['TimeStamp'] = frame['TimeStamp'].apply(lambda x: x.split(' ')[1])
            frame['TimeStamp'] = frame['TimeStamp'].apply(lambda x: x.split(':'))
            frame['TimeStamp'] = frame['TimeStamp'].apply(lambda x: int(x[0]) * 60 + int(x[1]))
            
            # if condition - calculate if rows>1
            if (len(frame) > 1):
                mean = frame['TimeStamp'].mean()
                mean_in_hours = mean / 60
                std = frame['TimeStamp'].std()
                std_in_hours = std/60
                x = (mean_in_hours)
                y = std_in_hours
                low = x - y
                high = x + y
                minutes = mean_in_hours*60
                minlow = (low%1) * 60
                minhigh = (high%1) *60
                mean_in_hours, minutes = divmod(minutes, 60)
                print ( frame['AID'].iloc[0] , 'low :' "%02d:%02d"%(low,minlow), 'high :' "%02d:%02d"%(high,minhigh))
            else: 
                    print (frame['AID'].iloc[0], "%02d:%02d"%(mean_in_hours,minutes))
            start = i + 1


for item in array[0:]:
    #print (item)
    # splits dataframes according to AID
    df_new = df[df['AID'] == item]
    print(df_new)
    # extracting time from the TimeStamp
    df['TimeDifference'] = df['TimeStamp'].apply(lambda x: x.split(' ')[1])
    df_new['TimeDifference'] = df_new['TimeDifference'].apply(lambda x: x.split(':'))
    df_new['TimeDifference'] = df_new['TimeDifference'].apply(lambda x: int(x[0]) * 60 * 60 + int(x[1]) * 60 + int(x[2]))
    df_new.reset_index(level=None, drop=False, inplace=True, col_level=0, col_fill='')
    timedifference()
    dataprocessing() 

                
              
                

                
            
                

     

