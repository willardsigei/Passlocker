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

