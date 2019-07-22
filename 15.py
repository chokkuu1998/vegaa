pp,qq=map(int,input().split())
for i in range(1,min(pp,qq)+1):
    if((pp%i==0) and (qq%i==0)):
        x=i
print(x)
