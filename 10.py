aa11=int(input())

bb11=[]

for i in range (2,aa11+1):

	if(aa11%i)==0:
  
		bb11.append(i)
    
		aa11=aa11//i
    
k1=sorted(bb11)

print(*k1
