import io

while True:
  line = raw_input("$ ").split(" ")
  if line[0] == 'l':
    if len(line) < 3:
      #
    else:
       io.list()
