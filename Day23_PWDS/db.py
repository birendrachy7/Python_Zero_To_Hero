# create a file name db.py
# add 5 function in it:
# - create_bdb
# - add_data
# - read_data
# - update_data
# - delete_data

# Inside every function function add print statement saying " You are inside "
# Call the function

# Import SQLite
import sqlite3

# connect to DataBase
connection = sqlite3.connect("students.db")

# Calling the cursor: this is what  help us to interact with database

cursor = connection.cursor()

# Creating the table
"""
# create table table_name (
#     column1 datatype constraints,
#     column1 datatype constraints,
#     column1 datatype constraints,
#     .........
# )

# Example:
#     create table employee(
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         ..........
#     )
"""


# def create_table_query():

#     create_table_query = """
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     age INTEGER,
#     email TEXT
# )
# """
#     try:
#         cursor.execute(create_table_query)
#         print("Table Create Successfully")

#     except Exception as e:
#         print("Error creating table")
#         print(e)

# def add_db():
    #     #Altering the table - Add column
    #     alter_table_query = """
    #         alter table users add column phone_number text;
    # """
    #     try:
    #         cursor.execute(alter_table_query)
    #         print('Table altered Successfully - Added Phone number columns')

    #     except Exception as e:
    #      print('Error altering table')
    #      print(e)

    #  # ALtering table - Rename table

    #     rename_table_query = """
    # alter table users rename to students;
    # """
    #     try:
    #         cursor.execute(rename_table_query)
    #         print('Table Rename Successfully from users to students')

    #     except Exception as e:
    #         print('Error renaming table')
    #         print(e)

    # # Create - Single Inserting record to database table

    # insert_single_query="""
    # insert into students (name , age, email, phone_number) values (?,?,?,?);
    # """
    # try:
    #     cursor.execute(insert_single_query,['Birendra',20,'biru@gmail.com','895316'])
    #     connection.commit()
    #     print('Single record insert successfully')
    # except Exception as e:
    #     print("Error")
    #     print(e)
    
    # Multiple Record to database table
    # insert_multiple_query = """
    # insert into students (name, age,email,phone_number) values (?,?,?,?);
    # """
    # students_data = [
    #     ["Bibek", 22, "bibke@gmail.com", "255-589"],
    #     ["Lochan", 23, "locahna@gmail.com", "265616130"],
    #     ["bob", 25, "bob@gmail.com", "1566565"],
    # ]

    # try:
    #     cursor.executemany(insert_multiple_query, students_data)
    #     connection.commit()
    #     print("Multiple record inserted successfully")
    # except Exception as e:
    #     print("Error while inserting multiple records")
    #     print(e)


def read_db():
    print("-----------Reading all data----------------")
    cursor.execute('select * from students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    print()
    
    # print("----------------read_column data-----------")
    # cursor.execute('select name,email from students')
    # column_data = cursor.fetchall()
    # for column in column_data:
    #     print(column)
        
    # print()
    
    # print("----------------read conditional data--------------")
    # cursor.execute("SELECT * FROM students WHERE email = 'biru@gmail.com'")
    # conditional_data_reading = cursor.fetchall()
    # for con in conditional_data_reading:
    #     print(con)
    
    # print()
    
    # print("----------------Sorting by select-----------")
    # cursor.execute('select name from students order by Name ASC')
    # sorting_data_reading = cursor.fetchall()
    # for sor in sorting_data_reading:
    #     print(sor)

# def update_db():
#     update_query=""" 
#     update students set age = 21 where name = "Birendra";
#     """
    
#     try:
#         cursor.execute(update_query)
#         print('Update successfully')
#     except Exception as e:
#         print("Error")
#         print(e)

def delete_db():
    cursor.execute("delete from students where name =?",("bob",))
    connection.commit()
    print("Data Delete Successfully")


# create_table_query()
# add_db()
# update_db()
delete_db()
read_db()
