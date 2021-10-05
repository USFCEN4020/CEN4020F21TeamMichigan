from db_connection import db_conn


def updateTitle(username):
    print("Enter your title: ")
    title = input()

    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute(
        f"UPDATE profile SET title = '{title}' WHERE username ='{username}';")
    conn.commit()

    print("Update successfully!")
    updateProfile(username)


def updateMajor(username):
    print("Enter your major: ")
    # major starts w uppercase and the rest is lower case
    major = input()

    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute(
        f"UPDATE profile SET major = '{major}' WHERE username ='{username}';")
    conn.commit()
    print("Update successfully!")
    updateProfile(username)


def updateUniName(username):
    print("Enter your university: ")
    # university name starts w uppercase and the rest is lower case
    uni = input()

    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute(
        f"UPDATE profile SET university = '{uni}' WHERE username ='{username}';")
    conn.commit()
    print("Update successfully!")
    updateProfile(username)


def updateAbout(username):
    print("What should people know about you? ")
    # university name starts w uppercase and the rest is lower case
    abt = input()

    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute(
        f"UPDATE profile SET about = '{abt}' WHERE username ='{username}';")
    conn.commit()
    print("Update successfully!")
    updateProfile(username)


def updateExp(username):
    print("")
    print("Update successfully!")
    updateProfile(username)


def updateEdu(username):
    print("")
    print("Update successfully!")
    updateProfile(username)


def updateProfile(username):
    from inCollege import mainMenu
    print("Choose your option: ")
    print(" 1. Update Title\n 2. Update Major\n 3. Update University name\n 4. Update About\n 5. Update Experiences\n 6. Update Education\n 7. Go back")
    option = input()
    while (option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6' and option != '7'):
        print('Invalid option. Please re-enter: ')
        option = input()
    if (option == '1'):
        updateTitle(username)
    elif (option == '2'):
        updateMajor(username)
    elif (option == '3'):
        updateUniName(username)
    elif (option == '4'):
        updateAbout(username)
    elif (option == '5'):
        updateExp(username)
    elif (option == '6'):
        updateEdu(username)
    else:
        mainMenu(username)


def viewProfile(username):
    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # get first name
    cur.execute(
        f"SELECT first_name FROM auth WHERE username ='{username}';")
    firstName = cur.fetchone()

    # get last name
    cur.execute(
        f"SELECT last_name FROM auth WHERE username ='{username}';")
    lastName = cur.fetchone()

    # get title
    cur.execute(
        f"SELECT title FROM profile WHERE username ='{username}';")
    title = cur.fetchone()

    # get major
    cur.execute(
        f"SELECT major FROM profile WHERE username ='{username}';")
    major = cur.fetchone()

    # get university
    cur.execute(
        f"SELECT about FROM profile WHERE username ='{username}';")
    uni = cur.fetchone()

    # get about info
    cur.execute(
        f"SELECT about FROM profile WHERE username ='{username}';")
    about = cur.fetchone()
    conn.commit()

    # display profile
    print('---------------------')
    print(firstName[0], end=" ")
    print(lastName[0])
    print('---------------------')

    print("Title: ", end="")
    print(title[0])

    print("Major: ", end="")
    print(major[0])

    print("University: ", end="")
    print(uni[0])

    print("About: ", end="")
    print(about[0])
