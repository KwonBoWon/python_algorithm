from itertools import combinations

N, M=map(int , input().split())

cards=list(map(int , input().split()))

com=list(combinations(cards,3))

maxi=0
for i in com:
  if sum(i)<=M:
    maxi=max(sum(i), maxi)

print(maxi)
