#!/usr/bin/python3
'''
    The Review class module
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
        Implementation of Review.
    '''
    place_id = ""
    user_id = ""
    text = ""
