nn1=int(input())
nn=math.radians(nn1)
if (nn>0 and nn<1):
    print(round(math.sin(nn),2),end='')
else:
    print(round(math.sin(nn)),end='')  
