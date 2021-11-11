# incomplete function
def courses(username):
    print("Which of these trending courses do you want to learn? Type your option: ")
    print("1. How to use inCollege learning")
    print("2. Train the trainer")
    print("3. Gamification of learning")
    print("4. Understanding the Architectural Design Process")
    print("5. Project Management Simplified")
    print("4. Go back")


def trainingEducation():
    print("Type your option to view: ")
    print("1. Data Structures and Algorithms")
    print("2. Web Development")
    print("3. Database Design")
    print("4. Programming Languages")
    print("5. Go back")
    option = input()
    if option == "1" or option == "2" or option == "3" or option == "4":
        print("Under construction!")
        trainingEducation()
    elif option == "5":
        trainingMenu()
    else:
        print("Invalid option!")
        trainingEducation()


def businessAnalysis():
    from inCollege import login
    print("Which of these trending courses do you want to learn? Type your option: ")
    print("1. How to use inCollege learning")
    print("2. Train the trainer")
    print("3. Gamification of learning")
    print("4. Go back")
    print("Not seeing what you're looking for? Sign in to see all 7,609 results.")
    option = input()
    if (option == "1" or option == "2" or option == "3"):
        login()
    elif (option == "4"):
        trainingMenu()
    else:
        print("Invalid option")
        businessAnalysis()


def trainingMenu():
    from inCollege import main
    print("Type your option to view: ")
    print("1. Training and Education")
    print("2. IT Help Desk")
    print("3. Business Analysis and Strategy")
    print("4. Security")
    print("5. Go back")
    option = input()
    if (option == "1"):
        trainingEducation()
    elif (option == "2"):
        print("Coming Soon!")
        trainingMenu()
    elif (option == "3"):
        businessAnalysis()
    elif (option == "4"):
        print("Coming Soon!")
        trainingMenu()
    elif (option == "5"):
        main()
    else:
        print("Invalid option")
        trainingMenu()
