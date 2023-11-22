
# create dictionary to hold connection info 
dbConfig = { 
    'user': 'root',      # use your admin name
    'password': "123456Phuc@",   # use your real password 
    'host': '127.0.0.1',      # IP address of localhost 
}

import mysql.connector 
# unpack dictionary credentials
conn = mysql.connector.connect(**dbConfig) 
print(conn)

conn.close()
