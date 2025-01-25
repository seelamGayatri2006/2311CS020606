import pandas as pd
import seaborn as sns
import matplotlib

# Sample data (you can replace this with your actual data)
data = {
    'Temperature': [23, 25, 38, 18, 21, 14, 14, 16, 29, 27, 28, 38, 31, 13, 14, 15, 33, 35, 37, 14, 24, 25, 28, 19, 18, 20],
    'Humidity': [65, 66, 77, 78, 70, 75, 98, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperature'], df['Humidity'], color='blue', label='Temperature vs Humidity')

# Adding labels and title
plt.title('Temperature vs Humidity', fontsize=14)
plt.xlabel('Temperature', fontsize=12)
plt.ylabel('Humidity', fontsize=12)
plt.legend()

# Show the plot
plt.show()
