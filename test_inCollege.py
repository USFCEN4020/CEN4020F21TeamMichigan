import pytest
from authorization import isAuthorized
from find_user import findUser
from user_profile import updateTitle, updateMajor, updateUniName, updateAbout, viewProfile, updateExp, updateEdu, updateProfile
from add_user import addDefaultUser
import io
import sys
import app


# should be able to run with py.test in terminal, add -v to see

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


########################################################## EPIC 5 ##############################################################
