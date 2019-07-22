numberr_ob=int(input())
for i in range(2,numberr_ob):
    if(numberr_ob%i==0):
        print("yes")
        break
else:
    print("no")
