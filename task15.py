a,b,c,d = ( int(input()) for i in range(4))
for i in range (c,d+1):
  print('\t',i,end='')
for i in range (a,b+1):
  print('\n', i,'\t',end='')
  for j in range(c,d+1):
    print(i*j, '\t', end='')
print()