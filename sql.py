import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record, craete table, retrieve
cursor=connection.cursor()

## create the table

table_info="""
CREATE TABLE student(name varchar(25), class varchar(25), section varchar(25), marks int);
"""
cursor.execute(table_info)

## insert some more records

cursor.execute('''INSERT INTO student VALUES('Krish','Data Science','A',90)''')
cursor.execute('''INSERT INTO student VALUES('Sudhanshu','Data Science','B',100)''')
cursor.execute('''INSERT INTO student VALUES('Darius','Data Science','A',86)''')
cursor.execute('''INSERT INTO student VALUES('Vikash','DEVOPS','A',50)''')
cursor.execute('''INSERT INTO student VALUES('Dipesh','DEVOPS','A',35)''')


## display all the records
print("The inserted records are")

data=cursor.execute('''SELECT * FROM student''')

for row in data:
    print(row)

## close the connection
connection.commit()
connection.close()

