# aura-analysis-

This code consists of analyzing the data that was logged in aura-datalog. 

In order to understand user behaviour and contribute towards creating a favourites page for Aura's App we need to analyze the timings and time period of when the appliances were in use.

We use Pandas library in Python as a tool for data analysis. 

First,import the CSV file from aura-datalog and store it into a new dataframe (df). A list containing unique AID is stored in "array" : ```array = df['AID'].unique()``` 

To make it easier to analyze data, data clustering is required and so we cluster the data according to the unique AID's in array into a new dataframe(df_new).This is done in the for loop.  

```
   for item in array[0:]:
   df_new = df[df['AID'] == item]
   ``` 

Once,data clustering is done we create a new column in df_new called "Time Difference", this column converts the TimeStamp column value into seconds which is used in the function ```timedifference()``` for calculations. 

In ```timedifference()```  we find the time difference between consecutive rows. We keep the first row as it is, and do the calculations from the next row onwards. 
```df_new['TimeDifference'].iloc[i - 1] = df_new['TimeDifference'].iloc[i] - df_new['TimeDifference'].iloc[ i - 1]``` 

After finding the time differences in rows, now we need to process the data and carry out statistical calculations. 
We want to understand and retrieve ranges for when an appliance is in use,this is carried out in ```dataprocessing()```. To reduce anomalies and redundancies,we only accept if the range of the difference is greater than or equal to 1800 seconds(30 minutes). This is because other data maybe a user trying out different appliances or it could be data from two different dates(negative time difference values).

Since the date is not necessary in making calculations, we convert the TimeStamp column to only contain the minutes, if the cluster contains more than one row after the if condition for the time range is statisfied statistical calculations are carried out.If the cluster contains only one row, then we only calculate the mean. 

The mean and standard deviation of the TimeStamp column is calculated. The low and high values are used to show the minimum and maximum values of when a particular appliance is used. After that we covert the minutes back into 24-hour format to display the time ranges. 

### For executing the program:

Execute the functions block by block by pressing Shift+Enter and then the for-loop.





 
 



    



