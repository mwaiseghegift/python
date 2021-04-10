import json

data = {
    "Name":"Gift",
    "age":8,
    "married":False,
    "movie_holic":True,
    "parents":("Mary","Grantone"),
    "kids":None,
    "cars":[
        {"model":"Tesla X", "horse_power":10000},
        {"model":"lamboghini_offroad","horse_power":20000}
    ]
}

json_data = json.dumps(data, indent=4)
print(json_data)

"""
use indent to make them readable
separator to change thir separator
"""