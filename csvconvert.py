import csv

# Array of strings
data = [
    ["Name", "Age", "Location"],
    ["John", "25", "New York"],
    ["Emma", "30", "Los Angeles"],
    ["Michael", "28", "Chicago"]
]

# Specify the file name
csv_file = "D:\\sheets\\output.csv"

# Write the array of strings into the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file has been written successfully.")
