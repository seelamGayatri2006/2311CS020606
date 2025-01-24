import pandas as pd 
import numpy as np 
import matplotlib.pyplot as pyplotimport seaborn as sns
np.random.seed(10)
data = pd.DataFrame({
    'value': np.concatenate([np.random.normal(0,1,100),np.random.randit.normal(10,1,10)]) 
})
Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = q3 + 1.5 * IQR

outliers = data[(data['value'] < lower_bound) | (data['value'] > upper_bound)]
 print()


#Given : 23, 42, 12, 10, 15, 14, 9.
#Arrange the given dataset in ascending order.
#9,10,12,14,15,23,42
#Hence,
#Minimum = 9
#maximun = 42
#median = 14
#First Quartile (Q1) = 10 (middle value of 9, 10, 12 is 10)
#Third Quartile (Q3) = 23(middle value of 15, 23, 42 is 23).