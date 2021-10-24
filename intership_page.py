from db_connection import db_conn
from add_user import canAdd

"""
    This file will operate the intership_page. Functionality is limited to creating a job post.(9/25/21)
"""

# Job Search option selected.
def jobSearch(userName):
    print("-----------------------------------------")
    print("Please select one of the four options")
    print("1.   Post Job")
    print("2.   Delete Job")
    print("3.   See Job List")
    print("4.   Go Back")
    print("-----------------------------------------")
    
    usr_input = int(input("Please enter your selection:\t"))
    
    if(usr_input == 1):
        response = totalAccountsJobs()
        if(canAdd(response)): # Check to make sure only 10 jobs created.
            postJob(userName)
        else:
            print("\nToo many job posts currently\n")
            jobSearch(userName)
    elif(usr_input == 2):
        delJob = deleteJob(userName)
        if (delJob == 0):
            print("I'm sorry, you've never posted a job with that title.")
            jobSearch(userName)
        else:
            print("The job post has been succesfully deleted.")
            jobSearch(userName)
    elif(usr_input == 3): #Challenge 6
        seen = listJobs(userName)
        if (seen):
            jobSearch(userName)
    elif(usr_input == 4):
        try:
            from user_page import userPage # Import userPage. Note try/except not required.
            userPage(userName)            
        except:
            print("Error importing userPage")
    else:
        print("\nPlease enter a valid input\n")
        jobSearch(userName)
    
# Post Job option selected from Job Search.
def postJob(userName):
    """Every job that is posted will have five parts: a title, a description, the employer, a location, and a salary."""
    title = input("Please enter title: ")
    description = input("Please enter description: ")
    employer = input("Please enter employer: ")
    location = input("Please enter location: ")
    salary = input("Please enter salary: ")
    
    #Add job post entry into database.
    conn = db_conn()
    cur = conn.cursor()
    query = f"INSERT INTO jobs (title, description, employer, location, name, salary) VALUES ('{title}', '{description}', '{employer}', '{location}', '{userName}', '{salary}');"
    cur.execute(query, (title, description, employer, location, userName, salary))
    conn.commit()
    jobSearch(userName)
    return 1

# This is not the same as totalAccount it is specific to jobs.
def totalAccountsJobs():
    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # counts number of users
    cur.execute("SELECT COUNT(*) FROM jobs;")
    return cur.fetchall()


################Challenge 6################
#Delete a job posted by the user.
def deleteJob(userName):
    title = input("Please enter the job title: ")
    
    #Connect to Database
    conn = db_conn()
    cur = conn.cursor()
    #seach db for job
    cur.execute(f"SELECT COUNT(*) FROM jobs WHERE name='{userName}' AND title='{title}';")
    exists = cur.fetchall()
    if(exists[0][0] < 1):
        return 0
    else:
        query = f"DELETE FROM jobs WHERE name='{userName}' AND title='{title}';"
        cur.execute(query)
        conn.commit()
        return 1

#Challenge 6
def listJobs(userName):
    #Connect to Database
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT title FROM jobs;")
    jobList = cur.fetchall()
    print("Current job listings: ")
    for elem in jobList:
        print("- " + elem[0])

    print("-----------------------------------------")
    print("Please select one of the four options")
    print("1.   See Job Info")
    print("2.   Apply to Job")
    print("3.   Save Job")
    print("4.   Go Back")
    print("-----------------------------------------")
    response = int(input("Please enter your selection:\t"))
    if(response == 1):
        if(jobInfo(userName)):
            listJobs(userName)
        else:
            listJobs(userName)
    elif(response == 2):
        applied = applyJob(userName)
        if(applied == 1):
            print("Successfully Applied to job!")
            listJobs(userName)
        else:
            print("Error in applying. You can't apply to a job you posted or doesn't exist.")
            listJobs(userName)
    elif response == 3:
        if saveJob(userName):
            print("Job saved")
        else:
            print("Error saving job")
            listJobs(userName)
    else:
        jobSearch(userName)
    return 1

#Challenge 6
def jobInfo(userName):
    title = input("Please enter title of job post you wish to view:\t")
    if(title):
        print("Searching...")
    #Connect to Database
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM jobs WHERE title='{title}';")
    info = cur.fetchall()
    cur.execute(f"SELECT * FROM applications WHERE title = '{title}' AND id = '{userName}';")
    apps = cur.fetchall()
    print("Title: " + info[0][1])
    print("Description: " + info[0][2])
    print("Employer: " + info[0][3])
    print("Location: " + info[0][4])
    print("Salary: " + info[0][5])
    if not apps[0][6]:
        print("Already applied!")
    return 1

#Challenge 6
def applyJob(userName):
    title = input("Please enter title of job you want to apply for:\t")
    #Connect to Database
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM jobs WHERE title='{title}' AND name != '{userName}';")
    info = cur.fetchall()[0]
    if (info[0] == 0):
        return 0
    else:
        grad = input("Please enter your graduation date:\t")
        start = input("Please enter the date you wish to start:\t")
        reason = input("Please share why you'd be a good fit for this role:\t")
        query = f"INSERT INTO applications (title, name, grad_date, start_date, reason, pending) VALUES ('{title}', '{userName}', '{grad}', '{start}', '{reason}', FALSE);"
        cur.execute(query, (title, userName, grad, start, reason))
        conn.commit()
        return 1




def listAppliedJobs(username):
    print("Here are the jobs you have applied for")
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM applications WHERE name ='{username}';")
    results = cur.fetchall()
    for i in range(len(results)):
        print(i,". ", results[i][1])
    return 1

def listNotAppliedJobs(username):
    print("Here are the jobs you have not applied for")
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM applications WHERE name !='{username}';")
    results = cur.fetchall()
    for i in range(len(results)):
        print(i,". ", results[i][1])
    return 1

def saveJob(username):
    title = input("Please enter the title of the job you would like to save")
    conn = db_conn()
    cur = conn.cursor()
    query = f"INSERT INTO applications (title, name, grad_date, start_date, reason, pending) VALUES ('{title}', '{username}', ' ', ' ', ' ', TRUE);"
    cur.execute(query, (title, username, " ", " ", " "))
    conn.commit()
    return 1



def listSavedJobs(username):
    print("Here are all your saved jobs")
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM applications WHERE id = '{username}' AND pending = TRUE;")
    results = cur.fetchall()
    for elements in results:
        print(elements[1])
    
    usr_in = input("Enter 1 to go back or 2 to remove a saved job")
    if usr_in == 1:
        return 1
    else:
        title = input("Please enter the title of the job you'd like to remove")
        cur.execute(f"DROP * FROM applications WHERE id = '{username} AND pending = TRUE AND title = '{title}'")
        conn.commit()
        print("Saved job removed")
        return 1


################End of Challenge 6################