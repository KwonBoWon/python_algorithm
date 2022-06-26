from sys import stdin
stack = []
N = int(input())

for _ in range(N):
  order = stdin.readline().split()
  if order[0] == 'pop':
    if len(stack) == 0:
      print("-1")
    else:
      print(stack.pop())
  elif order[0] == 'size':
    print(len(stack))
  elif order[0] == 'empty':
    print(1-(bool(stack)))
  elif order[0] == 'top':
    if len(stack) == 0:
      print("-1")
    else:
      print(stack[-1])
  else:#push x
    stack.append(order[1]) 