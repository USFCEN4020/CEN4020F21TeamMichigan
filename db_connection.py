import psycopg2

# Fucntion connects to the localhost server and incollege db


def db_conn():
    # Connect to your postgres DB
    return psycopg2.connect(host='localhost', port='5432', database='incollege', user='postgres', password='3600')


def createTables():
    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute(f"CREATE TABLE IF NOT EXISTS auth(username VARCHAR(50) PRIMARY KEY, password VARCHAR(50) NOT NULL, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL);")
    cur.execute(f"CREATE TABLE IF NOT EXISTS jobs(id SERIAL PRIMARY KEY, title VARCHAR(50) NOT NULL, description VARCHAR(255) NOT NULL, employer VARCHAR(50) NOT NULL, location VARCHAR(50) NOT NULL, name VARCHAR(50) NOT NULL, salary REAL);")
    cur.execute(f"CREATE TABLE IF NOT EXISTS control (username VARCHAR(50) PRIMARY KEY REFERENCES auth(username), email boolean, sms boolean , advertising boolean, language VARCHAR(20));")
    cur.execute(f"CREATE TABLE IF NOT EXISTS profile(username VARCHAR(50) PRIMARY KEY REFERENCES auth(username), title TEXT, major VARCHAR(70), university VARCHAR(70), about TEXT);")
    cur.execute(f"CREATE TABLE IF NOT EXISTS experiences(username VARCHAR(50), title VARCHAR(70), employer VARCHAR(70), date_started TEXT, date_ended TEXT, location VARCHAR(70), description TEXT);")
    cur.execute(f"CREATE TABLE IF NOT EXISTS education(username VARCHAR(50) PRIMARY KEY REFERENCES auth(username), school VARCHAR(70), degree VARCHAR(70), year_attended TEXT);")
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS friends(user_1 VARCHAR(50), user_2 VARCHAR(50), pending BOOLEAN);")
    # Challenge 6
    cur.execute(f"CREATE TABLE IF NOT EXISTS applications(id SERIAL PRIMARY KEY, title VARCHAR(50), name VARCHAR(50), grad_date VARCHAR(50), start_date VARCHAR(50), reason VARCHAR(255), save BOOLEAN);")
    conn.commit()
