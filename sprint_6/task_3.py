# In user.json file we have information about users in format [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...], 
# in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...]. 
# Function user_with_department(csv_file, user_json, department_json) should read from json files information and create csv file in format:
# header line - name, department
# next lines :  <userName>, <departmentName>
# If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.
# Create appropriate json-schemas for user and department.
# If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception  
# To validate instances create function validate_json(data, schema)

import json
import csv
from jsonschema import validate, ValidationError

class InvalidInstanceError(Exception):
    pass

class DepartmentNameError(Exception):
    pass

def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise InvalidInstanceError(f"Invalid JSON instance: {e.message}")

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_csv(csv_file, header, data):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

def user_with_department(csv_file, user_json, department_json):
    user_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "department_id": {"type": "integer"},
            },
            "required": ["id", "name", "department_id"],
        },
    }

    department_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
            },
            "required": ["id", "name"],
        },
    }

    users = read_json(user_json)
    departments = read_json(department_json)

    validate_json(users, user_schema)
    validate_json(departments, department_schema)

    header = ["name", "department"]
    data = []

    for user in users:
        department_id = user["department_id"]
        department = next((d["name"] for d in departments if d["id"] == department_id), None)
        if department is None:
            raise DepartmentNameError(f"Department with id {department_id} not found.")

        data.append([user["name"], department])

    write_csv(csv_file, header, data)
