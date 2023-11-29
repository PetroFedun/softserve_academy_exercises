# Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
# This class should contain method serialize for serialize object to filename according to  type. 
# For defining format create enum FileType with values JSON, BYTE.
# Create function serialize(object, filename, filetype).
# This function use SerializeManager and should serialize object to filename according to type.
# For example:
# if user_dict = { 'name': 'Roman', 'id': 8}
# then
# serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
# serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String"

import json
import pickle
from enum import Enum

class FileType(Enum):
    JSON = "json"
    BYTE = "byte"

class SerializeManager:
    def __init__(self, filename, file_type):
        self.filename = filename
        self.file_type = file_type

    def serialize(self, obj):
        if self.file_type == FileType.JSON:
            with open(self.filename, "w") as file:
                json.dump(obj, file)
        elif self.file_type == FileType.BYTE:
            with open(self.filename, "wb") as file:
                pickle.dump(obj, file)
        else:
            raise ValueError("Unsupported file type")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

def serialize(obj, filename, file_type):
    with SerializeManager(filename, file_type) as manager:
        manager.serialize(obj)
