import happybase

# HBase configuration
hbase_host = '127.0.0.1'  # Replace with your HBase server hostname or IP address
hbase_port = 9090  # Replace with your HBase Thrift server port

# Connect to HBase
connection = happybase.Connection(host=hbase_host, port=hbase_port)

try:
    # Open a table
    table_name = 'logs_table'  # Replace with your HBase table name
    table = connection.table(table_name)

    # Perform a scan on the table
    for key, data in table.scan():
        print(f"Row key: {key}, Data: {data}")

finally:
    # Close the connection
    connection.close()
