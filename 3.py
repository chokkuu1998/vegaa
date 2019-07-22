uu=int(input())

l=0

ru=uu

while uu>0:

  ru=uu%10
  
  l+=ru**2
  
  uu=uu//10
  
print(l)
