class Node:
  def __init__(self, item, next):
    self.item=item
    self.nex=next

class Stack:
  def __init__(self):
    self.last=None
  def push(self, item):
    self.last=Node(item, self.last)
  def pop(self):
    item=self.last.itemself.last=self.last.next
    return item


def isValid(self, s:str)->bool:
  stack=[]
  table={
  ')':'(',
  '}':'{',
  ']':'{',


  }


  for char in s:
    if char not in table:
      stack.append(char)
    elif not stack or table[char] != stack.pop():
      return False
  print('*',stack)
  return len(stack)==0


S=input()
for i in S:
  print(isValid(S, i))

#print(stack)