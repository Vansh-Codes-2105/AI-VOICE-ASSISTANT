import csv
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote 2016.exe')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'google', 'https://www.google.co.in/')"
cursor.execute(query)
con.commit()

#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


#desired_columns_indices = [0, 20]
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    #csvreader = csv.reader(csvfile)
    #for row in csvreader:
        #selected_data = [row[i] for i in desired_columns_indices]
        #3cursor.execute("INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?);", tuple(selected_data))  
#con.commit()
#con.close()