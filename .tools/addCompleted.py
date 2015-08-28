import sys

def addCompleted(currentTodoList,identifier):
  newDoc = []
  done = False
  for line in open(currentTodoList).readlines():
    if identifier in line and done==False and "c " not in line:
      done = True
      newDoc.append("c "+line)
    else:
      newDoc.append(line)
  f = open(currentTodoList, 'w+')
  for line in newDoc:
    f.write(line)

addCompleted(sys.argv[1],sys.argv[2])
