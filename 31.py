aa=input()
aa.split()
aa=a.replace(" ","")
bb=[i for i in aa if aa.count(i)==1]
cc=' '.join(bb)
print(cc.lower())
