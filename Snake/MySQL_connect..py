import mysql.connector
conn = mysql.connector.connect(user="root",  password="123456Phuc@", host='127.0.0.1')  
print(conn)
conn.close()
