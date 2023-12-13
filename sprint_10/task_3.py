# Create a Python program to use the sqlite database named "q1.db". 
# The query to the database should display information, as shown in 
# the example below, including phrases: about the successful connection, 
# the total number of records, the actual records, the record of closing the database. 
# From the table of "customers" to deduce all records for which in a "grade" field of value more than 200 with sort ordering on id
# For example output:
# Connected to SQLite
# Total rows are:   2
# Printing each row
# Id:  3022
# Name:  Nik Rimando
# City:  Madrid
# Grade:  1000
# Seller:  6001
# Id:  3025
# Name:  Grem Zusisa
# City:  USA
# Grade:  2000
# Seller:  6002
# The SQLite connection is closed

import sqlite3

def execute_query():
    try:
        connection = sqlite3.connect("q1.db")
        print("Connected to SQLite")
        cursor = connection.cursor()
        query = """
            SELECT * FROM customers
            WHERE grade > 200
            ORDER BY id;
        """
        cursor.execute(query)
        records = cursor.fetchall()
        print(f"Total rows are:   {len(records)}")
        print("Printing each row")
        for record in records:
            print(f"Id:  {record[0]}\nName:  {record[1]}\nCity:  {record[2]}\nGrade:  {record[3]}\nSeller:  {record[4]}\n\n")
    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        if connection:
            connection.close()
            print("The SQLite connection is closed")

execute_query()
