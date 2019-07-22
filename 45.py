anglee=int(input())
bb=math.radians(anglee)
yy=math.sin(bb)
if(bb<1):
    print(round(yy,1))
elif(bb>1):
    print(round(yy))
