"""
python io.py [flags] directory
"""

import sys
from os import walk
from os import remove
import shutil
    files = []
    for (dirpath, dirnames, filenames) in walk(direc):
        files.extend(filenames)
        break

def copy(src, dest):
    shutil.copy(src, dest)

def move(src, dest):
 shutil.move(src, dest)

def delete(src):
  os.remove(src)
