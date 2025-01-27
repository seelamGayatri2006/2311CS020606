import pandas as pd
sales_data = {
    'Transaction' : [1,2,3,4,5],
    'CustomerID': [101,102,103,104,101],
    'Amount' : [250, 300, 400, 500, 600],
    'Data' : ['2025-01-01','2025-01-02','2025-01-03','2025-01-04','2025-01-05']
}# Display 
customer_data = {
    'CustomerID' : [101, 102, 103, 104],
    'CustomerName' : ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30,35,40,25],
    'City' : ['New York','los Angeles' , 'Chicago','Houston']
    
    
}
sales_df = pd.DataFrame(sales_data)
customers_df = pd.DataFrame(customer_data)

print("Sales DataFrame:")
print(sales_df.head())
#1. Exploring the dataset (using shape and describe)
print("\nShape of sales data:", sales_df.shape)
print("\nSales data statistics:")
print(sales_df.describe())
print("Sales dataframe",sales_df)
print("customers_df",customers_df)

# filter a datafraame of sales data frame where sales amount > 400 
# display (data.loc[(data.Brand == 'Maruti')])


merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)

print("\nAccess data using ''")

# 2. Merging data (Sales with Customer info)
merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)

# 3. Accessing data using `loc` and `iloc`
print("\nAccess data using `loc` (row 1):")
print(merged_df.loc[1])

print("\nAccess data using `iloc` (row 2):")
print(merged_df.iloc[2])

# 4. Handling Missing Values
# Let's introduce some missing data for demonstration
merged_df.loc[2, 'Age'] = None  # Introduce missing value in Age column
print(merged_df)
# Check for missing values
print("\nCheck missing values (isnull):")
print(merged_df.isnull().sum())

# Fill missing values with the mean (for Age column)
merged_df['Age'].fillna(merged_df['Age'].mean(), inplace=True)
print("\nData after filling missing values:")
print(merged_df)

# 5. Aggregation: Calculate the mean sales per customer
mean_sales = merged_df.groupby('CustomerName')['Amount'].mean()
print("\nMean sales per customer:")
print(mean_sales)