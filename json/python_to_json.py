"""
converting from python to json
we use json.dumps()
"""

import json

data = {
    "user":"Gift",
    "course":"Computer Science",
    "DOB":"2020",
    "status":"single"
}

json_data = json.dumps(data)
print(json_data)