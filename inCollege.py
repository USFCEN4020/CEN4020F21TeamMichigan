from authorization import isAuthorized
from add_user import canAdd, addUser, totalAccount
from find_user import findUser
from navigation_links import usefulLink, importantLink

# Handles logins


def login():
    from user_page import userPage
    username = input("Username: ")
    password = input("Password: ")
    next = isAuthorized(username, password)
    if (next):
        print('working')
        print("Type your option to proceed: \n 1. View Useful Links\n 2. View InCollege Important Links\n 3. Continue to user page")
        option = input()
        while (option != "1" and option != "2" and option != "3"):
            print("Invalid option")
            option = input()
        if (option == "1"):
            usefulLink()
        elif (option == "2"):
            importantLink(username)
        else:
            userPage(username)

    else:
        print("Login failed...")
        print("Please try again")
        login()


# handles signups
def signup():
    response = totalAccount()
    if(canAdd(response)):
        addUser()
        print("Thank you for signing up!")
        print("Now log in with your new username and password")
        login()
    else:
        print("All permitted accounts have been created, please come back later")


def main():
    print(" ")
    print("---welcome to inCollege!---")

    print("Please type your option:\n 1. View Useful Links\n 2. View InCollege Important Links\n 3. Continue to InCollege")
    print("---------------")
    choice = input()

    if choice == "1":
        usefulLink()
    elif choice == "2":
        importantLink(None)
    elif choice == "3":
        print("My Story:")
        print("I had a low GPA and no experience while in college. My LinkedIn profile was blank because I hadn't done anything yet. That was until I found inCollege!")
        print(
            "Now I have a job and can start paying by my student loans. Thanks inCollege!")
        print("To see my story type 'video'")
        print("Connect with others type 'connect'")
        print("Please type 'login' to log in to your account")
        print("or type 'signup' to create a new account")

        option = input()
        convert = str(option).lower()

        # interprests user input
        if (convert == "login"):
            login()
        elif (convert == "signup"):
            signup()
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
                    login()
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
