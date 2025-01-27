import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns
datf = pd.DataFrame({"Season 1" : [7,4,5,6,3],
                    "Season 2": [1,2,8,4,9],
                   "Season 3": [6,7,8,9,3]})
p = sns.histplot(data = datf)
p.set(xlabel="X Label Value", ylabel = "Y Label Value")
plt.show()
