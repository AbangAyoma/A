
#!/usr/bin/python3
"""
    importing the unittesting module
"""
import unittest
from models import user

class TestBaseModel(unittest.TestCase):
    def test_user(self):
        '''Testing if user John is equal to the user1 created'''
        self.assertIsEqual('John',user1)
