import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('project_database/project_covid-database.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
def drop_table():
    cursor_obj.execute("drop table covid_vaccination ")
    print("table dropped successfully")


# # deleting the records
def delete_records():
    sql_delete_query = """DELETE from covid_vaccination"""
    cursor_obj.execute(sql_delete_query)
    connection_obj.commit()
    print("Record deleted successfully ")

 
# Creating table
def create_table():
    table = """ CREATE TABLE covid_vaccination (
                ADHAR_NUMBER INT UNIQUE NOT NULL,
                First_Name CHAR(25) NOT NULL,
                Last_Name char(10),
                Phone_Number INT not null,
                Dose INT
            ); """
    cursor_obj.execute(table)
    print("table is created")

def enter_records(): 
    while True:
        adhar_number = input("enter the adhar number:  ")
        if len(str(adhar_number)) != 12:
            print("enter valid adhar number")
            continue
        first_name = input("enter the first name:  ")
        last_name = input("enter the last name:  ")
        phone_number = input("enter the phone number:  ")
        if len(str(phone_number)) != 10:
            print("enter valid phone number")
            continue
        dose = int(input("enter the dosage number:  "))
        if dose > 2:
            print("enter the valid dose number")
            continue
        sql = "insert into covid_vaccination(adhar_number, first_name, last_name, phone_number, dose) values (?, ?, ?, ?, ?);"
        cursor_obj.execute(sql, (adhar_number, first_name, last_name, phone_number, dose))
        connection_obj.commit()
        data=cursor_obj.execute('''SELECT * FROM covid_vaccination''')
        for row in data:
            print(row)
    
# # printing the records 
def print_records():  
    print("Data Inserted in the table: ")
    data=cursor_obj.execute('''SELECT * FROM covid_vaccination''')
    for row in data:
        print(row)  

# create_table()
        
enter_records()

# delete_records() 

# print_records() 

# drop_table()   
    
    
    