dd=int(input())
ee=[]
for i in range(0,dd):
    ee.append(list(map(int,input().split())))
c=0
k=0
for i in range(0,dd):
    for j in range(0,dd):
        if ee[i][j]==1:
            if i!=dd-1 and ee[i+1][j]==0:
                c=c+1
            if j!=dd-1 and ee[i][j+1]==0:
                c=c+1
            if i!=0 and ee[i-1][j]==0:
                c=c+1
            if j!=0 and ee[i][j-1]==0:
                c=c+1
            if i==0 and j==0 or i==dd-1 and j==dd-1  or i==0 and j==dd-1 or i==dd-1 and j==0 and c==2:
                k=k+1
            elif i==1 and j>0 and j<dd-1 and c==3:
                k=k+1
            elif c==4:
                k=k+1
        c=0
                
print(k)
