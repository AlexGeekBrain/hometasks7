import django
from os import walk, stat, path
from collections import defaultdict


def my_dir():
    root_dir = django.__path__[0]
    django_files = defaultdict(int)
    for root, dirs, files in walk(root_dir):
        for file in files:
            size = 10 ** len(str(stat(path.join(root, file)).st_size))
            django_files[size] += 1

    for size, num in sorted(django_files.items()):
        print(f'{size}: {num}')


my_dir()
