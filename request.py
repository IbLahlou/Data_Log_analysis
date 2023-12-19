import happybase

# HBase configuration
hbase_host = '127.0.0.1'  
hbase_port = 9090  

# Connect to HBase
connection = happybase.Connection(host=hbase_host, port=hbase_port)

try:
    # Open a table
    table_name = 'logs'  
    table = connection.table(table_name)

    # Perform a scan on the table
    for key, data in table.scan():
        print(f"Row key: {key}, Data: {data}")

finally:
    # Close the connection
    connection.close()
