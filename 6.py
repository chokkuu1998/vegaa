array_size=input()

array=list(map(int,input().split()))

ss=1

for i in array:

    if array.count(i)==ss:
    
        print(i)
        
        break;
        
    else:
    
        continue;
