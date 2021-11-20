from db_connection import db_conn

# incomplete function
def courses(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM courses WHERE username='{username}'"
    )
    result = cur.fetchall()
    courseList = ["1. How to use inCollege learning", "2. Train the trainer", "3. Gamification of learning","4. Understanding the Architectural Design Process", "5. Project Management Simplified"]
    print(result)
    print("Which of these trending courses do you want to learn? Type your option: ")
    if (checkCourse(username,"1")):
        print("1. How to use inCollege learning- Completed")
    else:
        print("1. How to use inCollege learning")
    if (checkCourse(username,"2")):
        print("2. Train the trainer - Completed")
    else:
        print("2. Train the trainer")
    if (checkCourse(username,"3")):
        print("3. Gamification of learning - Completed")
    else:
        print("3. Gamification of learning")
    if (checkCourse(username,"4")):
        print("4. Understanding the Architectural Design Process - Completed")
    else:
        print("4. Understanding the Architectural Design Process")
    if (checkCourse(username,"5")):
        print("5. Project Management Simplified - Completed")
    else:
        print("5. Project Management Simplified")
    print("6. Go back")
    option = input()
    completedCourse = courseList[int(option)-1]
    if (checkCourse(username, option)):
        print("You have already taken this course, do you want to take it again? Enter Yes or No")
        selection = input()
        if (selection == "No" or selection == "no"):
            print("Course Cancelled")
            courses(username)
        else:
            print("You have now completed this training")
            
    if (int(option) < 7 ):
        print("You have now completed this training")
        cur.execute(
            f"INSERT INTO courses(username, courseName, courseNumber)  VALUES('{username}','{completedCourse}','{option}');"
        )
        conn.commit()

def checkCourse(username, courseNumber):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM courses WHERE username='{username}' AND courseNumber ='{courseNumber}'"
    )
    if (cur.fetchone() is None):
        return 0
    else:
        return 1



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
        login(0) 
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
