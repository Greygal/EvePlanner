import os
import shutil

__author__ = 'stkiller'

dir_name = os.path.dirname(os.path.realpath(__file__))
for (root, dirs, files) in os.walk(dir_name, topdown=False):
    for current_dir in dirs:
        path = os.path.join(root, current_dir)
        if current_dir == '__pycache__':
            print("Deleting : %s" % path)
            shutil.rmtree(path)
        elif not os.listdir(path):
            print("Deleting : %s" % path)
            shutil.rmtree(path)
