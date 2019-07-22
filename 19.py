aa23=int(input())
lli=list(map(str,input().split()[:aa23]))
lli.sort()
lli.sort(key=len)
for i in lli:
        print(i,end=" ")
