list = [int(i) for i in input().split()]
cnt = len(list)
if cnt > 1:
    for i in range(cnt):
        print(list[i-1] + list[(i+1) % cnt], end=' ')
else:
    print(*list)