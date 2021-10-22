import unittest
from users import User
from users import Credentials

class TestClass(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Willard','willard')

    def test_init(self):
        self.assertEqual(self.new_user.username,'Willard')
        self.assertEqual(self.new_user.password,'willard')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credentials('Gmail','willard','willard')
   
    def test_init(self):
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'willard')
        self.assertEqual(self.new_credential.password,'willard')

    def save_credential_test(self):
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_delete_credential(self):
        self.new_credential.save_details()
        test_credential = Credentials("facebook","willard","willard")
        test_credential.save_details()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_find_credentialr(self):
      
        self.new_credential.save_details()
        test_credential = Credentials("Instagram","willlard","willard") 
        test_credential.save_details()
        the_credential = Credentials.find_credential("Instagram")
        self.assertEqual(the_credential.account,test_credential.account)
