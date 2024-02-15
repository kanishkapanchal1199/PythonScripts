import pandas as pd
import numpy as np

# Generate data for the first Excel sheet
np.random.seed(0)  # For reproducibility

num_records = 100000
ids = np.arange(1, num_records + 1)
names = np.random.choice(['John', 'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy'], num_records)
ages = np.random.randint(20, 40, num_records)
emails = np.random.choice(['john@example.com', 'alice@example.com', 'bob@example.com', 'charlie@example.com',
                           'david@example.com', 'emma@example.com', 'frank@example.com', 'grace@example.com',
                           'henry@example.com', 'ivy@example.com'], num_records)

df1 = pd.DataFrame({'id': ids, 'name': names, 'age': ages, 'email': emails})
df1.to_excel("D:\\sheets\\sheetFirst.xlsx", index=False)

# Generate data for the second Excel sheet with some matching and some different records
matching_records = 50000
different_records = num_records - matching_records

# Shuffle the ids array to ensure randomness
np.random.shuffle(ids)

# Extract matching and different ids
matching_ids = ids[:matching_records]

# Generate matching data for the second sheet
matching_names = np.random.choice(['John', 'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy'], matching_records)
matching_ages = np.random.randint(20, 40, matching_records)
matching_emails = np.random.choice(['john@example.com', 'alice@example.com', 'bob@example.com', 'charlie@example.com',
                                    'david@example.com', 'emma@example.com', 'frank@example.com', 'grace@example.com',
                                    'henry@example.com', 'ivy@example.com'], matching_records)

# Generate different data for the second sheet
different_ids = np.arange(1, different_records + 1)  # Start from 1 for the different records
different_names = np.random.choice(['John', 'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy'], different_records)
different_ages = np.random.randint(20, 40, different_records)
different_emails = np.random.choice(['john@example.com', 'alice@example.com', 'bob@example.com', 'charlie@example.com',
                                     'david@example.com', 'emma@example.com', 'frank@example.com', 'grace@example.com',
                                     'henry@example.com', 'ivy@example.com'], different_records)

# Combine matching and different data for the second sheet
df2 = pd.DataFrame({'id': np.arange(1, num_records + 1),  # IDs start from 1
                    'name': matching_names.tolist() + different_names.tolist(),
                    'age': matching_ages.tolist() + different_ages.tolist(),
                    'email': matching_emails.tolist() + different_emails.tolist()})
df2.to_excel("D:\\sheets\\sheetSecond.xlsx", index=False)

print("Data generation completed. Two Excel sheets created: 'sheet1.xlsx' and 'sheet2.xlsx'")
