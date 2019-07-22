AA1=int(input())

BB1=[]

for i in range (2,AA1+1):

	if(AA1%i)==0:
  
		BB1.append(i)
    
		AA1=AAA1//i
    
k1=sorted(BB1)

print(*k1)
