x,h,m = int(input()), int(input()), int(input())
hours = (x+(h*60)+m) // 60
minute = (x+(h*60)+m) % 60
print(hours)
print(minute)