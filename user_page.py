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
        print("Please select one of the six options")
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


# this function finds all the current friends that the user has and returns them
# as a tuple of tuples of the rows that matched the query
# i.e. ((user_1 value, user_2 value, pending value),(user_1 value, user_2 value, pending value), ...)


# returns a list of tuples that contain a row from auth the the user is friends with
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
    if len(ret) == 0:
        return []
    return ret[0]


def displayFriendsProfile(username, first_name, last_name):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM profile WHERE username='{username}'"
    )
    result = cur.fetchall()
    print("----------------------------")
    print("Your Friend ", first_name, " ", last_name)
    print("----------------------------")
    print("Title: ", result[0][1])
    print("Major: ", result[0][2])
    print("University: ", result[0][3])
    print("About: ", result[0][4])
    cur.execute(
        f"SELECT * FROM education WHERE username='{username}'"
    )
    result = cur.fetchall()
    print("----------------------------")
    print("Education")
    print("----------------------------")
    print("School: ", result[0][1])
    print("Degree: ", result[0][2])
    print("Year Graduated: ", result[0][3])
    cur.execute(
        f"SELECT * FROM experiences WHERE username='{username}'"
    )
    result = cur.fetchall()
    print("----------------------------")
    print("Work History")
    print("----------------------------")
    for i in range(len(result)):
        print("Title: ", result[i][1])
        print("Employer: ", result[i][2])
        print("Start Date: ", result[i][3])
        print("End Date: ", result[i][4])
        print("Location: ", result[i][5])
        print("Discription: ", result[i][6])

    return 1

# this function deletes the row where the two users exist
# this effectively removes the friendship or it can also
# be used to reject friend requests


def removeFriend(user_1, user_2):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"DELETE FROM friends WHERE (user_1 = '{user_1}' AND user_2 = '{user_2}') OR (user_1 = '{user_2}' AND user_2 = '{user_1}');")
    conn.commit()
    return 1


def showNetwork(username):

    conn = db_conn()
    cur = conn.cursor()

    while True:
        print("----------------------------")
        pending_friends = findPendingFriendRequests(username)
        if len(pending_friends) > 0:
            print("You have ", len(pending_friends),
                  " pending friend requests")
        print("1.   View my Current Network")
        print("2.   View my Pending Friend Requests")
        print("3.   Go Back")

        usr_input = int(input())
        if usr_input == 1:
            friends = findUserFriends(username)
            if len(friends) == 0:
                print("You have no friends")
                continue
            print("Here is a list of people you have connected with:")
            for i in range(len(friends)):
                print(i, ".\t", friends[i][2], " ", friends[i][3])

            print(
                "If you want to display your friends profile press 1 if you could like to unfriend press 2")
            user_options = int(input())
            if user_options == 2:
                print("If you want to disconnect with someone enter their number or enter ", (len(
                    friends) + 1), " to return")
                user_in = int(input())
                if user_in == len(friends)+1:
                    continue
                removeFriend(username, friends[user_in][0])
                print("You are no longer friends with ",
                      friends[user_in][2], " ", friends[user_in][3])
            elif user_options == 1:
                displayFriendsProfile(
                    friends[i][0], friends[i][2], friends[i][3])

        elif usr_input == 2:
            while True:
                pending_friends = findPendingFriendRequests(username)
                #print("Pending friends: ", pending_friends)
                if len(pending_friends) == 0:
                    print("You have no friend requests")
                    break
                pen_friends = []
                for i in range(len(pending_friends)):
                    if pending_friends[i][0] != username:
                        pen_friends.append(pending_friends[i][0])
                    elif results[i][1] != username:
                        pen_friends.append(pending_friends[i][1])

                ret = []
                for i in range(len(pen_friends)):
                    cur.execute(
                        f"SELECT * FROM auth WHERE username='{pen_friends[i]}'"
                    )
                    ret.append(cur.fetchone())
                print("---------------------------------")
                print("Pending Friends:")

                for i in range(len(ret)):
                    print(i, ".\t", ret[i][2], " ", ret[i][3])
                print("Select one to accept or reject or press 3 to return")
                usr_in = int(input())
                if usr_in == 3:
                    break
                print(
                    "Would you like to:\n1.\taccept\n2.\treject\n3.\tignore \nthis friend request?")
                u_in = int(input())
                if u_in == 1:
                    confirmFriend(username, ret[usr_in][0])
                    print("You are now friends")
                elif u_in == 2:
                    removeFriend(username, ret[usr_in][0])
                    print("Friend request rejected")
                elif u_in == 3:
                    continue

        elif usr_input == 3:
            print("Returning...")
            return


def confirmFriend(user_2, user_1):
    removeFriend(user_1, user_2)
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO friends(user_1, user_2, pending)  VALUES('{user_1}','{user_2}',FALSE);"
    )
    conn.commit()
    return 1


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
    # make sure that the two users are not already friends
    cur.execute(
        f"SELECT * FROM friends WHERE (user_1 = '{user_1}' AND user_2 = '{user_2}') OR (user_1 = '{user_2}' AND user_2 = '{user_1}');"
    )
    results = cur.fetchall()
    if len(results) != 0:
        print("You are already friends")
        return True

    new_friend = f"INSERT INTO friends(user_1, user_2, pending) VALUES('{user_1}', '{user_2}', '{pending}');"
    cur.execute(new_friend, (user_1, user_2, pending))
    conn.commit()
    return True


# searches the database for the username of a user with a certain last name
def lastNameSearch(user, lastname):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM auth WHERE last_name = '{lastname}' AND username = '{user}';"
    )
    results = cur.fetchall()
    if len(results) == 0:
        print("There are no users with this last name")
        return True
    else:
        return False

    # if there are multiple users with the same last name then they will all be listed
    print("Are you looking for:")
    for i in range(len(results)):
        print(i, ". ", results[i][2], " ", results[i][3])
    if len(results) == 1:
        usr = int(input("Enter 0 to confirm friend request:\t"))
    else:
        usr = int(
            input("Please select which specific person you are refering to:\t"))

    if makeFriends(user, results[usr][0]):
        print("Friend request pending")

# searches for people who go to the same university


def universitySearch(username, uni):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM profile WHERE university = '{uni}' AND NOT username = '{username}';"
    )
    results = cur.fetchall()
    if len(results) == 0:
        print("There are no users that go to this school")
        return False

    same_school = []
    for i in range(len(results)):
        if results[i][0] != username:
            same_school.append(results[i][0])

    ret = []
    for i in range(len(same_school)):
        cur.execute(
            f"SELECT * FROM auth WHERE username='{same_school[i]}'"
        )
        ret.append(cur.fetchall())

    print("Are you looking for:")
    for i in range(len(ret)):
        print(i, ". ", ret[i][0])
    u_in = int(input())
    makeFriends(username, ret[u_in][0])


def majorSearch(username, major):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM profile WHERE major = '{major}' AND NOT username = '{username}';"
    )
    results = cur.fetchall()
    if len(results) == 0:
        print("There are no users that have this major")
        return False

    same_major = []
    for i in range(len(results)):
        if results[i][0] != username:
            same_major.append(results[i][0])

    ret = []
    for i in range(len(same_major)):
        cur.execute(
            f"SELECT * FROM auth WHERE username='{same_major[i]}'"
        )
        ret.append(cur.fetchall())

    print("Are you looking for:")
    for i in range(len(ret)):
        print(i, ". ", ret[i][0])
    u_in = int(input())
    makeFriends(username, ret[u_in][0])


# this funciton prompts the user to enter a search method and
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
            uni = input("Please enter a Univeristy:\t")
            universitySearch(username, uni)

        elif search_method == 3:
            major = input("Please enter a Major:\t")
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
