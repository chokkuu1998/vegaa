ann1,ann2,ann3=map(int,input().split(" "))
if(ann1!=0 and ann2!=0 and ann3!=0):
    a=ann1+ann2+ann3
else:
    a=0
if(a==180):
    print("yes")
else:
    print("no")
