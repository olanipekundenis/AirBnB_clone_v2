#!/usr/bin/python3
"""file_storage.py module"""
import os
import json


class FileStorage():
    """serializes and deserializes to JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary as __object"""

        return FileStorage.__objects

    def new(self, obj):
        """format the key as object id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):

        """serializes __objects to JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """deserializes JSON file to __objects if JSON exits"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity

        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized_obj = None

            try:
                deserialized_obj = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized_obj is None:
                return

            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized_obj.items()}
