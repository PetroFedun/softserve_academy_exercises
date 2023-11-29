# Create function find(file, key)
# This function parses json-file and returns all unique values of the key.
# 1.json:
# [{"name": "user_1”, "password": "pass_1”},
# {"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
# find("1.json", "password") returns ["pass_1", "qwerty"]
# 2.json:
# [{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
# find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]
# 3.json:
# {"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
# find("3.json", "password") returns ["1234qweQWE"]

import json

def find(file, key):
    unique_values = []

    def extract_values(data):
        if isinstance(data, list):
            for item in data:
                extract_values(item)
        elif isinstance(data, dict):
            for k, v in data.items():
                if k == key:
                    if isinstance(v, list):
                        unique_values.extend(v)
                    else:
                        unique_values.append(v)
                elif isinstance(v, (list, dict)):
                    extract_values(v)

    with open(file, 'r') as json_file:
        data = json.load(json_file)
        extract_values(data)
    return list(set(unique_values))
