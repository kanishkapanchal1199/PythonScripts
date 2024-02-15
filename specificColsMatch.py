import pandas as pd
import time

def compare_excel_files(file1, file2):
    start_time = time.time()  # Record start time
    
    # Read Excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Merge dataframes on ID column
    merged_df = pd.merge(df1, df2, on='id', suffixes=('_1', '_2'), how='outer')

    # Create a list to store comparison result
    comparison_data = []

    # Iterate over each row
    for index, row in merged_df.iterrows():
        id_value = row['id']
        name_match = row['name_1'] == row['name_2']
        age_match = row['age_1'] == row['age_2']

        if name_match and age_match:
            status = 'Matched'
        else:
            mismatched_columns = []
            if not name_match:
                mismatched_columns.append('name')
            if not age_match:
                mismatched_columns.append('age')
            status = 'Mismatched: ' + ', '.join(mismatched_columns)

        # Append the comparison result to the list
        comparison_data.append({'id': id_value, 'status': status})

    # Create DataFrame from the list of dictionaries
    comparison_result = pd.DataFrame(comparison_data)
    # Write the result to a new Excel file
    comparison_result.to_excel("D:\\sheets\\comparison_result_new.xlsx", index=False)
    
    end_time = time.time()  # Record end time
    elapsed_time = end_time - start_time
    print(f"Time taken for file generation: {elapsed_time} seconds")

# Example usage:
compare_excel_files("D:\\sheets\\sheetFirst.xlsx", "D:\\sheets\\sheetSecond.xlsx")
