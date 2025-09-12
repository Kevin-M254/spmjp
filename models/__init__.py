#!/usr/bin/python3
""" Instantiates an instance of Storage to be used """

from os import getenv

storage_t = getenv("SPMJP_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
