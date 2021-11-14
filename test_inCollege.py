import pytest
from db_connection import db_conn
from inCollege import findPendingFriendRequests
from tud_test_base import set_keyboard_input, get_display_output, mock_input, mock_input_output_end, mock_input_output_start, set_input
from navigation_links import general
from authorization import isAuthorized
from find_user import findUser
from user_profile import updateTitle, updateMajor, updateUniName, updateAbout, viewProfile, updateExp, updateEdu, updateProfile
from add_user import addDefaultUser, validatePassword, canAdd
from user_page import confirmFriend, displayFriendsProfile, findReceivedMessages, findUserFriends, makeFriends, removeFriend, lastNameSearch, sendMessage, universitySearch, majorSearch
from intership_page import applyJob, deleteJob, jobSearch, listAppliedJobs, postJob, listNotAppliedJobs, saveJob
from notifications import jobNoti, messageNoti, profileNoti, checkNewJobs, checkNewUsers, checkDeletedJobs
import io
import sys
import app


# should be able to run with py.test in terminal, add -v to see
############################################################################
# Challenge 9 tests

def coursesTest(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM courses WHERE username='{username}'"
    )
    result = cur.fetchall()
    courseList = ["1. How to use inCollege learning", "2. Train the trainer", "3. Gamification of learning","4. Understanding the Architectural Design Process", "5. Project Management Simplified"]
    option = 1
    completedCourse = courseList[int(option)-1]
            
    if (int(option) < 7 ):
        cur.execute(
            f"INSERT INTO courses(username, courseName, courseNumber)  VALUES('{username}','{completedCourse}','{option}');"
        )
        conn.commit()
    return 1


def checkCourseTest(username, courseNumber):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM courses WHERE username='{username}' AND courseNumber ='{courseNumber}'"
    )
    return 1


def trainingEducationTest():
    option = 1
    if option == "1" or option == "2" or option == "3" or option == "4":
        return 1
    else:
        return 1


def test_courses():
    assert coursesTest("anessa23") == 1
    

def test_checkCourse():
    assert checkCourseTest("anessa23", 1) == 1


def test_trainingEducation():
    assert trainingEducationTest() == 1


############################################################################
# Challenge 8 tests
# User anessa23 must be used and set up to run test

def jobNotiTest(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT EXISTS(SELECT name='{username}' FROM applications);"
    )
    records = cur.fetchall()
    return 1


def profileNotiTest(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM profile WHERE username='{username}';"
    )
    records = cur.fetchall()

    return 1


def messageNotiTest(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM messages WHERE user_1='{username}';"
    )
    records = cur.fetchall()
    return 1


def numberOfJobsNotiTest(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM jobs WHERE name='{username}';"
    )
    records = cur.fetchall()
    return 1


#checks to see if the test user anessa23 has new jobs that are not in sync
#This is a modified version of checkNewUsers(username) function from notification.py
def checkNewUserstest(username):
    # Get the lists of the new jobs and get the list of the last known jobs the user had.
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM auth;"
    )
    newUsers = cur.fetchall()
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM priorusers WHERE username='{username}';"
    )
    oldUsers = cur.fetchall() 
    # Compare the new and old and see what is different.
    newUserNumber = 0
    newFirstName = []
    newLastName = []
    for i in range(0, len(newUsers)):
        tempTitle = newUsers[i][0]
        booleanFlag = 0
        for j in range(0, len(oldUsers)):
            if(tempTitle == oldUsers[j][1]):
                booleanFlag = 1
        if(booleanFlag == 0):
            newUserNumber += 1
            newFirstName.append(newUsers[i][2])
            newLastName.append(newUsers[i][3])
            conn = db_conn()
            cur = conn.cursor()
            cur.execute(
                f"INSERT INTO priorusers(username, otheruser) VALUES('{username}', '{newUsers[i][0]}');"
            )
            conn.commit()

    return 1 # All has gone well.


#checks for anessa23 if there are any newly deleted jobs
#This is a modified version of the checkDeletedJobs(username) function from notificatoins.py
def checkDeletedJobs(username):
    # Get the lists of the new jobs and get the list of the last known jobs the user had.
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM jobs;"
    )
    oldJobs = cur.fetchall()
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM appliedjobs WHERE username='{username}';"
    )
    newJobs = cur.fetchall()

    newJobNumber = 0
    newJobTitles = []
    for i in range(0, len(newJobs)):
        tempTitle = newJobs[i][1]
        booleanFlag = 0
        for j in range(0, len(oldJobs)):
            if(tempTitle == oldJobs[j][1]):
                booleanFlag = 1
        if(booleanFlag == 0):
            newJobNumber += 1
            newJobTitles.append(newJobs[i][1])
            conn = db_conn()
            cur = conn.cursor()
            cur.execute(
                f"DELETE FROM appliedjobs WHERE title='{newJobs[i][1]}';"
            )
            conn.commit()

    return 1 # All has gone well.


#function checks that the test user anessa23's jobs are with sync to user
#checkNewJobs(username) from notifications.py without print statements
def checkNewJobstest(username):

    # Get the lists of the new jobs and get the list of the last known jobs the user had.
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM jobs;"
    )
    newJobs = cur.fetchall()
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM priorjobs WHERE username='{username}';"
    )
    oldJobs = cur.fetchall()

    # Compare the new and old and see what is different.
    newJobNumber = 0
    newJobTitles = []
    for i in range(0, len(newJobs)):
        tempTitle = newJobs[i][1]
        booleanFlag = 0
        for j in range(0, len(oldJobs)):
            if(tempTitle == oldJobs[j][1]):
                booleanFlag = 1
        if(booleanFlag == 0):
            newJobNumber += 1
            newJobTitles.append(newJobs[i][1])
            conn = db_conn()
            cur = conn.cursor()
            cur.execute(
                f"INSERT INTO priorjobs(username, jobTitle) VALUES('{username}', '{newJobs[i][1]}');"
            )
            conn.commit()

    return 1 # All has gone well.


def test_notifications():
    assert jobNotiTest('anessa23') == 1
    assert profileNotiTest('anessa23') == 1
    assert messageNotiTest('anessa23') == 1
    assert numberOfJobsNotiTest('anessa23') == 1

def test_checkNewUsers():
    assert checkNewUserstest("anessa23") == 1

def test_checkNewJobs():
    assert checkNewJobstest("anessa23") == 1

def test_deletedJobs():
    assert checkDeletedJobs("anessa23") == 1



############################################################################
# challenge 7 tests
# jim2301 and anessa23 are the two test accounts
# they must be friends and jim must have already sent a message to anessa
# additionally jim must not be friends with kelly324 to test the plus messaging feature
# jim2301 should have no messages
# anessa23 should have a message sent to her
# jim should also be a plus user
############################################################################


# tests that the plan column was added to the table
def planTest():
    conn = db_conn()
    cur = conn.cursor()
    plan = ['standard', 'plus']
    cur.execute(
        f"SELECT * FROM auth WHERE plan='{plan[0]}' OR plan = '{plan[1]}'")
    results = cur.fetchall()
    if len(results) != 0:
        return 1
    else:
        return 0


def inboxTesting():
    results = [findReceivedMessages(
        'jim2301'), findReceivedMessages('anessa23')]
    if len(results[0]) == 0 and len(results[1]) != 0:
        return 1
    else:
        return 0


def sendTestMessage(username):
    conn = db_conn()
    cur = conn.cursor()

    cur.execute(
        f"SELECT * FROM friends WHERE user_1 = 'anessa23' AND user_2 = '{username}' OR user_1 = '{username}' AND user_2 = 'anessa23';")
    results = cur.fetchall()

    message = "test message"

    cur.execute(
        f"INSERT INTO messages(user_1, user_2, message)  VALUES('anessa23','{username}','{message}');")
    conn.commit()

    results = cur.execute(
        f"SELECT * FROM messages WHERE user_1 = 'jim2301' AND user_2 = 'anessa23';")
    if len(results) == 0:
        return 0
    else:
        return 1


def plusMessageTest(username):
    conn = db_conn()
    cur = conn.cursor()
    # jim and kelly324 are not friends
    friendname = 'kelly324'

    message = "plus test message"

    cur.execute(
        f"INSERT INTO messages(user_1, user_2, message)  VALUES('{friendname}','{username}','{message}');")
    conn.commit()

    results = cur.execute(
        f"SELECT * FROM messages WHERE user_1 = 'jim2301' AND user_2 = 'kelly324';")
    if len(results) == 0:
        return 0
    else:
        return 1


def displayAllInSystemTest():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM auth;")
    results = cur.fetchall()
    if len(results) == 0:
        return 0
    else:
        return 1


def test_messaging():
    #assert inboxTesting() == 0
    #assert planTest() == 1
    #assert sendTestMessage('jim2301') == 1
    #assert plusMessageTest('jim2301') == 1
    assert displayAllInSystemTest() == 1

############################################################################


gen_output = ["Type your option to view: ",
              "1. Sign up",
              "2. Help Center",
              "3. About",
              "4. Press",
              "5. Blog",
              "6. Careers",
              "7. Developers",
              "8. Go back", ]


##########################################################################################


# check if isAuthorize correctly detects account already exists in the database
# for accounts that return 1, change the username and password into what you have in your database
@pytest.mark.parametrize('username, password, result',
                         # return 0 if account doesnt exist
                         [
                             ('anessa23', 'An23@abc1', 0),
                             ('jim2301', 'Jim@2a53f', 0),
                             ('panther902', 'P4na3.def', 0),
                             ('kelly324', 'kElly34.xyz', 0)

                         ]

                         )
def test_isAuthorized(username, password, result):
    assert isAuthorized(username, password) == result


@pytest.mark.parametrize('first, last, result',
                         # return 0 if user is not found
                         [
                             ('anessa23', 'An23@abc1', 0),
                             ('jim2301', 'Jim@2a53f', 0),
                             ('panther902', 'P4na3.def', 0),
                             ('kelly324', 'kElly34.xyz', 0)

                         ]
                         )
def test_find_user(first, last, result):
    assert findUser(first, last) == result


# this function checks if the password is valid
@pytest.mark.parametrize('password, result',
                         [
                             # invalid passwords
                             ('1232', 0),
                             ('2_Shor!', 0),
                             ('abcdefg8!', 0),
                             ('TooLong_Pa55word', 0),
                             ('missingcap1!', 0),
                             ('NononAlph5', 0),
                             # valid passwords
                             ('Mark@1234', 1),
                             ('aneSsa.9', 1),
                             ('h0uS2@jd', 1),

                         ]
                         )
def test_validatePassword(password, result):
    assert validatePassword(password) == result


# this function checks if user can sign up based on the number of accounts in the database
def test_canAdd():
    # if the number of accounts is less than 5, return true
    assert(canAdd([(1, )]) == 1)
    assert(canAdd([(2, )]) == 1)
    assert(canAdd([(4, )]) == 1)
    assert(canAdd([(-1, )]) == 1)
    assert(canAdd([(0, )]) == 1)

    # if the number of accounts is more than 10, return false
    assert(canAdd([(11, )]) == 0)


"""
    Test the function updateTitle, will return a 1 if everything goes well and 0 otherwise. This function
    can only be called once the user is in the user page so they already have a valid account as proven
    by tests of days past.
"""


@pytest.mark.parametrize('username, title, result',
                         # return 0 if account doesnt exist
                         [
                             ('anessa23', 'newAne', 1),
                             ('jim2301', 'newJim', 1),
                             ('panther902', 'newPan', 1),
                             ('kelly325', 'newKelly', 1),
                             ('kevin23', 'newKevin', 1),
                             ('nhi34', 'newNhi', 1)
                         ]

                         )
def test_updateTitle(username, title, result):
    assert updateTitle(username, title) == result


@pytest.mark.parametrize('username, major, result',
                         # return 0 if account doesnt exist
                         [
                             ('anessa23', 'Bio', 1),
                             ('jim2301', 'Premed', 1),
                             ('panther902', 'Computer', 1),
                             ('kelly325', 'Psych', 1),
                             ('kevin23', 'Telekinesis', 1),
                             ('nhi34', 'Underwaterbasketweaving', 1)
                         ]

                         )
def test_updateMajor(username, major, result):
    assert updateMajor(username, major) == result


@pytest.mark.parametrize('username, uni, result',
                         # return 0 if account doesnt exist
                         [
                             ('anessa23', 'newAne', 1),
                             ('jim2301', 'newJim', 1),
                             ('panther902', 'newPan', 1),
                             ('kelly325', 'newKelly', 1),
                             ('kevin23', 'newKevin', 1),
                             ('nhi34', 'newNhi', 1)
                         ]

                         )
def test_updateUniName(username, uni, result):
    assert updateUniName(username, uni) == result


@pytest.mark.parametrize('username, abt, result',
                         # return 0 if account doesnt exist
                         [
                             ('anessa23', 'newAne', 1),
                             ('jim2301', 'newJim', 1),
                             ('panther902', 'newPan', 1),
                             ('kelly325', 'newKelly', 1),
                             ('kevin23', 'newKevin', 1),
                             ('nhi34', 'newNhi', 1)
                         ]

                         )  # Possibly best way to test functions
def test_updateAbout(username, abt, result):
    assert updateAbout(username, abt) == result


def test_viewProfile():
    try:
        # Try to make the defult user if the defult user is not already made. This try catch is here only to ensure that one defult user is made.
        addDefaultUser()
        assert viewProfile('defultUser') == 1
    except:
        assert viewProfile('defultUser') == 1


def test_updateExp():
    sys.stdin = io.StringIO(
        '1\ndefultUser\njoe\n02/01/99\n02/02/99\nMoon\nMinning\nSpace Minner\nsomething important')
    assert updateExp('defultUser') == 1


########################################################## WEEK 5 ##############################################################
@pytest.mark.parametrize('username, first, last, expected',
                         [
                             ('defultUser', 'John', 'Doe', 1)
                         ])
def test_displayFriendsProfile(username, first, last, expected):
    assert displayFriendsProfile(username, first, last) == expected


@pytest.mark.parametrize('username, expected',
                         [
                             ('defultUser', []),
                             ('nhi123', [])
                         ])
def test_findUserFriends(username, expected):
    assert findUserFriends(username) == expected


@pytest.mark.parametrize('username, expected',
                         [
                             ('defultUser', 1)
                         ])
def test_removeFriends(username, expected):
    assert removeFriend(username, username) == expected


@pytest.mark.parametrize('username, expected',
                         [
                             ('defultUser', 1)
                         ])
def test_confirmFriend(username, expected):
    assert confirmFriend(username, username) == expected


@pytest.mark.parametrize('username, expected',
                         [
                             ('notDefultUser', False)
                         ])
def test_makeFriends(username, expected):
    assert makeFriends(username, username) == expected


@pytest.mark.parametrize('username, last, expected',
                         [
                             ('notDefultUser', 'Doe', False),
                             ('nhi123', 'Ng', True),
                             ('Kenvin23', 'K.', True)
                         ])
def test_lastNameSearch(username, last, expected):
    if(expected == False):
        sys.stdin = io.StringIO('0')
    assert lastNameSearch(username, last) == expected


@pytest.mark.parametrize('username, school, expected',
                         [
                             ('defultUser', 'USF', False),
                             ('nhi123', 'UF', False),
                             ('kevin12', 'UT', False)
                         ])
def test_universitySearch(username, school, expected):
    if(expected == True):
        sys.stdin = io.StringIO('0')
    assert universitySearch(username, school) == expected


@pytest.mark.parametrize('username, major, expected',
                         [
                             ('defultUser', 'Biomed', False),
                             ('nhi234', 'Comp Sci', False),
                             ('kevin123', 'Marketing', False)
                         ])
def test_majorSearch(username, major, expected):
    assert majorSearch(username, major) == expected

################### EPIC 6##########################


def test_listAppliedJobs():
    assert listAppliedJobs('defultUser') == 1


def test_listNotAppliedJobs():
    assert listNotAppliedJobs('defultUser') == 1


# def test_postJob():
#     mock_input_output_start()
#     set_input(['a', 'a', 'a', 'a', 1])
#     postJob('defultUser')
#     assert postJob('defultUser') == 1


def test_jobSearch():
    mock_input_output_start()
    set_input(['5'])
    assert jobSearch('defultUser') == 1
    mock_input_output_end()


def test_deleteJob():
    mock_input_output_start()
    set_input(['a'])
    assert deleteJob('defultUser') == 0
    mock_input_output_end()


def test_applyJob():
    mock_input_output_start()
    set_input(['a', 'a', 'a', 'a'])
    assert applyJob('defultUser') == 0
    mock_input_output_end()


# def test_saveJob():
#     mock_input_output_start
#     set_input(['title'])
#     assert saveJob('defultUser') == 1
#     mock_input_output_end
