"""
converting from json to python
You pass it with using json.loads()
"""

import json

data = '{"user":"Gift","email":"itsregalo047@gmail.com","course":"Computer Science","code":"p101","year":3}'

py_data = json.loads(data)
print(py_data["user"])