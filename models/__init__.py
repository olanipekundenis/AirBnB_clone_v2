#!/usr/bin/python3
"""__init__ initializes the models directory"""
from models.engine.file_storage import FileStorage
from models.engine.file_storage import FileStorage
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
