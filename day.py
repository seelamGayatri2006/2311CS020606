import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Create sample dataset
data = {
    "Square_Feet_Area": [8500, 9600, np.nan, 11250, np.nan, 9550, 14260, np.nan, 1830, 11500],
    "Year_Built": [2003, 2001, np.nan, 1990, 2000, 2006, 1978, 1950, np.nan, 2020],
    "OverAll_Condition": [5, 8, 6, 7, np.nan, 7, 8, 6, np.nan, 9],
    "Ready_to_move": ["Yes", "No", "Yes", np.nan, "No", np.nan, "Yes", "Yes", "No", "Yes"],
    "Sale_Price": [200000, 180000, 215000, 210000, 190000, 250000, 225000, 220000, 240000, 230000]
}

df = pd.DataFrame(data)

# Print Original DataFrame
print("Original DataFrame")
print(df)

# Create an imputer for numeric columns to replace NaN with mean
numeric_imputer = SimpleImputer(strategy='mean')

# Apply the imputer to the numeric columns
df[['Square_Feet_Area', 'Year_Built', 'OverAll_Condition']] = numeric_imputer.fit_transform(df[['Square_Feet_Area', 'Year_Built', 'OverAll_Condition']])

# Replacing missing values with mode for categorical columns
df['Ready_to_move'] = df['Ready_to_move'].fillna(df['Ready_to_move'].mode()[0])

# Print DataFrame after imputation
print("\nDataFrame after replacing missing values with mean (for numeric) and mode (for categorical)")
print(df)