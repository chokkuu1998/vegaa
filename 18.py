aa=input()
flag=0
for i in aa:
    if(aa.isdigit()==True):
        flag=1
    else:
        flag=0
        break
if(flag==0):
    print("no")
else:
    print("yes")
