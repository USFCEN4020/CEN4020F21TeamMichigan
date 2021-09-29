from inCollege import login
from intership_page import jobSearch

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

    print("-----------------------------------------")
    print("Please select one of the three options")
    print("1.   Find someone you know")
    print("2.   Learn a skill")
    print("3.   Log out")
    print("4.   job Search")
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
    else:
        print("\nPlease enter a valid input\n")
        userPage()


"""
Page under construction
"""


def findSomeonePage():
    underConstruction()
    userPage()


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
