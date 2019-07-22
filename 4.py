d=int(input())

ee=str(input())

ee=list(ee)

for i in ee:

	if(i=='a' or i=='ee' or i=='i' or i=='o' or i=='u'):
  
		ee.remove(i)
    
k=ee[::-1]

print("".join(k))
