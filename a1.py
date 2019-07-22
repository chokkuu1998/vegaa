pp1,aa1=map(int,input().split())
z=[(k,l) for k in range(pp1) for l in range(pp1) if k+l==(pp1/2) and k*l==aa1]
if len(z)>0:
    print("yes",end='')
else:
    print("no",end='') 
