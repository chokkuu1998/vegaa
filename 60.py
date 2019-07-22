nn1=int(input())
ss=str(input())
a=""
r=""
for i in range(len(s)):
    if ss[i]=='1':
        aa=aa+ss[i]+" "
    elif ss[i]=='0':
        r=r+aa
        aa=""
print(r.strip())
