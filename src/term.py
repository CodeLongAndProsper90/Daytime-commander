import io

while True:
  line = raw_input("$ ").split(" ")
  if line[0] == 'l':
    if len(line) < 3:
      continue
    else:
       io.list()
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
