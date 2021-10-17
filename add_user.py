from db_connection import db_conn

# Checks if there is room for a new account


def canAdd(response):
    # print(response)
    if (response[0][0] > 9):
        return 0
    else:
        return 1


def totalAccount():
    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # counts number of users
    cur.execute("SELECT COUNT(*) FROM auth;")
    return cur.fetchall()


def validatePassword(password):
    cap = False
    dig = False
    alp = False
    for elm in password:
        if (elm.isupper()):
            cap = True
        elif (elm.isnumeric()):
            dig = True
        elif (not elm.isalnum()):
            alp = True
        else:
            continue

    if (cap and dig and alp and len(password) >= 8 and len(password) <= 12):
        return 1
    else:
        return 0

# Adds user to the database


# this function checks if a username exists or not
# if it exists then it returns true, otherwise false
def isUsernameTaken(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM auth WHERE username='{username}';"
    )
    if cur.fetchone() is None:
        return False
    return True


def addUser():
    # Open a cursor to perform database operations
    conn = db_conn()
    cur = conn.cursor()
    while True:
        username = input("Enter a username: ")
        if isUsernameTaken(username):
            print("This username is already taken")
        else:
            break

    # finds out if password is allowed
    while True:
        password = input("Enter a password: ")
        if validatePassword(password) == 1:
            break
        print("Please enter a valid password\nA valid password contains 8-12 characters, a capital letter, a digit, and a non-alpha character.")

    first = input("First Name: ")
    last = input("Last Name: ")

    # insert user info
    auth = f"INSERT INTO auth(username, password, first_name, last_name) VALUES('{username}', '{password}', '{first}', '{last}');"
    control = f"INSERT INTO control(username, email, sms, advertising, language) VALUES('{username}', '{1}', '{1}', '{1}', '{'English'}');"
    profile = f"INSERT INTO profile(username, title, major, university, about) VALUES('{username}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}');"
    experiences = f"INSERT INTO experiences(username, title, employer, date_started, date_ended, location, description) VALUES('{username}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}');"
    education = f"INSERT INTO education(username, school, degree, year_attended) VALUES('{username}', '{'NULL'}', '{'NULL'}', '{'NULL'}');"

    cur.execute(auth, (username, password, first, last))
    cur.execute(control, (username, 1, 1, 1, 'English'))
    cur.execute(profile, (username, 'NULL', 'NULL', 'NULL', 'NULL'))
    cur.execute(experiences, (username, 'NULL', 'NULL',
                'NULL', 'NULL', 'NULL', 'NULL'))
    cur.execute(education, (username, 'NULL', 'NULL', 'NULL'))

    conn.commit()
    return 1


# Defult user for testing purposes. This is not used for any other context.
def addDefaultUser():
    username = "defultUser"
    password = "password1"
    first = "John"
    last = "Doe"
    title = "Mr."
    major = "Computer Science"
    university = "USF"
    about = "Lorem ipus"

    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # insert user info
    auth = f"INSERT INTO auth(username, password, first_name, last_name) VALUES('{username}', '{password}', '{first}', '{last}');"
    control = f"INSERT INTO control(username, email, sms, advertising, language) VALUES('{username}', '{1}', '{1}', '{1}', '{'English'}');"
    profile = f"INSERT INTO profile(username, title, major, university, about) VALUES('{username}', '{title}', '{major}', '{university}', '{about}');"
    experiences = f"INSERT INTO experiences(username, title, employer, date_started, date_ended, location, description) VALUES('{username}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}', '{'NULL'}');"
    education = f"INSERT INTO education(username, school, degree, year_attended) VALUES('{username}', '{'NULL'}', '{'NULL'}', '{'NULL'}');"

    cur.execute(auth, (username, password, first, last))
    cur.execute(control, (username, 1, 1, 1, 'English'))
    cur.execute(profile, (username, 'NULL', 'NULL', 'NULL', 'NULL'))
    cur.execute(experiences, (username, 'NULL', 'NULL',
                              'NULL', 'NULL', 'NULL', 'NULL'))
    cur.execute(education, (username, 'NULL', 'NULL', 'NULL'))

    conn.commit()
    return 1
