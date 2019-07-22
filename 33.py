nn3=int(input())
count=0
for i in range(nn3):
    nn1,nn2=map(int,input().split())
    if nn1<nn2:
        count+=1
print(count,end='') 
