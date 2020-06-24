a,b,h = int(input()),int(input()),int(input())
if a <= h <= b: print('Это нормально')
elif a <= b < h: print('Пересып')
else: print('Недосып')