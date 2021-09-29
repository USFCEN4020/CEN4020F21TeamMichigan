import psycopg2

# Fucntion connects to the localhost server and incollege db


def db_conn():
    # Connect to your postgres DB
    return psycopg2.connect(host='localhost', port='5432', database='postgres', user='postgres', password='3600')
