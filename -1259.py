import sys
input=sys.stdin.readline
while True:
  N=input().rstrip()
  if N=="0":
    break
  print("yes" if N==N[::-1] else "no")
  #print(N)
