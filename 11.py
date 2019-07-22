rrs1=int(input())
ll2=[]
for j in range (2,rrs1+1):
    if(rrs1%j)==0:
        ll2.append(j)
        rrs1=rrs1//j
o=sorted(ll2)
print(*o)
