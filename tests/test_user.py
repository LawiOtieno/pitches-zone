import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):

        '''

        testcase  to create an instance of User class.

        '''
        self.new_user = User(password = 'banana')


    def test_password_setter(self):
        
        '''

        testcase to  ascertain that when password is being hashed and the pass_secure contains a value.
        
        '''
        self.assertTrue(self.new_user.password_hash is not None)

        

    def test_no_access_password(self):
          
                '''

                testcase to comfirm the application raises Attribute error when a user tries to access the password property.

                '''
                with self.assertRaises(AttributeError):
                     self.new_user.password


    def test_password_verification(self):

        '''
        testcase to comfirm that password_hash can be verified when a user passes in the correct password.
        '''
        self.assertTrue(self.new_user.verify_password('banana'))    