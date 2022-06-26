T= int(input())
for i in range(T):
  H, W,N=map(int, input().split())
  #print(N%H, N//H+1)
  if N%H==0:
    print(H*100+N//H)
  else:
    print(N%H*100+N//H+1)


  #print(N%H,N//H+1)
  #N//H=열수, N%H=층수
