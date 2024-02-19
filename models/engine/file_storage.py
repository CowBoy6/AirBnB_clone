#!/usr/bin/python3
"""
    Define class FileS_torage Module
"""
import json
import sys
sys.path.append("/home/oussama/github/AirBnB_clone")
import models.base_model



class File_Storage:
    """
        Serializes instances to JSON file and deserializes to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Return the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Set new obj into __objects
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        self.__objects[key] = value_dict
    def save(self):
        """
        Serializes the objects into JSON file
        """
        new_objects={}
        try:
            for key,val in self.__objects.items():
                if type(val)!= type(dict):
                    new_objects[key]= val.to_dict()
        except AttributeError:
            pass


        with open(self.__file_path, mode='w') as fd:
            json.dump(new_objects, fd)

    def reload(self):
        """
        Reload the file and deserializes JSON into __objects
        """

        try:
            with open(self.__file_path, "r") as fd:
                self.__objects = json.load(fd)
        except FileNotFoundError:
            pass