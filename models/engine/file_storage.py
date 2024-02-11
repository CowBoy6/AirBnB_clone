#!/usr/bin/python3
"""
    Define class FileS_torage Module
"""
import json
import sys
sys.path.append("/home/oussama/github/AirBnB_clone")
import models


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
        objects_dict = {}
        for key, val in self.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(self.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
        Reload the file and deserializes JSON into __objects
        """

        try:
            with open(self.__file_path, encoding="UTF8") as fd:
                self.__objects = json.load(fd)
            for key, val in self.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                self.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass