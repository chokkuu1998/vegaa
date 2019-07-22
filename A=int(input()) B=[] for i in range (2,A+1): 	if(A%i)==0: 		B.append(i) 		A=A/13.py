AA=int(input())
BB=[]
for i in range (2,AA+1):
	if(AA%i)==0:
		BB.append(i)
		AA=AA//i
k=sorted(BB)
print(*k)
