import pandas as pd
import time

def compare_excel_files(file1, file2):
    start_time = time.time()  # Record start time
    
    # Read Excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Merge dataframes on ID column
    merged_df = pd.merge(df1, df2, on='id', suffixes=('_1', '_2'), how='outer')

    # Create a list to store mismatched data
    mismatched_data = []

    # Iterate over each row
    for index, row in merged_df.iterrows():
        id_value = row['id']
        name_match = row['name_1'] == row['name_2']
        age_match = row['age_1'] == row['age_2']

        # Check if both name and age are mismatched
        if not (name_match and age_match):
            # Create a status string indicating the mismatched columns
            mismatched_columns = []
            if not name_match:
                mismatched_columns.append('name')
            if not age_match:
                mismatched_columns.append('age')

            status = f"Mismatched: {', '.join(mismatched_columns)}"
            
            # Append the ID and status to the mismatched data list
            mismatched_data.append({'id': id_value, 'status': status})

    # Convert the list of mismatched data to a DataFrame
    mismatched_df = pd.DataFrame(mismatched_data)
    
    # Write the mismatched data to a new Excel file
    mismatched_df.to_excel("D:\\sheets\\mismatched_data.xlsx", index=False)
    
    end_time = time.time()  # Record end time
    elapsed_time = end_time - start_time
    print(f"Time taken for file generation: {elapsed_time} seconds")

# Example usage:
compare_excel_files("D:\\sheets\\sheetFirst.xlsx", "D:\\sheets\\sheetSecond.xlsx")
