'''
Created on May 29, 2019
Ch07
@author: Burkhard A. Meier
'''

import mysql.connector 
import GuiDBConfig as guiConf 

GUIDB = 'LeaderBoard' 
 
# unpack dictionary credentials  
conn = mysql.connector.connect(**guiConf.dbConfig) 
 
cursor = conn.cursor() 

cursor.execute("SHOW DATABASES")  
print(cursor.fetchall()) 
 
conn.close() 