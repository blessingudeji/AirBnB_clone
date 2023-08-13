#!/usr/bin/python3
'''
    Tests for the state module
'''
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    '''
        Tests the State class.
    '''

    def test_State_inheritence(self):
        '''
            Tests that State class inherits from BaseModel.
        '''
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        '''
            Tests that State class contains the attribute `name`.
        '''
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        '''
            Tests that State class attribute name is class type str.
        '''
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
