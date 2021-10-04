import pytest
from authorization import isAuthorized
from add_user import validatePassword, canAdd
from find_user import findUser
from tud_test_base import set_keyboard_input, get_display_output
from navigation_links import general, importantLink


"""
run with py.test in terminal,
add -v to see more detailed information about the tests
add -vv to see even more details

tutorial for testing commandline input and output:
https://www.youtube.com/watch?v=tBAj2FqgIwg 
"""
#################################### Week 3 testing ######################################

### Useful links tests ###

## General
#link to sign up page

gen_output = ["Type your option to view: ",
    "1. Sign up",
    "2. Help Center",
    "3. About",
    "4. Press",
    "5. Blog",
    "6. Careers",
    "7. Developers",
    "8. Go back",]


def test_general_signup():
    set_keyboard_input(["1"])
    general()
    output = get_display_output()
    assert output == gen_output + ["All permitted accounts have been created, please come back later"]

    #Help center produces "We're here to help"
def test_general_helpcenter():
    set_keyboard_input(["2"])
    general()
    output = get_display_output() 
    assert output == gen_output + ["\nWe're here to help!\n"]



#About displays: 
#In College: Welcome to In College, the world's largest
#college student network with many users in many countries and territories
#worldwide

def test_general_about():
    set_keyboard_input(["3"])
    general()
    output = get_display_output()
    assert output == gen_output + ["\nWelcome to InCollege, the world's largest college student network with many users in many countries and territories worldwide.\n"]


#Press displays:
#In College Pressroom: Stay on top of the latest news, updates, and reports
def test_general_press():
    set_keyboard_input(["4"])
    general()
    output = get_display_output()
    assert output == gen_output + ["\nIn College Pressroom: Stay on top of the lastest news, updates, and reports.\n"]

#Blog, Careers, and Developers will display "under construction"
def test_general_rest():
    set_keyboard_input(["5"])
    general()
    output = get_display_output()
    assert output == gen_output + ["\nUnder construction\n"]

    set_keyboard_input(["6"])
    general()
    output = get_display_output()
    assert output == gen_output + ["\nUnder construction\n"]

    set_keyboard_input(["7"])
    general()
    output = get_display_output()
    assert output == gen_output + ["\nUnder construction\n"]



links = ['Type your option to view: ',
    "1. A Copyright Notice",
    "2. About",
    "3. Accessibility",
    "4. User Agreement",
    "5. Privacy Policy",
    "6. Cookie Policy",
    "7. Copyright Policy",
    "8. Brand Policy",
    "9. Guest Control",
    "10. Language",
    "11. Go back"]
### inCollege Important links test ###
##Copyright notice
def test_copyright_notice():
    set_keyboard_input(["1"])
    importantLink("kevin23")
    output = get_display_output()
    assert output == links + ["\nAll rights are reserved for the inCollege Team Michigan. All images and or text afiliated to this site is as well under the ownership off all members aboard the team. All accounts created withing the site are private from third party sources and all data is to be stored on the affiliated owners server.\n"]


##About
def test_about():
    set_keyboard_input(["2"])
    importantLink("kevin23")
    output = get_display_output()
    assert output == links + ["/nThis website was created with the intent of promoting success in graduation college students./n"]


##Accessibility
def test_access():
    set_keyboard_input(["3"])
    importantLink("kevin23")
    output = get_display_output()
    assert output == links + ["\nAs of now this program does not comply with any additional functionality for disabilities\n"]


##User Agreement
def test_user_agreement():
    set_keyboard_input(["4"])
    importantLink("kevin23")
    output = get_display_output()
    assert output == links + ["\nCreating an account hereby signifies that the user has agreeed to the terms and conditions of the app. All personal data is protected to the extent of the affiliated owners hardware.\n"]


##Privacy Policy
def test_privacy():
    set_keyboard_input(["5"])
    importantLink("kevin23")
    output = get_display_output()
    assert output == links + [""]


##cookie policy
def test_cookie():
    set_keyboard_input(["6"])
    importantLink("kevin23")
    output = get_display_output()
    assert output == links + ["\nAll personal data is protected to the extent of the affiliated owners hardware. The affiliated owners are not responsible for data breaches and or attacks to the hardware physically or otherwise.\n"]


##Copyright Policy
def test_copyright_policy():
    set_keyboard_input(["7"])
    importantLink("kevin23")
    output = get_display_output()
    assert output == links + ["\nAll text and images associated to the site are the property of the owners. Any use of the content outside the context of this application is prohibited by law.\n"]


##Brand Policy
def test_brand_policy():
    set_keyboard_input(["8"])
    importantLink("kevin23")
    output = get_display_output()
    assert output == links + ["\nUser cookies are used to ensure the convience of our user. All personal data is protected within the context of our hardware security.\n"]


##Guest Controls
def test_guest_controls():
    set_keyboard_input(["9"])
    importantLink("kevin23")
    output = get_display_output()
    assert output == links + ["\nGuests have limited access to the site. In order to ensure full access a valid account must be created and verified.\n"]


##Languages
def test_languages():
    set_keyboard_input(["10"])
    importantLink("kevin23")    #insert a valid account username to test
    output = get_display_output()
    assert output == links + ["Select your language: \n1. English \n2. Spanish"]


##########################################################################################



#check if isAuthorize correctly detects account already exists in the database
#for accounts that return 1, change the username and password into what you have in your database
@pytest.mark.parametrize('username, password, result',
    #return 0 if account doesnt exist
    [
                            ('anessa23', 'An23@abc1', 0),
                            ('jim2301', 'Jim@2a53f', 0),
                            ('panther902', 'P4na3.def', 0),
                            ('kelly324', 'kElly34.xyz',0),
    #return 1 if account already exists
    #Change these values into any account you have in your database
    #Or sign up with these accounts before testing
                            ('kevin23', 'Keva.2421',1),
                            ('nhi34', 'Nhi@nguyen35',1)
    ]

)
def test_isAuthorized(username, password, result):
    assert isAuthorized(username, password) == result

@pytest.mark.parametrize('first, last, result',
    #return 0 if user is not found
    [
                            ('anessa23', 'An23@abc1', 0),
                            ('jim2301', 'Jim@2a53f', 0),
                            ('panther902', 'P4na3.def', 0),
                            ('kelly324', 'kElly34.xyz',0),
    #return 1 if user is found
    #Change these values into any account you have in your database
    #Or sign up with these accounts before testing
                            ('Kevin', 'va',1),
                            ('Nhi', 'N',1)                   
    ]
)
def test_find_user(first,last, result):
    assert findUser(first,last) == result



#this function checks if the password is valid
@pytest.mark.parametrize('password, result',
                         [
                            #invalid passwords
                            ('1232', 0),
                            ('2_Shor!', 0),
                            ('abcdefg8!', 0),
                            ('TooLong_Pa55word',0),
                            ('missingcap1!',0),
                            ('NononAlph5',0),                          
                            #valid passwords
                            ('Mark@1234',1),
                            ('aneSsa.9',1),
                            ('h0uS2@jd',1),

                         ]
                         )
def test_validatePassword(password, result):
    assert validatePassword(password) == result



#this function checks if user can sign up based on the number of accounts in the database
def test_canAdd():
    #if the number of accounts is less than 5, return true
    assert(canAdd([(1, )]) == 1)
    assert(canAdd([(2, )]) == 1)
    assert(canAdd([(4, )]) == 1)
    assert(canAdd([(-1, )]) == 1)
    assert(canAdd([(0, )]) == 1)

    #if the number of accounts is more than 5, return false
    assert(canAdd([(5, )]) == 0)
    assert(canAdd([(6, )]) == 0)


