numbb=int(input())
list1=[]
for i in range(1,numbb+1):
    if(numbb%i==0):
        list1.append(i)
for num in list1:
    if(num%2!=0):
        print(num,end=" ")
