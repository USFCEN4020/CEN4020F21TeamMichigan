from db_connection import db_conn


def jobNoti(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT EXISTS(SELECT name='{username}' FROM applications);"
    )
    records = cur.fetchall()
    if (records[0][0] == False):
        print("------------------------------------------------------------------------------- ")
        print("Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
        print("-------------------------------------------------------------------------------")


def profileNoti(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM profile WHERE username='{username}';"
    )
    records = cur.fetchall()
    if (len(records) == 0):
        print("-----------------------------------")
        print("Don't forget to create a profile!")
        print("-----------------------------------")


def messageNoti(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM messages WHERE user_1='{username}';"
    )
    records = cur.fetchall()
    if (len(records) != 0):
        print("-----------------------------------")
        print("You have messages waiting for you!")
        print("-----------------------------------")


def numberOfJobsNoti(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM jobs WHERE name='{username}';"
    )
    records = cur.fetchall()

    print("-----------------------------------")
    print("You have currently applied for ", len(records), " jobs!")
    print("-----------------------------------")
