"""
python io.py [flags] directory
"""

import sys
from os import walk
import shutil

def list(direc):
    files = []
    for (dirpath, dirnames, filenames) in walk(direc):
        files.extend(filenames)
        break

def copy(src, dest):
    shutil.copy(src, dest)

def move(src,dest):
    shutil.move(src, dest)
