from cassandra.cluster import Cluster

# Replace these with your Cassandra cluster details
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

# Replace 'your_keyspace' with the actual keyspace name
keyspace = 'my_keyspace'
session.set_keyspace(keyspace)

# Replace 'employees' with your actual table name
table_name = 'person'

# Define your query to fetch records
query = "SELECT * FROM {table_name}"

# Execute the query and fetch the results
result = session.execute(query)

# Process the results
for row in result:
    print(row)

# Close the Cassandra session and cluster connection
session.shutdown()
cluster.shutdown()
