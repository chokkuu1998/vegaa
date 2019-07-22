ll=list(map(str,input().split()))
cc=0
for i in range(len(ll[0])):
    if(ll[0][i]!=ll[1][i]):
        c+=1
bb=int(ll[2])
if(c==bb):
    print("yes")
else:
    print("no")
