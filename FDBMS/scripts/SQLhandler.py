import sqlite3

import random

# Initialize Faker to generate random data


# Connect to the SQLite database
conn = sqlite3.connect("faculty.sqlite3")
cur = conn.cursor()

# Create tables (if they don't exist)
cur.execute('''CREATE TABLE IF NOT EXISTS STUDENTS(
            REGNO varchar(100),
            Name varchar(255),
            Email varchar(255),
            Phone_no integer(10)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS FACULTIES(
            EMPID varchar(100),
            Name varchar(255),
            Email varchar(255),
            Phone_no integer(10)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS DEPARTMENTS(
            DEPT_ID varchar(255),
            DEPT_Name varchar(255),
            EMPID varchar(255),
            REGNO integer(10)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS COURSES(
            C_ID varchar(100),
            C_Name varchar(255),
            EMPID varchar(255),
            REGNO integer(10)
            )''')

cur.execute('''
CREATE TRIGGER IF NOT EXISTS delete_student_data
AFTER DELETE ON STUDENTS
BEGIN
    DELETE FROM COURSES WHERE REGNO = OLD.REGNO;
END;
''')
             

# Function to store student data
def store_stud_data(REGNO, NAME, EMAIL, PH_NO):
    cur.execute(
        '''INSERT INTO STUDENTS (REGNO, Name, Email, Phone_no) VALUES (?, ?, ?, ?)''',
        (REGNO, NAME, EMAIL, PH_NO)
    )

# Function to store faculty data
def store_faculty_data(EMPID, NAME, EMAIL, PH_NO):
    cur.execute(
        '''INSERT INTO FACULTIES (EMPID, Name, Email, Phone_no) VALUES (?, ?, ?, ?)''',
        (EMPID, NAME, EMAIL, PH_NO)
    )

# Function to store department data
def store_dept_data(DEPT_ID, DEPT_NAME, EMPID, REGNO):
    cur.execute(
        '''INSERT INTO DEPARTMENTS (DEPT_ID, DEPT_Name, EMPID, REGNO) VALUES (?, ?, ?, ?)''',
        (DEPT_ID, DEPT_NAME, EMPID, REGNO)
    )

# Function to store course data
def store_course_data(C_ID, C_Name, EMPID, REGNO):
    cur.execute(
        '''INSERT INTO COURSES (C_ID, C_Name, EMPID, REGNO) VALUES (?, ?, ?, ?)''',
        (C_ID, C_Name, EMPID, REGNO)
    )

conn.commit()
conn.close()


# Generate and store mock data
for i in range(1, 11):
    REGNO = f'REG{i}'
    NAME = fake.name()
    EMAIL = fake.email()
    PH_NO = random.randint(1000000000, 9999999999)
    store_stud_data(REGNO, NAME, EMAIL, PH_NO)

for i in range(1, 6):
    EMPID = f'EMP{i}'
    NAME = fake.name()
    EMAIL = fake.email()
    PH_NO = random.randint(1000000000, 9999999999)
    store_faculty_data(EMPID, NAME, EMAIL, PH_NO)

for i in range(1, 6):
    DEPT_ID = f'DEPT{i}'
    DEPT_NAME = fake.job()
    EMPID = f'EMP{i}'
    REGNO = f'REG{i}'
    store_dept_data(DEPT_ID, DEPT_NAME, EMPID, REGNO)

for i in range(1, 6):
    C_ID = f'COURSE{i}'
    C_Name = fake.job()
    EMPID = f'EMP{i}'
    REGNO = f'REG{i}'
    store_course_data(C_ID, C_Name, EMPID, REGNO)

# Commit changes and close connection
conn.commit()
conn.close()
