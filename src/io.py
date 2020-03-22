"""
python io.py [flags] directory
"""

import sys
from os import walk
from os import remove
files = []
for (dirpath, dirnames, filenames) in walk(sys.argv[-1]):
    files.extend(filenames)
    break

def copy(src, dest):
  import shutil
  shutil.copy(src, dest)

def move(src, dest):
 shutil.move(src, dest)

def delete(src):
  os.remove(src)
