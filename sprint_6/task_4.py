# Class Student has attributes full_name:str, avg_rank: float, courses: list
# Class Group has attributes title: str, students: list.
# Make both classes JSON serializable. 
# Json-files represent information about student (students). 
# Create methods:  
# Student.from_json(json_file) that return Student instance from attributes from json-file;
# Student.serialize_to_json(filename)
# Group.serialize_to_json(list_of_groups, filename)
# Group.create_group_from_file(students_file)
# Parse given files, create instances of Student class and create instances of Group class 
# (title for group is name of json-file without extension).

import json
from json import JSONEncoder

class Student:
    def __init__(self, full_name, avg_rank, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def to_json(self):
        return {'full_name': self.full_name, 'avg_rank': self.avg_rank, 'courses': self.courses}

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, 'r') as file:
            json_data = json.load(file)
        return cls(json_data['full_name'], json_data['avg_rank'], json_data['courses'])

    def serialize_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_json(), file)

    @staticmethod
    def deserialize_from_json(filename):
        with open(filename, 'r') as file:
            json_data = json.load(file)
        return Student.from_json(json_data)

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

class Group:
    def __init__(self, title, students):
        self.title = title
        self.students = students

    def to_json(self):
        return {'title': self.title, 'students': [student.to_json() for student in self.students]}

    @classmethod
    def from_json(cls, json_data):
        students = [Student.from_json(student_data) for student_data in json_data['students']]
        return cls(json_data['title'], students)

    @staticmethod
    def serialize_to_json(groups, filename):
        data = [{'title': group.title, 'students': [student.to_json() for student in group.students]} for group in groups]
        with open(filename + ".json", 'w') as file:
            json.dump(data, file)

    @staticmethod
    def create_group_from_file(students_file):
        title = students_file.split('.')[0]
        students = [Student.deserialize_from_json(students_file)]
        return Group(title, students)
