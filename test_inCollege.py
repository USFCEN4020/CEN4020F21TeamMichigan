import pytest
from authorization import isAuthorized
from add_user import validatePassword, canAdd
from find_user import findUser


#should be able to run with py.test in terminal, add -v to see 


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
                            ('kevin23', 'Keva.2421',1),
                            ('nhi34', 'Nhi@nguyen35',1)                   
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


