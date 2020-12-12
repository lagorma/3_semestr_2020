import json

class MyClass:
    def __init__(self, name, surname, is_hired):
        self.name = name
        self.surname = surname
        self.is_hired = is_hired

    def __dict__(self):
        return {'name': self.name, 'surname': self.surname, 'is_hired': self.is_hired}

    def __str__(self):
        return f'MyClass({self.name},{self.surname},{self.is_hired})'


def obj_to_json(obj):
    data = obj.__dict__()
    #with open("data_file.json", "w") as write_file:
    #    json.dump(data, write_file)
    return json.dumps(data)


def json_to_obj(obj):
    return MyClass(**json.loads(obj))

'''
#test for obj_to_json
a = MyClass('me', 'my_surname', True)
s = obj_to_json(a)
print(s,type(s))

#test for json_to_obj
y = json_to_obj(s)
print(y,type(y))
'''
