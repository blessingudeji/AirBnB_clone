#!/usr/bin/python3
from json import dump, load
import models

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
	objects_dict = {}
	for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

         with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
              dump(objects_dict, file)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as file:
                FileStorage.__objects = load(file)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
