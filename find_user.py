from db_connection import db_conn

def findUser(first, last):
    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute(f"SELECT * FROM auth WHERE first_name='{first}' AND last_name='{last}';")

    # Retrieve query results and check if user exsists
    if(cur.fetchone() is None):
        return 0
    else:
        return 1