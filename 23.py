aaa,bbb=map(int,input().split())
count=0
for i in range(aaa,bbb+1):
    s=math.sqrt(i)
    if math.sqrt(i)==int(s):
        count+=1
print(count)
