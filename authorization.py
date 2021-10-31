#import psycopg2
from db_connection import db_conn

# Checks if the username and password exsist in the db
def isAuthorized(username, password):
    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute(f"SELECT * FROM auth WHERE username='{username}' AND password='{password}';")

    # Retrieve query results and check if user exsists
    if(cur.fetchone() is None):
        return 0
    else:
        return 1



