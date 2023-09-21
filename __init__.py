from os import walk
import os.path
from json import loads


def load(path):
    this_dir, this_filename = os.path.split(__file__)
    file_path = os.path.join(this_dir, path)
    with open(file_path) as f:
        data = f.read()
    return loads(data)


def exist(path):
    this_dir, this_filename = os.path.split(__file__)
    file_path = os.path.join(this_dir, path)
    return os.path.exists(file_path)


def get_dir_files(path):
    this_dir, this_filename = os.path.split(__file__)
    dir_path = os.path.join(this_dir, path)
    return next(walk(dir_path), (None, None, []))[2]
