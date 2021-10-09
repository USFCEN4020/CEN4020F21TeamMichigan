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

    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()


    print("Enter 1 if you would like to add a work experience or 2 if you would like to edit a work experience")
    option = input()

    if option == 2:
        print("Here is your work experience")
        cur.execute("SELECT * FROM experiences")
        table = cur.fetchall()
        for row in table:
            print (row)
            print("\n")
        print("Please enter the title you would like to edit")
        titleInput = input()

    print("Please enter your job title")
    job = input()
    job = ' '.join(word[0].upper() + word[1:] for word in job.split())
    if option == 2:
        cur.execute(
            f"UPDATE experiences SET title = '{job}' WHERE username ='{username}';")
        conn.commit()

    print("Please enter your employer's name")
    employer = input()
    employer = ' '.join(word[0].upper() + word[1:] for word in employer.split())
    if option == 2:
        cur.execute(
            f"UPDATE experiences SET employer = '{employer}' WHERE username ='{username}';")
        conn.commit()

    print("Please enter your starting date (mm/dd/yy)")
    start_date = input()
    if option == 2:
        cur.execute(
            f"UPDATE experiences SET date_started = '{start_date}' WHERE username ='{username}';")
        conn.commit()

    print ("Please enter your ending date (mm/dd/yy)")
    end_date = input()
    if option == 2:
        cur.execute(
            f"UPDATE experiences SET date_ended = '{end_date}' WHERE username ='{username}';")
        conn.commit()
    
    print("Please enter the location of this job")
    location = input()
    location =' '.join(word[0].upper() + word[1:] for word in location.split())
    if option == 2:
        cur.execute(
            f"UPDATE experiences SET location = '{location}' WHERE username ='{username}';")
        conn.commit()

    print("Please enter a discription of your job")
    description =input()
    if option == 2:
        cur.execute(
            f"UPDATE experiences SET description = '{description}' WHERE username ='{username}';")
        conn.commit()

    if option != 2:
        cur.execute(
            f"INSERT INTO experiences (username ,title, employer, date_started, date_ended, location, description) VALUES('{username}', '{'job'}', '{'employer'}', '{'start_date'}', '{'end_date'}', '{'location'}', '{'description'}')")
        conn.commit()

    print("Update successfully!")
    updateProfile(username)


def updateEdu(username):

    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    print("Please enter the Univeristy you attended")
    university = input()
    university = ' '.join(word[0].upper() + word[1:] for word in university.split())
    cur.execute(
        f"UPDATE education SET school = '{university}' WHERE username ='{username}';")
    conn.commit()

    print("Please enter the degree recived")
    degree = input()
    degree = ' '.join(word[0].upper() + word[1:] for word in degree.split())
    cur.execute(
        f"UPDATE education SET degree = '{degree}' WHERE username ='{username}';")
    conn.commit()

    print("Please enter the year you graduated (yyyy)")
    year = input()
    cur.execute(
        f"UPDATE education SET year_attended = '{year}' WHERE username ='{username}';")
    conn.commit()


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

    # get title info
    cur.execute(
        f"SELECT title FROM experiences WHERE username ='{username}';")
    title = cur.fetchall()
    conn.commit()

    # get employer info
    cur.execute(
        f"SELECT employer FROM experiences WHERE username ='{username}';")
    employer = cur.fetchall()
    conn.commit()

    # get start date info
    cur.execute(
        f"SELECT date_started FROM experiences WHERE username ='{username}';")
    date_started = cur.fetchall()
    conn.commit()

    # get end date info
    cur.execute(
        f"SELECT date_ended FROM experiences WHERE username ='{username}';")
    date_ended = cur.fetchall()
    conn.commit()

    # get location info
    cur.execute(
        f"SELECT location FROM experiences WHERE username ='{username}';")
    location = cur.fetchall()
    conn.commit()

    # get description info
    cur.execute(
        f"SELECT description FROM experiences WHERE username ='{username}';")
    description = cur.fetchall()
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

    print('---------------------')
    print('Past Experience')
    print('---------------------')




