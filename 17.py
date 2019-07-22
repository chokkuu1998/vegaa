a,b=map(int,input().split())
d=input()
c=list(map(int,input().split()))
h=list(map(int,input().split()))
for i in h:
	c.append(i)
	print(max(c),end=' ')	
