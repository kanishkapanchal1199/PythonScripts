import pandas as pd
import numpy as np

# Generate data for the first Excel sheet
np.random.seed(0)  # For reproducibility

num_records = 100000
num_columns = 50  # Number of columns
ids = np.arange(1, num_records + 1)
names = np.random.choice(['John', 'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy'], num_records)
ages = np.random.randint(20, 40, num_records)

# Generate random values for 50 columns
column_names = [f'column_{i+1}' for i in range(num_columns)]
column_data = {col: np.random.randint(0, 100, num_records) for col in column_names}

df1 = pd.DataFrame({'id': ids, 'name': names, 'age': ages, **column_data})
df1.to_excel("D:\\sheets\\sheetFirst1.xlsx", index=False)

# Generate data for the second Excel sheet with some matching and some different records
matching_records = 50000
different_records = num_records - matching_records

# Shuffle the ids array to ensure randomness
np.random.shuffle(ids)

# Generate matching data for the second sheet
matching_names = np.random.choice(['John', 'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy'], matching_records)
matching_ages = np.random.randint(20, 40, matching_records)

# Generate random values for 50 columns for matching records
matching_column_data = {col: np.random.randint(0, 100, matching_records) for col in column_names}

# Generate different data for the second sheet
different_ids = np.arange(1, different_records + 1)  # Start from 1 for the different records
different_names = np.random.choice(['John', 'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy'], different_records)
different_ages = np.random.randint(20, 40, different_records)

# Generate random values for 50 columns for different records
different_column_data = {col: np.random.randint(0, 100, different_records) for col in column_names}

# Combine matching and different data for the second sheet
df2 = pd.DataFrame({'id': np.arange(1, num_records + 1),  # IDs start from 1
                    'name': np.concatenate([matching_names, different_names]),
                    'age': np.concatenate([matching_ages, different_ages]),
                    **{col: np.concatenate([matching_column_data[col], different_column_data[col]]) for col in column_names}})
df2.to_excel("D:\\sheets\\sheetSecond1.xlsx", index=False)

print("Data generation completed. Two Excel sheets created: 'sheetFirst1.xlsx' and 'sheetSecond1.xlsx'")
