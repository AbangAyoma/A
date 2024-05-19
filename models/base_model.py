#!/usr/bin/python3

'''import basic python modules'''

import cmd, uuid, shlex
from datetime import datetime

class BaseModel(cmd.Cmd):

    def __init__(self, id=None):
        """
        Initialize the BaseModel class.

        Parameters:
            id (optional): The unique identifier for the BaseModel instance. If not provided, a new UUID will be generated.

        Returns:
            None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel object.

        :return: A string in the format "BaseModel <id> <dict_repr>", where <id> is the object's id and <dict_repr> is the string representation of the BaseModel class's __dict__.
        :rtype: str
        """
        return 'BaseModel' + ' <' + self.id + '> '  + str(BaseModel.__dict__ )
    
    def __setattr__(self, name, value):
        """
        Set the value of an attribute of the object.

        Parameters:
            name (str): The name of the attribute to set.
            value: The value to set the attribute to.

        This method is overridden to update the `updated_at` attribute before setting any other attribute. It first checks if the attribute being set is not `updated_at`, and if so, it updates the `updated_at` attribute with the current datetime. Then, it calls the parent class's `__setattr__` method to set the attribute with the given value.

        Note:
            This method is called automatically when an attribute is set on an object.

        Example:
            obj = BaseModel()
            obj.name = "John"
            print(obj.updated_at)  # prints the current datetime
        """
        # Update the updated_at attribute before setting any attribute
        if name != 'updated_at':
            super().__setattr__('updated_at', datetime.now())
        super().__setattr__(name, value)

# Create an instance of MyObject
# obj = BaseModel()
# print("Created at:", obj.created_at)
# print("Updated at:", obj.updated_at)

# Modify an attribute
# obj.some_attribute = 'New Value'
# print("Updated at after modification:", obj.updated_at)

# Modify another attribute
# obj.another_attribute = 42
# print("Updated at after another modification:", obj.updated_at)

# obi = BaseModel()
# print(obi.id)
# print("\n")
# print(BaseModel.__dict__)
# print("\n")
# print(BaseModel)
