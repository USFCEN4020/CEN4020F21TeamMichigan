from inCollege import login, findPendingFriendRequests
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


def userPage(username):
    while True:
        print("-----------------------------------------")
        print("Please select one of the three options")
        print("1.   Find someone you know")
        print("2.   Learn a skill")
        print("3.   Log out")
        print("4.   job Search")
        print("5.   Go Back")
        print("6.   Show my Network")
        print("-----------------------------------------")

        usr_input = int(input("Please enter your selection:\t"))

        if usr_input == 1:
            findSomeonePage(username)
        elif usr_input == 2:
            learnSkillPage(username)
        elif usr_input == 3:
            login()
        elif usr_input == 4:
            jobSearch(username)
        elif usr_input == 5:
            return
        elif usr_input == 6:
            showNetwork(username)
        else:
            print("\nPlease enter a valid input\n")
            userPage()


#this function finds all the current friends that the user has and returns them
#as a tuple of tuples of the rows that matched the query
#i.e. ((user_1 value, user_2 value, pending value),(user_1 value, user_2 value, pending value), ...)
#returns a list of tuples that contain a row from auth the the user is friends with
def findUserFriends(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM friends WHERE (user_1='{username}' OR user_2='{username}') AND (pending = FALSE);"
    )
    results = cur.fetchall()
    friends = []
    for i in range(len(results)):
        if results[i][0] != username:
            friends.append(results[i][0])
        elif results[i][1] != username:
            friends.append(results[i][1])
        
    ret = []
    for i in range(len(friends)):
        cur.execute(
            f"SELECT * FROM auth WHERE username='{friends[i]}'"
        )
        ret.append(cur.fetchall())

    return ret


#this function deletes the row where the two users exist
#this effectively removes the friendship or it can also
#be used to reject friend requests
def removeFriend(user_1, user_2):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"DELETE * FROM friends WHERE (user_1 = '{user_1}' AND user_2 = '{user_2}') OR (user_1 = '{user_2}' AND user_2 = '{user_1}');"
    )

def showNetwork(username):
    while True:
        print("----------------------------")
        pending_friends = findPendingFriendRequests(username)
        if len(pending_friends) > 0:
            print("You have ", len(pending_friends), " pending friend requests")
        print("1.   View my Current Network")
        print("2.   View my Pending Friend Requests")
        print("#.   Go Back")

        usr_input = int(input())
        if usr_input == 1:
            friends = findUserFriends(username)
            if len(friends) == 0:
                print("You have no friends")
                continue
            print("Here is a list of people you have connected with")
            for i in range(len(friends)):
                print(i, ".\t", friends[i][3], " ", friends[i][4])
            print("If you want to disconnect with someone enter their number or enter ", (len(friends) + 1) , " to return")
            user_in = int(input())
            if user_in == len(friends)+1:
                continue
            removeFriend(username, friends[i][0])
        elif usr_input == 2:
            pending_friends = findPendingFriendRequests(username)
        elif usr_input == 3:
            print("Returning...")
            return

        



"""
this function takes two usernames and adds them to the table 
of friends with pending = false
The friends table is set up as an edge list graph that only
stores the list of edges that connect users to make a graph.
it also stores a pending value that is true when 
"""
def makeFriends(user_1, user_2):
    if user_1 == user_2:
        return False
    pending = True
    conn = db_conn()
    cur = conn.cursor()
    #make sure that the two users are not already friends
    cur.execute(
        f"SELECT * FROM friends WHERE (user_1 = '{user_1}' AND user_2 = '{user_2}') OR (user_1 = '{user_2}' AND user_2 = '{user_1}');"
    )
    results = cur.fetchall()
    if len(results) != 0:
        print("You are already friends")
        return False

    cur.execute(
        f"INSERT INTO friends(user_1, user_2, pending) VALUES('{user_1}', '{user_2}', '{pending}');"
    )
    return True


#searches the database for the username of a user with a certain last name
def lastNameSearch(user,lastname):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM auth WHERE last_name = '{lastname}' AND NOT username = '{user}';"
    )
    results = cur.fetchall()
    if len(results) == 0:
        print("There are no users with this last name")
        return True

    #if there are multiple users with the same last name then they will all be listed
    print("Are you looking for:")
    for i in range(len(results)):
        print(i, ". ", results[i][2], " ", results[i][3])
    if len(results) == 1:
        usr = input("Enter 1 to confirm friend request:\t")
        usr = usr - 1
    else:
        usr = input("Please select which specific person you are refering to:\t")    

    if makeFriends(user, results[usr][0]):
        print("Friend request pending")
    
#searches for people who go to the same university
def universitySearch(username, uni):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM profile WHERE university = '{uni}' AND NOT username = '{user}';"
    )
    results = cur.fetchall()
    if len(results) == 0:
        print("There are no users that go to this school")
        return
    
    print("Are you looking for:")
    for i in range(len(results)):
        print(i,". ", results[i][0])





#this funciton prompts the user to enter a search method and 
def findSomeonePage(username):
    while True:
        print("------------------------------------")
        print("Find someone by searching by:\n1.\tLast Name\n2.\tUniversity\n3.\tMajor\n4.\tGo Back")
        search_method = int(input())

        if search_method == 1:
            lastname = input("Please enter a last name:\t")
            usrname = lastNameSearch(username, lastname)
            if usrname:
                print("Please try again\n")
                continue
            
        elif search_method == 2:
            uni = input("Please enter a Univeristy")
            universitySearch(username, uni)

        elif search_method == 3:
            major = input("Please enter a Major")
            majorSearch(username, major)

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
