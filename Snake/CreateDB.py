
import mysql.connector
import GuiDBConfig as guiConf 

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456Phuc@",
    database="LeaderBoard"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE highscore(name VARCHAR(50),score INTEGER(10))")
