# Epic #10
from db_connection import db_conn
import fileinput

# Epic #10


def add_usr_API(username, first, last, password):
    # Open a cursor to perform database operations
    conn = db_conn()
    cur = conn.cursor()

    # if user already exists then it returns 0
    cur.execute(
        f"SELECT * FROM auth WHERE username='{username}';"
    )
    if cur.fetchone() is None:
        return 0

    # In the event that the user data is already added.
    try:
        planInsert = 'standard'
        # insert user info
        auth = f"INSERT INTO auth(username, password, first_name, last_name, plan) VALUES('{username}', '{password}', '{first}', '{last}', '{planInsert}');"
        control = f"INSERT INTO control(username, email, sms, advertising, language) VALUES('{username}', '{1}', '{1}', '{1}', '{'English'}');"
        profile = f"INSERT INTO profile(username, title, major, university, about) VALUES('{username}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}');"
        experiences = f"INSERT INTO experiences(username, title, employer, date_started, date_ended, location, description) VALUES('{username}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}');"
        education = f"INSERT INTO education(username, school, degree, year_attended) VALUES('{username}', '{'NULL'}', '{'NULL'}', '{'NULL'}');"

        cur.execute(auth, (username, password, first, last, planInsert))
        cur.execute(control, (username, 1, 1, 1, 'English'))
        cur.execute(profile, (username, 'NULL', 'NULL', 'NULL', 'NULL'))
        cur.execute(experiences, (username, 'NULL', 'NULL',
                    'NULL', 'NULL', 'NULL', 'NULL'))
        cur.execute(education, (username, 'NULL', 'NULL', 'NULL'))

        conn.commit()
    except:
        print() #User data already added to database.
        
    return 1
# Epic #10


def add_job_API(inp):
    title = inp[0]
    des = ""
    for i in inp:
        if inp[0] == i:
            continue
        des = des + i
    try:
        conn = db_conn()
        cur = conn.cursor()
        query = f"INSERT INTO jobs (title, description, employer, location, name, salary) VALUES ('{title}', '{des}', '', '', '', '');"
        cur.execute(query, (title, des, "",
                    "", "", ""))
        conn.commit()
    except:
        print()
    return 1

# Epic #10


def add_training_API(training_prog):
    conn = db_conn()
    cur = conn.cursor()

    cur.execute(f"INSERT INTO training(description) VALUES('{training_prog}');")
    conn.commit()
    return 1


# Epic #10
def startup_API():

    #student account API
    first = last = password = usr =""
    try:
        file = open("studentAccounts.txt", 'r')
    except FileNotFoundError:
        print()
    if file != FileNotFoundError:
        for i in range(10):
            line = file.readline()
            if len(line) == 0:
                break
            print("test")
            line.split()
            usr = line[0]
            first = line[1]
            last = line[2]
            line = file.readline()
            password = line[0]
            line = file.readline()
            add_usr_API(usr, first, last, password)
    
    #Jobs API
    try:
        file = open("newJobs.txt")
    except FileNotFoundError:
        print()
    inp = []
    if file != FileNotFoundError:
        for line in file.readline():
            inp.append(line[0])
            if inp[-1].endswith("&&&"):
                add_job_API(inp)

    #training API
    try:
        file = open("newtraining.txt",'r')
    except FileNotFoundError:
        print()
    if file != FileNotFoundError:
        for line in file.readline():
            add_training_API(line)
            
    return 1


# Epic #10
def myCollegeJobsOutput():
    file = open("MyCollege_jobs.txt", "w")
    conn = db_conn()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM jobs;")

    results = cur.fetchall()

    if len(results) == 0:
        file.close()
        return 1

    for job in results:
        for i in range(len(job)):
            file.write(str(job[i]) + "\n")
        file.write("=====\n")
    file.close()
    return 1


def myCollegeProfiles():
    file = open("MyCollege_profiles.txt", "w")
    conn = db_conn()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM jobs;")

    results = cur.fetchall()

    if len(results) == 0:
        file.close()
        return 1

    for student in results:
        for elem in student:
            file.write(elem + "\n")
        file.write("=====\n")
    file.close()
    return 1


def myCollegeUsers():
    file = open("MyCollege_users.txt", "w")
    conn = db_conn()
    cur = conn.cursor()

    cur.execute(f"SELECT username, plan FROM auth;")

    results = cur.fetchall()
    if len(results) == 0:
        file.close()
        return 1

    for users in results:
        for elem in users:
            file.write(elem + " ")
        file.write("\n")
    file.close()
    return 1


def myCollegeTraining():
    file = open("MyCollege_training.txt", "w")
    conn = db_conn()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM auth;")

    results = cur.fetchall()

    if len(results) == 0:
        file.close()
        return 1

    for users in results:
        for elem in users:
            file.write(elem + "\n")
            cur.execute(
                f"SELECT courseName FROM courses WHERE username = '{elem}';")
            courseList = cur.fetchall()
            for x in courseList:
                for y in x:
                    file.write(y + "\n")

        file.write("=====\n")
    file.close()
    return 1


def myCollegeAppliedJob():
    file = open("MyCollege_appliedJobs.txt", "w")
    conn = db_conn()
    cur = conn.cursor()

    cur.execute(f"SELECT title FROM jobs;")

    results = cur.fetchall()

    if len(results) == 0:
        file.close()
        return 1

    for users in results:
        for elem in users:
            file.write(elem + "\n")
            cur.execute(
                f"SELECT name, reason FROM applications WHERE title = '{elem}';")
            nameReason = cur.fetchall()
            for x in nameReason:
                for y in x:
                    file.write(y + "\n")

        file.write("=====\n")
    file.close()
    return 1


def myCollegeSavedJobs():
    file = open("MyCollege_savedJobs.txt", "w")
    conn = db_conn()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM auth;")

    results = cur.fetchall()

    if len(results) == 0:
        file.close()
        return 1

    for users in results:
        for elem in users:
            file.write(elem + "\n")
            cur.execute(
                f"SELECT title FROM applications WHERE pending = 'true' AND name = '{elem}';")
            jobTitle = cur.fetchall()
            for x in jobTitle:
                for y in x:
                    file.write(y + "\n")

        file.write("=====\n")
    file.close()
    return 1
