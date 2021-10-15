from inCollege import login
from intership_page import jobSearch
from db_connection import db_conn

"""
under construction function to print
under construction for functions 
that are under construction
"""


def underConstruction():
    print("\nThis option is Under Construction\nReturning...")


"""
function that runs after a user successfully logs in 
here a user has 3 options
learn a new skill
find someone you know
log out
"""


def userPage(userName):
    while True:
        print("-----------------------------------------")
        print("Please select one of the three options")
        print("1.   Find someone you know")
        print("2.   Learn a skill")
        print("3.   Log out")
        print("4.   job Search")
        print("5.   Go Back")
        print("-----------------------------------------")

        usr_input = int(input("Please enter your selection:\t"))

        if usr_input == 1:
            findSomeonePage()
        elif usr_input == 2:
            learnSkillPage(userName)
        elif usr_input == 3:
            login()
        elif usr_input == 4:
            jobSearch(userName)
        elif usr_input == 5:
            return
        else:
            print("\nPlease enter a valid input\n")
            userPage()

#this function takes two usernames and adds them to the table of friends
#with pending = false
def makeFriends(user_1, user_2):
    if user_1 == user_2:
        return False
    pending = True
    conn = db_conn()
    cur = conn.cursor()
    #make sure that the two users are not already friends
    cur.execute(
        f"SELECT * FROM friends WHERE (user_1 = '{user_1}' AND user_2 = '{user_2}') OR (user_1 = '{user_2}' AND user_2 = '{user_1}')"
    )
    results = cur.fetchall()
    if len(results) != 0:
        print("You are already friends")
        return

    cur.execute(
        f"INSERT INTO friends(user_1, user_2, pending) VALUES('{user_1}', '{user_2}', '{pending}');"
    )


#searches the database for 
def lastNameSearch(user,lastname):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM auth WHERE last_name = '{lastname}' AND NOT username = '{user}';"
    )
    results = cur.fetchall()
    if len(results) == 0:
        print("There are no users with this last name")
        return NULL

    for i in range(len(results)):
        print(results[i])
    
    if makeFriends(user, results[0]):
        print("Friend request pending")
    
    




#this funciton prompts the user to enter a search method and 
def findSomeonePage(username):
    while True:
        print("Find someone by searching by:\n1.\tLast Name\n2.\tUniversity\n3.\tMajor\n4.\tGo Back")
        search_method = int(input())

        if search_method == 1:
            lastname = input("Please enter a last name")
            usrname = lastNameSearch(username, lastname)
            if usrname == NULL:
                print("Please try again\n")
                continue
            
        elif search_method == 2:
            uni = input("Please enter a Univeristy")
            universitySearch()

        elif search_method == 3:
            major = input("Please enter a Major")
            majorSearch()

        elif search_method == 4:
            return



"""
This page gives the user 5 skills to learn and gives the option to 
return back to the userPage
"""


def learnSkillPage(userName):
    print("\n\n-----------------------------------------")
    print("Choose a new skill to learn")
    print("1.   Coding skills")
    print("2.   People skills")
    print("3.   Management skills")
    print("4.   Analytical skills")
    print("5.   IT skills")
    print("6.   Go back")
    print("-----------------------------------------")

    usr_input = int(input("Please make a selection:\t"))

    if usr_input == 1:
        underConstruction()
        learnSkillPage()
    elif usr_input == 2:
        underConstruction()
        learnSkillPage()
    elif usr_input == 3:
        underConstruction()
        learnSkillPage()
    elif usr_input == 4:
        underConstruction()
        learnSkillPage()
    elif usr_input == 5:
        underConstruction()
        learnSkillPage()
    elif usr_input == 6:
        print("Returning...")
        userPage(userName)
    else:
        print("Please enter a valid input")
        learnSkillPage()
