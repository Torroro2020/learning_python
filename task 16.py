a,b = ( int(input()) for i in range(2))
count = 0
sum = 0
if a%3 != 0:
  a+=1
for i in range (a, b + 1):
  if i%3 == 0:
    sum += i
    count += 1
  else:
    continue
print(sum / count)