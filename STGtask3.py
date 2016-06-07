#This Program implements all the Tasks that are as mentioned in the Document-"Sample Project using Python and Sqlite3", provided by the STG dept., TU Darmstadt.
#This program can be run multiple times, without re-populating the same data repeatedly(i.e, again and again) 

import random
import sqlite3
import matplotlib.pyplot as plt


#Connect to the database, if not present - Create the database and connect to it.
conn = sqlite3.connect('db3.db')
c = conn.cursor()


graphArray = []
tcp_id = []
tcp_value = []
udp_id = []
udp_value= []


#Create a table & if it is already present continue without exceptions
try:    
    c.execute('''CREATE TABLE comm3(ID INT, type text, size integer)''')
except sqlite3.OperationalError:
    print("Table already exists, hence continuing with the insertion of the data\nZoom to particularly view the data on Graph")
                    

#Function to Insert 1 million entries in the database    
def insert_data():
    for x in range(1,1000001):
        protocol = ['TCP', 'UDP']
        b = random.randrange(1,10001)
        graphArrayAppend = [x, random.choice(protocol), b]
        graphArray.append(graphArrayAppend)
    c.executemany('INSERT INTO comm3 VALUES (?,?,?)', graphArray)    
    conn.commit()
    

#Function to draw TCP values on Graph
def TCP_Graph():    
    for row in c.execute("SELECT * FROM comm3 where type='TCP'"):        
        id_value = row[0]
        tcp_id.append(id_value)
        size_value = row[2]
        tcp_value.append(size_value)   

#Function todraw UDP values on Graph
def UDP_Graph():
    for rowu in c.execute("SELECT * FROM comm3 where type='UDP'"):        
        id_valueu = rowu[0]
        udp_id.append(id_valueu)
        size_valueu = rowu[2]
        udp_value.append(size_valueu)

#calling the above defined functions
insert_data()
TCP_Graph()
UDP_Graph()

#Plotting the graph
plt.plot(tcp_id, tcp_value, '.', label='TCP Line' )
plt.plot(udp_id, udp_value, '.', label='UDP Line' )
plt.xlabel("Entry Number in the Database")
plt.ylabel("Size of the Entry Number")
plt.title("TCP vs UDP - Size Plotting Graph")
plt.legend()
plt.show()

#Deleting data after demonstration
def delete_data():
    c.execute("DELETE FROM comm3")
    conn.commit()

delete_data()
