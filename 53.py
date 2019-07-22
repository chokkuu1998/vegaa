aa,bb=list(map(int,input().split()))
cc=list(map(int,input().split()))[:aa]
for i in range(0,bb):
  if(i==bb-1):
    print(cc[i])
