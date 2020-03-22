"""
python io.py [flags] directory
"""

import sys
from os import walk
from os import remove
import shutil
import os.path
def List():
  files = []
  for (dirpath, dirnames, filenames) in walk(direc):
    files.extend(filenames)
    break

def copy(src, dest):
  if os.path.exists(src):
    shutil.copy(src, dest)
    return 0
  else:
    return 1
def move(src, dest):
  if os.path.exists(src):
    shutil.move(src, dest)
    return 0
  else:
    return 1
def delete(src):
  if os.path.exists(src):
    remove(src)
    return 0
  else:
    return 1
