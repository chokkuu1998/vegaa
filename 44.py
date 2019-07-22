aaa,bbb= list(map(str,input().split()))
bbb=int(bbb)
for i in range(bbb):
  ccc= ""
  ccc += aaa[-1]
  for i in range(len(aaa)-1):
    ccc+= aaa[i]
  aaa= ccc
print(aaa)
