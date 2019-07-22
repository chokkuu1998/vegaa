xx,yy=list(map(int,input().split()))
ii,jj=list(map(int,input().split()))
kk,ll=list(map(int,input().split()))
if (xx==ii==kk) or (yy==jj==l) or (xx==yy) or (ii==jj) or (kk==l) :
    print("yes")
else:
    print("no")
