import pandas as pd
import time

def compare_excel_files(file1, file2):
    start_time = time.time()  # Record start time
    
    # Read Excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Merge dataframes on ID column
    merged_df = pd.merge(df1, df2, on='id', suffixes=('_1', '_2'), how='outer')

    print(merged_df)

    # Create a list to store comparison result
    comparison_data = []

    # Iterate over each row
    for index, row in merged_df.iterrows():
        id_value = row['id']

        # Check if data is matched or mismatched for each column (excluding 'id')
        mismatched_columns = [col for col in df1.columns if col != 'id' and row[f'{col}_1'] != row[f'{col}_2']]

        if len(mismatched_columns) == 0:
            status = 'Matched'
        else:
            status = 'Mismatched: ' + ', '.join(mismatched_columns)

        # Append the comparison result to the list
        comparison_data.append({'id': id_value, 'status': status})

    # Create DataFrame from the list of dictionaries
    comparison_result = pd.DataFrame(comparison_data)
    # Write the result to a new Excel file
    comparison_result.to_excel("D:\\sheets\\comparison_result_new1.xlsx", index=False)
    
    end_time = time.time()  # Record end time
    elapsed_time = end_time - start_time
    print(f"Time taken for file generation: {elapsed_time} seconds")

# Example usage:
compare_excel_files("D:\\sheets\\sheetFirst1.xlsx", "D:\\sheets\\sheetSecond1.xlsx")
