ma,nb=list(map(int,input().split()))

l=list(map(int,input().split()))

for s in range(0,nb):

  l=([l[-1]] + l[:-1])
  
print(*l)
