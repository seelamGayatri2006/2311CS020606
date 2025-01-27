import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.randint(20,81,1000)

plt.hist(data,bins=10000,edgecolor='black',color='purple')
plt.title('Histogram of Cancer Patients Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.show()
          