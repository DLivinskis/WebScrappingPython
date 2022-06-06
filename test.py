import mysql.connector
from mysql.connector import Error


def InsertToSQL(thislistNames,thislistPrices,product,today):
    for Entry in thislistNames:
        connection = mysql.connector.connect( host='localhost',
                                                database = 'scrapping',
                                                user = 'root',
                                                password = '0000')

        mycursor = connection.cursor()
        sql = "INSERT INTO salidzini (name,price,queryname,date) VALUES (%s, %s,%s,%s)"
        val = (thislistNames[Entry], thislistPrices[Entry], product, today)
        mycursor.execute(sql, val)
        connection.commit()
        print(mycursor.rowcount, "record inserted.")





""""
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database = 'scrapping',
                                         user = 'root',
                                         password = '0000')
    if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
"""