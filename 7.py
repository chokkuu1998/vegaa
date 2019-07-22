ll,rr=map(int,input().split())

b=[]

for i in range(1,100000):

    if(i%ll==0 and i%rr==0):
    
        b.append(i)
        
b.sort()

print(b[0])
