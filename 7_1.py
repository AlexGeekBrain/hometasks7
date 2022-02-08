from os import path, makedirs

folders = {'my_project': [{'settings': []}, {'authapp': []}, {'adminapp': []}, {'authapp': []}]}

for key, val in folders.items():
    if not path.exists(key):
        for item in val:
            for i in item.keys():
                makedirs(path.join(key, i))
