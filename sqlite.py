import sqlite3

## Connect to sqllite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table
cursor = connection.cursor()

## Create table Query
table_info = """
CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""


cursor.execute(table_info)

## Insert some more record
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Kongden','Data Analytics','B',95)''')
cursor.execute('''Insert Into STUDENT values('Seyha','Machine Learning','C',80)''')
cursor.execute('''Insert Into STUDENT values('Seavlang','Deep Learning','B',90)''')
cursor.execute('''Insert Into STUDENT values('ChanRath','LLM','C',80)''')

## Display all the record
print("The inserted record are")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

## Commit my changes in the database
connection.commit()
connection.close()