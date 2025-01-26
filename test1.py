import pandas as pd
data = [20,30,40,50,2,3,6,8,10,18,19]
No_of_studied = data[4:8]
print("No.of hours_studied",No_of_studied)
Age=data[9:13]
print("Student_age",Age)
screen_time = data[12:18]
print("screen_time",screen_time)
Data_Frame = pd.DataFrame(data)
print(Data_Frame)