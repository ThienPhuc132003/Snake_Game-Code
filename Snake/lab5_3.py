import mysql

conn = mysql.connector.connect(user="root",  password="123456Phuc@", host='127.0.0.1')  
print(conn)
conn.close()


dbConfig = {
    'user': 'root',  
    'password': '123456Phuc@',  
    'host': '127.0.0.1',
}
import mysql.connector
# unpack dictionary credentials
conn = mysql.connector.connect(**dbConfig)  
print(conn)

import GuiDBConfig as guiConf 
# unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)  
print(conn)
