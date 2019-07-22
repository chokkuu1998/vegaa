nn23,kk,pp=map(str,input().split())
nn23=list(n23)
kk=list(k)
pp=int(p)
count=0
for i in range(0,len(nn23)):
        if(nn23[i]!=kk[i]):
            count=count+1
if(count==pp):
    print("yes")
else:
    print("no")
