import mysql.connector





hostname = 'localhost'
username = 'brychxpin'
password = '12172328'
database = 'brychxpinNotes'

# Simple routine to run a query on a database and print the results:
# def doQuery( conn ) :
#     cur = conn.cursor()

#     cur.execute( "SELECT fname, lname FROM employee" )

#     for firstname, lastname in cur.fetchall() :
#         print( firstname, lastname )



print( "Using mysql.connector:" )
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
if myConnection:
    print("yes bitch")
else:
    print("u suck")
    myConnection.close()

