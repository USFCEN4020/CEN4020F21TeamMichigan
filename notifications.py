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
<<<<<<< Updated upstream
=======

 
# Checks to see if there are new jobs with sync to user.
def checkNewJobs(username):

    # Get the lists of the new jobs and get the list of the last known jobs the user had.
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM jobs;"
    )
    newJobs = cur.fetchall()
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM priorjobs WHERE username='{username}';"
    )
    oldJobs = cur.fetchall()
    
    # Compare the new and old and see what is different.
    newJobNumber = 0
    newJobTitles = []
    for i in range(0, len(newJobs)):
        tempTitle = newJobs[i][1]
        booleanFlag = 0
        for j in range(0, len(oldJobs)):
            if(tempTitle == oldJobs[j][1]):
                booleanFlag = 1
        if(booleanFlag == 0):
            newJobNumber += 1
            newJobTitles.append(newJobs[i][1])
            conn = db_conn()
            cur = conn.cursor()
            cur.execute(
                f"INSERT INTO priorjobs(username, jobTitle) VALUES('{username}', '{newJobs[i][1]}');"
            )
            conn.commit()
        
    # Print every new job that wasn't in the past jobs the user previsouly knew.
    for i in range(0, newJobNumber):
        print("-----------------------------------")
        print("A new job", newJobTitles[i], "has been posted")
        print("-----------------------------------")
        
    return 1; # All has gone well.

"""def checkDeletedJobs(username):
    # Get the lists of the new jobs and get the list of the last known jobs the user had.
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM jobs;"
    )
    newJobs = cur.fetchall()
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM priorusers WHERE username='{username}';"
    )
    oldJobs = cur.fetchall()"""
    
# Checks to see if there are new jobs with sync to user.
def checkNewUsers(username):

    # Get the lists of the new jobs and get the list of the last known jobs the user had.
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM auth;"
    )
    newUsers = cur.fetchall()
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM priorusers WHERE username='{username}';"
    )
    oldUsers = cur.fetchall()
    
    # Compare the new and old and see what is different.
    newUserNumber = 0
    newFirstName = []
    newLastName = []
    for i in range(0, len(newUsers)):
        tempTitle = newUsers[i][0]
        booleanFlag = 0
        for j in range(0, len(oldUsers)):
            if(tempTitle == oldUsers[j][1]):
                booleanFlag = 1
        if(booleanFlag == 0):
            newUserNumber += 1
            newFirstName.append(newUsers[i][2])
            newLastName.append(newUsers[i][3])
            conn = db_conn()
            cur = conn.cursor()
            cur.execute(
                f"INSERT INTO priorusers(username, otheruser) VALUES('{username}', '{newUsers[i][0]}');"
            )
            conn.commit()
        
    # Print every new job that wasn't in the past jobs the user previsouly knew.
    for i in range(0, newUserNumber):
        print("-----------------------------------")
        print(newFirstName[i], newLastName[i], "has joined InCollege")
        print("-----------------------------------")
        
    return 1; # All has gone well.
>>>>>>> Stashed changes
