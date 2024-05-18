#!/usr/bin/python3

'''import basic python modules'''

import cmd, uuid, shlex, datetime

class BaseModel(cmd.Cmd):
    '''BaseModel class is the base class for other instances'''
    def __init__(self, id=None):
        """
        Initialize the BaseModel class.
        """
        self.id = str(uuid.uuid4())

    def __str__(self):
        return 'BaseModel' + ' <' + self.id + '> '  + '<self.__dict__ >'

obi = BaseModel()
print(obi)
