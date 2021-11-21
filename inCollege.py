from authorization import isAuthorized
from add_user import canAdd, addUser, totalAccount
from find_user import findUser
from navigation_links import usefulLink, importantLink
from user_profile import updateProfile, viewProfile
from db_connection import createTables
from db_connection import db_conn
from notifications import jobNoti, messageNoti, profileNoti
from notifications import jobNoti, messageNoti, profileNoti, checkNewJobs, checkNewUsers, checkDeletedJobs
from training import trainingMenu, courses
from input_API import startup_API, myCollegeProfiles, myCollegeJobsOutput, myCollegeUsers,myCollegeTraining, myCollegeAppliedJob, myCollegeSavedJobs
# Handles logins


def login(startpage):
    username = input("Username: ")
    password = input("Password: ")
    next = isAuthorized(username, password)
    if (next):
        if (startpage == 1):
            mainMenu(username)
        elif (startpage == 0):
            courses(username)
            myCollegeTraining()
    else:
        print("Login failed...")
        print("Please try again")
        login(1)

# this function executes a querey to see how many pending friend requests
# a user has
# it returns all the rows where the current user is one of the two users and
# where pending is true


def findPendingFriendRequests(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM friends WHERE (user_2='{username}') AND (pending = TRUE);"
    )
    return cur.fetchall()


def mainMenu(username):

    # checking if they have any friend requests
    results = findPendingFriendRequests(username)
    if len(results) > 0:
        print("You have ", len(results),
              " new friend requests \nCheck them out in the Show my Network option in the user page!")

    while True:
        from user_page import userPage
        print('working')
        jobNoti(username)
        profileNoti(username)
        messageNoti(username)
        checkNewJobs(username)
        checkDeletedJobs(username)
        checkNewUsers(username)
        print("Type your option to proceed: \n 1. View Useful Links\n 2. View InCollege Important Links\n 3. Edit Profile\n 4. View Profile\n 5. InCollege Learning\n 6. Continue to user page")
        option = int(input())
        while not (option > 0 and option < 7):
            print("Invalid option")
            option = input()
        if (option == 1):
            usefulLink()
        elif (option == 2):
            print(username)
            importantLink(username)
        elif (option == 3):
            updateProfile(username)
        elif (option == 4):
            viewProfile(username)
        elif (option == 5):
            courses(username)
            myCollegeTraining()
        else:
            userPage(username)


# handles signups
def signup():
    response = totalAccount()
    if(canAdd(response)):
        addUser()
        myCollegeProfiles()
        print("Thank you for signing up!")
        print("Now log in with your new username and password")
        login(1)
    else:
        print("All permitted accounts have been created, please come back later")


def main():
    createTables()
    startup_API()
    myCollegeJobsOutput()
    myCollegeUsers()
    myCollegeTraining()
    myCollegeAppliedJob()
    myCollegeSavedJobs()
    print(" ")
    print("---welcome to inCollege!---")

    print("Please type your option:\n 1. View Useful Links\n 2. View InCollege Important Links\n 3. Training\n 4. Continue to InCollege")
    print("---------------")
    choice = input()

    if choice == "1":
        usefulLink()
    elif choice == "2":
        importantLink("None")
    elif choice == "3":
        trainingMenu()
    elif choice == "4":
        print("My Story:")
        print("I had a low GPA and no experience while in college. My LinkedIn profile was blank because I hadn't done anything yet. That was until I found inCollege!")
        print(
            "Now I have a job and can start paying back my student loans. Thanks inCollege!")
        print("To see my story type 'video'")
        print("Connect with others type 'connect'")
        print("Please type 'login' to log in to your account")
        print("or type 'signup' to create a new account")

        option = input()
        convert = str(option).lower()

        # interprests user input
        if (convert == "login"):
            login(1)
        elif (convert == "signup"):
            signup()
            myCollegeUsers()
        elif (convert == "video"):
            print("Video is now playing")
            main()
        elif (convert == "connect"):
            first = input("Enter their first name: ")
            last = input("Enter their last name: ")
            if (findUser(first, last)):
                print("They are a part of the InCollege system")
                print("Type 'login' to login or 'signup' to signup: ")
                ls = input()
                conv = str(ls).lower()
                if (conv == "signup"):
                    signup()
                else:
                    login(1)
            else:
                print("They are not yet a part of the InCollege system yet")
                main()
        else:
            print("Invalid option")
            main()
    else:
        print("Invalid choice.")
        main()


if __name__ == "__main__":
    main()
