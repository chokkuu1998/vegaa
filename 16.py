mm,nn=map(int,input().split())
space=input()
aa=list(map(int,input().split()))
bb=list(map(int,input().split()))
cc=[]
for i in range(len(bb)):
  aa.append(bb[i])
  cc.append(max(aa))
print(*c,sep=' ')
