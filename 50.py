zz1=int(input())
if(zz1>=-2**15+1 and zz1<=2**15+1):
  print('INT')
elif(zz1>=-2**31+1 and zz1<=2**31+1):
  print('LONG')
else:
  print('LONG LONG')  
