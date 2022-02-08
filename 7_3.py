from os import path, listdir, walk
from shutil import copytree

project = 'my_project_1'

try:
    for root, dirs, files in walk(project):
        if 'templates' in dirs and root != project:
            for i in listdir(path.join(root, 'templates')):
                copytree(path.join(root, 'templates', i), path.join(project, 'templates', i))
except FileExistsError:
    print('Work has already been done')
