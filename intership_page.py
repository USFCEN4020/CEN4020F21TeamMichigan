from db_connection import db_conn
from add_user import canAdd

"""
    This file will operate the intership_page. Functionality is limited to creating a job post.(9/25/21)
"""

# Job Search option selected.
def jobSearch(userName):
    print("-----------------------------------------")
    print("Please select one of the three options")
    print("1.   Post Job")
    print("2.   Go Back")
    print("-----------------------------------------")
    
    usr_input = int(input("Please enter your selection:\t"))
    
    if(usr_input == 1):
        response = totalAccountsJobs()
        if(canAdd(response)): # Check to make sure only 5 jobs created.
            postJob(userName)
        else:
            print("\nToo many job posts currently\n")
            jobSearch(userName)
    elif(usr_input == 2):
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