import pandas as pd
from cassandra.cluster import Cluster

def connect_to_cassandra():
    cluster = Cluster(['127.0.0.1'], port=9042)  # Replace with your Cassandra cluster address
    session = cluster.connect()  # Connect to the cluster
    return session

def insert_matched_data_to_cassandra(session, comparison_result, df1):
    for _, row in comparison_result.iterrows():
        id_value = row['id']
        status = row['status']

        if status == 'Matched':
            # Get matched record from df1
            matched_record = df1[df1['id'] == id_value].iloc[0]
            name = matched_record['name']
            age = matched_record['age']
            email = matched_record['email']

            # Insert matched data into Cassandra table
            query = "INSERT INTO tutorialspoint.person (id, name, age, email) VALUES (?, ?, ?, ?)"
            session.execute(query)

def compare_excel_files(file1, file2):
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

        # Check if data is matched or mismatched for each column (excluding 'id')
        mismatched_columns = [col for col in df1.columns if col != 'id' and row[col + '_1'] != row[col + '_2']]

        if len(mismatched_columns) == 0:
            status = 'Matched'
        else:
            status = 'Mismatched: ' + ', '.join(mismatched_columns)

        # Append the comparison result to the list
        comparison_data.append({'id': id_value, 'status': status})

    # Create DataFrame from the list of dictionaries
    comparison_result = pd.DataFrame(comparison_data)
    
    # Connect to Cassandra
    session = connect_to_cassandra()
    
    # Insert matched data into Cassandra
    insert_matched_data_to_cassandra(session, comparison_result, df1)

# Example usage:
compare_excel_files("D:\\sheets\\sheetFirst.xlsx", "D:\\sheets\\sheetSecond.xlsx")
