import json

with open("1.json","r") as myfile:
    data = json.load(myfile)
    data_initial = data.copy()
    print(json.dumps(data, indent=4, sort_keys=True))
    to_add = {"week": 3}
    temp = data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]
    temp["week"] = 3
with open("1.json", "w") as myfile:
    myfile.write(json.dumps(data, indent=4))
with open("1.json", "r") as myfile:
    data1 = json.load(myfile)
    print(json.dumps(data1, indent=4, sort_keys=True))
