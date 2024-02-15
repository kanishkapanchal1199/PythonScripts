import pandas as pd

# Specify the CSV file name
csv_file = "D:\\sheets\\output.csv"

# Read the CSV file while skipping the header
df = pd.read_csv(csv_file, skiprows=1)

# Print the DataFrame without the header
print(df[0])
