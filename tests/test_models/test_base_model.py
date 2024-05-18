
#!/usr/bin/python3
"""
    importing the unittesting module
"""
import unittest
from models import base_model

class TestBaseModel(unittest.TestCase):
    '''
        writing test  cases for  BaseModel
    '''

    def test_ID(self):
        self.assertIsInstance(BaseModel.id, str)
    
