numberr=int(input())
for power in range(100):
    if(numberr==2**power):
        print("yes")
        break
else:
    print("no")
