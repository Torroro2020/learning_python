n = int(input())
if n%10==1 and ((n%100)//10)!=1:  print(str(n) + ' ' + 'программист') #здесь норм
elif (n%10==2 or n%10==3 or n%10==4) and n%100//10!=1:  print(str(n)+' '+ 'программиста')
else:  print(str(n)+' '+ 'программистов')