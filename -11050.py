import sys
input=sys.stdin.readline

def f(n,k):
  if memo[n][k]>0:
    return memo[n][k]
  if n==k or k==0:
    memo[n][k]=1
    return memo[n][k]
  memo[n][k]=f(n-1, k-1)+ f(n-1, k)
  return memo[n][k]


N, K=map(int, input().split())
memo=[[-1 for _ in range(N+1)] for _ in range(N+1)]
print(f(N,K))