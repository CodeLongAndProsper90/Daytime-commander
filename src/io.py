"""
python io.py [flags] directory
"""

import sys
from os import walk

files = []
for (dirpath, dirnames, filenames) in walk(sys.argv[-1]):
    files.extend(filenames)
    break

def copy(src, dest):
  import shutil
  shutil.copyfile(src, dest)
