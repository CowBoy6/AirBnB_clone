#!/usr/bin/python3
import sys
sys.path.append('/home/oussama/github/AirBnB_clone') 
import models.engine.file_storage
import json
try:
    storage = models.engine.file_storage.File_Storage()
    storage.reload()
except json.decoder.JSONDecodeError :
    pass