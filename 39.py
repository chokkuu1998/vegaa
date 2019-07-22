numm=int(input())
aa=input().split(" ")
list1=[]
if(len(aa)==numm):
    for i in sorted(aa):
        list1.append(i)
if(list1==aa):
    print("yes")
else:
    print("no")
