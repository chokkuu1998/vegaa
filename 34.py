kk=int(input())
numm=[]
for i in range (2,kk+1):
    if(kk%i==0 and i%2==0):
        numm.append(i)
print(*numm)
