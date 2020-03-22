from io import * 

while True:
  line = input("$ ").split(" ")
  if line[0] == 'l':
    if len(line) < 3:
      continue
    else:
      if len(line) == 1:
       List('.')
      else:
        List(line[1])
  if line[0] == 'c':
    if len(line) != 3:
      print("E: Argument mismatch: c <src> <dest>")
    else:
      copy(line[1], line[2])
  if line[0] == 'm':
    if len(line) != 3:
      print("E: Argument mismatch: m <src> <dest>")
    else:
      move(line[1], line[2])
  if line[0] == 'd':
    if len(line) != 2:
      print("E: Argument mismatch: d <file>")
    else:
      c = input("Are you sure? <y/N>: ")
      if c.lower() == 'y':
        delete(line[0])
